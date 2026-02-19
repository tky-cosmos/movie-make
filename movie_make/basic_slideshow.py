from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory


def build_basic_slideshow(
    photos: list[Path], output_path: Path, seconds_per_photo: float = 3.0
) -> Path:
    """Build a simple slideshow video from photos using ffmpeg concat."""
    if not photos:
        raise ValueError("画像が0件のため動画を作成できません")

    ffmpeg_path = shutil.which("ffmpeg")
    if not ffmpeg_path:
        raise EnvironmentError(
            "ffmpeg が見つかりません。ffmpeg をインストールしてから再実行してください。"
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with TemporaryDirectory() as temp_dir:
        concat_file = Path(temp_dir) / "concat.txt"
        escaped_paths = [str(photo).replace("'", "'\\''") for photo in photos]

        with concat_file.open("w", encoding="utf-8") as f:
            for path in escaped_paths:
                f.write(f"file '{path}'\n")
                f.write(f"duration {seconds_per_photo:.3f}\n")
            f.write(f"file '{escaped_paths[-1]}'\n")

        command = [
            ffmpeg_path,
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_file),
            "-vf",
            "fps=30,format=yuv420p",
            "-movflags",
            "+faststart",
            str(output_path),
        ]

        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(
                "動画の作成に失敗しました。\n"
                f"ffmpeg stderr:\n{result.stderr.strip()}"
            )

    return output_path
