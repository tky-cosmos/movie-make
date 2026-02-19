from __future__ import annotations

from pathlib import Path

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def load_photos(input_dir: Path) -> list[Path]:
    """Return photo paths sorted by modified time and filename."""
    if not input_dir.exists() or not input_dir.is_dir():
        raise FileNotFoundError(f"写真フォルダが見つかりません: {input_dir}")

    photos = [
        path
        for path in input_dir.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    if not photos:
        raise ValueError(
            f"画像ファイルが見つかりませんでした ({', '.join(sorted(SUPPORTED_EXTENSIONS))}): {input_dir}"
        )

    photos.sort(key=lambda p: (p.stat().st_mtime, p.name.lower()))
    return photos
