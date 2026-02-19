from __future__ import annotations

import argparse
from pathlib import Path

from movie_make.basic_slideshow import build_basic_slideshow
from movie_make.photo_loader import load_photos


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="指定フォルダ内の写真からシンプルな成長ムービーを作成します。"
    )
    parser.add_argument(
        "--input-dir",
        required=True,
        help="写真フォルダのパス",
    )
    parser.add_argument(
        "--output",
        help="出力mp4のパス。未指定時は input-dir/growth_movie.mp4",
    )
    parser.add_argument(
        "--seconds-per-photo",
        type=float,
        default=3.0,
        help="1枚あたりの表示秒数 (デフォルト: 3.0)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_dir = Path(args.input_dir).expanduser().resolve()
    output_path = (
        Path(args.output).expanduser().resolve()
        if args.output
        else input_dir / "growth_movie.mp4"
    )

    if args.seconds_per_photo <= 0:
        print("エラー: --seconds-per-photo は0より大きい値を指定してください")
        return 1

    try:
        photos = load_photos(input_dir)
        build_basic_slideshow(
            photos=photos,
            output_path=output_path,
            seconds_per_photo=args.seconds_per_photo,
        )
    except (FileNotFoundError, ValueError, EnvironmentError, RuntimeError) as e:
        print(f"エラー: {e}")
        return 1

    print(f"完了: 動画を作成しました -> {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
