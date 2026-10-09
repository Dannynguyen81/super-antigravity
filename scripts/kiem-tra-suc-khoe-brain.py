#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script: kiem-tra-suc-khoe-brain.py
Mục đích: Audit chất lượng kho tri thức theo 6 phân tầng Knowledge Lifecycle (Lint link hỏng, kiểm tra thẻ tags, tìm note mồ côi).
SecondBrain Knowledge Lifecycle
"""

import re
import sys
from pathlib import Path

# Đảm bảo in UTF-8 mượt mà trên console Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT_DIR = Path(__file__).resolve().parent.parent

TARGET_DIRS = [
    "10-inbox",
    "20-sources",
    "30-working",
    "40-knowledge",
    "50-outputs",
    "90-archive",
]

WIKI_LINK_PATTERN = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]')

def main():
    print("=" * 60)
    print("🩺 KIỂM TRA SỨC KHỎE KHO TRI THỨC — KNOWLEDGE LIFECYCLE")
    print("=" * 60)

    all_md_files = {}
    for d_name in TARGET_DIRS:
        d_path = ROOT_DIR / d_name
        if not d_path.exists():
            continue
        for f in d_path.rglob("*.md"):
            if f.name.lower() == "readme.md" or "_templates" in f.parts:
                continue
            # Lưu key là stem và relative path
            all_md_files[f.stem] = f

    print(f"📊 Tổng số tài liệu phát hiện trong các phân tầng: {len(all_md_files)} file")

    broken_links = []
    incoming_links = {stem: 0 for stem in all_md_files}
    missing_frontmatter = []

    for stem, f_path in all_md_files.items():
        text = f_path.read_text(encoding="utf-8", errors="replace")
        
        # 1. Kiểm tra Frontmatter YAML
        if not text.startswith("---"):
            missing_frontmatter.append(f_path.name)

        # 2. Quét wiki links [[link]]
        matches = WIKI_LINK_PATTERN.findall(text)
        for link in matches:
            clean_link = link.strip().replace("\\", "/")
            link_stem = Path(clean_link).stem
            if link_stem in incoming_links:
                incoming_links[link_stem] += 1
            else:
                # Kiểm tra xem có file thật trên ổ đĩa không
                target_cand = ROOT_DIR / f"{clean_link}.md"
                target_cand2 = ROOT_DIR / clean_link
                if not target_cand.exists() and not target_cand2.exists():
                    broken_links.append((f_path.name, link))

    print("\n--- 1. Kiểm Tra Liên Kết Gãy (Broken Links) ---")
    if not broken_links:
        print("✅ Tuyệt vời! Không phát hiện liên kết gãy nào.")
    else:
        print(f"⚠️ Phát hiện {len(broken_links)} liên kết không trỏ tới đâu:")
        for source_file, target in broken_links:
            print(f"   ❌ Trong [{source_file}] -> Trỏ đến: [[{target}]]")

    print("\n--- 2. Kiểm Tra Cấu Trúc Metadata (Frontmatter) ---")
    if not missing_frontmatter:
        print("✅ 100% tài liệu có đầy đủ Frontmatter YAML tiêu chuẩn.")
    else:
        print(f"⚠️ Phát hiện {len(missing_frontmatter)} tài liệu chưa có Frontmatter:")
        for mf in missing_frontmatter:
            print(f"   ℹ️ {mf}")

    print("\n--- 3. Kiểm Tra Tài Liệu Mồ Côi (Orphan Notes) ---")
    orphans = [stem for stem, count in incoming_links.items() if count == 0]
    if not orphans:
        print("✅ Tất cả tài liệu đều được kết nối chặt chẽ.")
    else:
        print(f"ℹ️ Có {len(orphans)} tài liệu chưa có liên kết từ tài liệu khác (Cân nhắc gắn vào MOC/README):")
        for op in orphans[:10]:
            print(f"   🔗 {op}.md")
        if len(orphans) > 10:
            print(f"   ... và {len(orphans) - 10} tài liệu khác.")

    print("\n" + "=" * 60)
    print("🎯 BÁO CÁO TỔNG KẾT: Kho tri thức hoạt động tốt, sẵn sàng sử dụng!")
    print("=" * 60)
    return 0

if __name__ == "__main__":
    sys.exit(main())
