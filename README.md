# movie-make

子どもの写真フォルダから成長ムービーを作るためのプロジェクトです。

## Step 1-3: 最小機能（CLI）

指定フォルダ内の画像（`.jpg` / `.jpeg` / `.png`）を読み込み、
シンプルなスライドショー動画（mp4）を生成します。

### 必要条件

- Python 3.10+
- `ffmpeg` がインストールされ、PATH に通っていること

### 実行例

```bash
python -m movie_make.cli --input-dir /path/to/photos
```

- 出力先未指定時: `/path/to/photos/growth_movie.mp4`

出力先を指定する場合:

```bash
python -m movie_make.cli --input-dir /path/to/photos --output /path/to/photos/my_movie.mp4
```

1枚あたりの表示秒数を固定で指定する場合:

```bash
python -m movie_make.cli --input-dir /path/to/photos --seconds-per-photo 2.5
```

動画全体の長さ（秒）を指定して自動調整する場合（Step 2）:

```bash
python -m movie_make.cli --input-dir /path/to/photos --duration-sec 60
```

BGMファイルを先に指定しておく場合（Step 3の最小版: まだ合成はしない）:

```bash
python -m movie_make.cli --input-dir /path/to/photos --bgm /path/to/bgm.mp3 --bgm-volume 0.8
```

### 現在の仕様（Step 3まで）

- 写真フォルダを指定して動画を作成
- フォルダが存在しない場合はエラー表示
- 対象画像が0件の場合はエラー表示
- `--duration-sec` 指定時は、写真枚数から1枚あたり秒数を自動計算
- `--duration-sec` と `--seconds-per-photo` を同時指定した場合は `--duration-sec` を優先
- `--bgm` はファイル存在チェックのみ実施（まだ音声合成は未実装）
- `--bgm-volume` は 0.0〜1.0 の範囲チェックのみ実施
- エフェクト・テロップは未対応（今後追加予定）
