"""Background worker executed off-path to parse transcript and propose skill/rule updates.
Runs non-blocking, redacts data, checks for actionable patterns, and submits to promoter.
"""
import argparse
import json
import logging
import os
import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import CAPTURE_MAX_WINDOW_BYTES, get_workspace_state_dir
from src import admission_promoter, friction_detector, redact


def setup_logger(workspace_root: Path):
    log_file = get_workspace_state_dir(workspace_root) / "worker.log"
    logging.basicConfig(
        filename=str(log_file),
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )


def extract_recent_events(transcript_file: Path) -> list[dict]:
    """Reads JSONL transcript records up to byte cap."""
    if not transcript_file.exists():
        return []

    events = []
    total_bytes = 0

    try:
        with open(transcript_file, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                    events.append(record)
                    total_bytes += len(line)
                    if total_bytes >= CAPTURE_MAX_WINDOW_BYTES:
                        break
                except json.JSONDecodeError:
                    continue
    except Exception as e:
        logging.error(f"Error reading transcript: {e}")

    return events


def analyze_transcript_for_lessons(events: list[dict]) -> list[dict]:
    """Heuristic and pattern extractor for user corrections and durable lessons.
    In production environments, this can invoke a Flash/Haiku subagent prompt.
    """
    intents = []
    
    for ev in events:
        # Check user inputs for correction cues
        user_content = ""
        if ev.get("source") == "USER_EXPLICIT" or ev.get("type") == "USER_INPUT":
            user_content = str(ev.get("content", ""))

        if user_content and friction_detector.detect_correction_in_text(user_content):
            sanitized = redact.redact_text(user_content)
            logging.info(f"Detected user correction pattern: {sanitized[:60]}...")
            
            # Formulate an automated rule intent
            rule_slug = f"learned-rule-{abs(hash(sanitized)) % 10000}"
            clean_rule_desc = f"Quy tắc rút ra từ phản hồi: {sanitized[:50]}"
            rule_body = (
                f"---\n"
                f"name: {rule_slug}\n"
                f"description: \"Use when applying guideline: {clean_rule_desc}\"\n"
                f"trigger: model_decision\n"
                f"---\n\n"
                f"## Guideline\n"
                f"- Tuân thủ chỉ dẫn của người dùng: {sanitized}\n"
            )
            intents.append({
                "action": "create",
                "tier": "rule",
                "name": rule_slug,
                "content": rule_body,
                "reason": f"Phát hiện phản hồi uốn nắn từ user: {sanitized[:60]}",
            })

    return intents


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--transcript", default=None)
    args = parser.parse_args()

    workspace_root = Path(args.workspace)
    setup_logger(workspace_root)
    logging.info("Starting AutoHarness background reflection pass...")

    events = []
    if args.transcript:
        transcript_path = Path(args.transcript)
        events = extract_recent_events(transcript_path)

    if not events:
        logging.info("No transcript events found to process.")
        return

    logging.info(f"Loaded {len(events)} events from transcript.")
    intents = analyze_transcript_for_lessons(events)

    if not intents:
        logging.info("No distinct new lessons to stage this pass.")
        return

    for intent in intents:
        result = admission_promoter.land_intent(intent, workspace_root)
        logging.info(f"Admission result for {intent['name']}: {result}")

    # Perform periodic lifecycle check on mature skills
    admission_promoter.perform_lifecycle_pass(workspace_root)
    logging.info("Background reflection and lifecycle pass completed.")


if __name__ == "__main__":
    main()
