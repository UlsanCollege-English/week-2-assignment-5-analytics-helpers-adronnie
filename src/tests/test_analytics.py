from typing import List, Optional

def chunk(values: List[int], size: int) -> List[List[int]]:
    """Split values into sublists of length `size`. Last chunk may be shorter.
    Raise ValueError if size <= 0.
    """
    if size <= 0:
        raise ValueError("size must be positive")
    result = []
    for i in range(0, len(values), size):
        result.append(values[i:i+size])
    return result


def running_total(start: int, changes: List[int]) -> List[int]:
    """Return list of totals starting from `start` after applying each change."""
    totals = []
    current = start
    for change in changes:
        current += change
        totals.append(current)
    return totals


def index_of_first_at_least(values: List[int], threshold: int) -> Optional[int]:
    """Return the index of the first element >= threshold, or None if not found."""
    for i, v in enumerate(values):
        if v >= threshold:
            return i
    return None
