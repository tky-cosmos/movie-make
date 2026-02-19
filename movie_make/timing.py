from __future__ import annotations


def calculate_seconds_per_photo(photo_count: int, duration_sec: float) -> float:
    """Calculate display seconds per photo from total duration."""
    if photo_count <= 0:
        raise ValueError("photo_count は1以上である必要があります")
    if duration_sec <= 0:
        raise ValueError("duration_sec は0より大きい必要があります")

    return duration_sec / photo_count
