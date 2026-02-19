from __future__ import annotations

import argparse
from pathlib import Path

from movie_make.basic_slideshow import build_basic_slideshow
from movie_make.photo_loader import load_photos
from movie_make.timing import calculate_seconds_per_photo


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
    parser.add_argument(
        "--duration-sec",
        type=float,
        help="動画全体の長さ（秒）。指定時は写真枚数から1枚あたり秒数を自動計算",
    )
    parser.add_argument(
        "--bgm",
        help="BGMファイルのパス（現時点では存在確認のみ）",
    )
    parser.add_argument(
        "--bgm-volume",
        type=float,
        default=1.0,
        help="BGM音量（0.0〜1.0、現時点では入力確認のみ）",
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

    if args.duration_sec is not None and args.duration_sec <= 0:
        print("エラー: --duration-sec は0より大きい値を指定してください")
        return 1

    if args.bgm_volume < 0 or args.bgm_volume > 1:
        print("エラー: --bgm-volume は 0.0〜1.0 の範囲で指定してください")
        return 1

    bgm_path: Path | None = None
    if args.bgm:
        bgm_path = Path(args.bgm).expanduser().resolve()
        if not bgm_path.exists() or not bgm_path.is_file():
            print(f"エラー: BGMファイルが見つかりません: {bgm_path}")
            return 1
        print("情報: BGM指定を受け付けました（音声合成は次ステップで対応予定）")

    try:
        photos = load_photos(input_dir)

        seconds_per_photo = args.seconds_per_photo
        if args.duration_sec is not None:
            seconds_per_photo = calculate_seconds_per_photo(
                photo_count=len(photos), duration_sec=args.duration_sec
            )
            print(
                "情報: --duration-sec が指定されたため、"
                f"1枚あたり {seconds_per_photo:.3f} 秒で作成します"
            )

        build_basic_slideshow(
            photos=photos,
            output_path=output_path,
            seconds_per_photo=seconds_per_photo,
        )
    except (FileNotFoundError, ValueError, EnvironmentError, RuntimeError) as e:
        print(f"エラー: {e}")
        return 1

    if bgm_path:
        print("情報: BGM合成は未実装のため、今回は無音動画を出力しました")
    print(f"完了: 動画を作成しました -> {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
