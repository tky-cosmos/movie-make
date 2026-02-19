# movie-make

子どもの写真フォルダから成長ムービーを作るためのプロジェクトです。

## Step 1: 最小機能（CLI）

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

1枚あたりの表示秒数を変える場合:

```bash
python -m movie_make.cli --input-dir /path/to/photos --seconds-per-photo 2.5
```

### 現在の仕様（Step 1）

- 写真フォルダを指定して動画を作成
- フォルダが存在しない場合はエラー表示
- 対象画像が0件の場合はエラー表示
- エフェクト・テロップ・BGM なし（今後追加予定）

## 初心者向け: 次にやること（少しずつ進める）

はい、**Step 1 の次は PR 作成でOK**です。  
大きく進めすぎず、以下の順番で進めるのがおすすめです。

1. Step 1 が動くことを確認（最低限: `--help` とエラーケース）
2. PR を作成（何を追加したかを短く書く）
3. レビューで改善点を反映
4. 次の小さな機能（Step 2: 動画全体の長さ指定）に進む

### PR本文の最小テンプレ

- 目的: 何を実現したか（1〜2行）
- 変更点: 追加/修正したファイルと要点
- 確認方法: 実行したコマンド
- 制約: この環境でできなかった確認（例: ffmpeg未導入）

このプロジェクトでは、今後も「1機能ずつ小さくPR」を基本方針にします。
