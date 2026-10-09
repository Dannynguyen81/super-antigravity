"""Empirical lifecycle manager for Antigravity skills.
Determines which skills stay active, graduate probation, or get archived based on empirical call-rate.
"""
from typing import Any


def calculate_call_rate(calls: int, requests: int) -> float:
    """Calculates empirical call rate (calls per request)."""
    return calls / requests if requests > 0 else 0.0


def evaluate_lifecycle(
    managed_skills: list[dict[str, Any]],
    current_request_count: int,
    maturity_threshold: int,
    capacity_limit: int,
) -> list[str]:
    """Evaluates skills and returns a list of skill names to be safely archived.
    
    managed_skills item format:
    {
        "name": str,
        "created_at_request": int,
        "call_count": int
    }
    """
    to_archive: list[str] = []
    mature_pool: list[tuple[float, str]] = []

    for item in managed_skills:
        name = item["name"]
        created_at = item.get("created_at_request", 0)
        calls = item.get("call_count", 0)
        requests_active = max(1, current_request_count - created_at)

        # 1. Check Probation
        if requests_active < maturity_threshold:
            # Still in probation period, protected from eviction
            continue

        # 2. Graduation Review
        if calls == 0:
            # Full probation completed with zero calls -> genuine dormancy
            to_archive.append(name)
            continue

        # Qualified graduate -> enters mature pool
        rate = calculate_call_rate(calls, requests_active)
        mature_pool.append((rate, name))

    # 3. Capacity Contention
    # If the mature pool exceeds capacity, archive lowest by ascending rate
    if len(mature_pool) > capacity_limit:
        mature_pool.sort(key=lambda x: x[0])  # ascending rate
        excess_count = len(mature_pool) - capacity_limit
        for i in range(excess_count):
            to_archive.append(mature_pool[i][1])

    return to_archive
