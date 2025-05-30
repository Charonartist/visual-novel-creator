# Visual Novel Creator Tool

🎮 **ADVゲーム風紙芝居作成ツール**

ビジュアルノベル風のシーンを作成・管理できるWebアプリケーション。背景画像とテキストを組み合わせてゲーム風の画像を生成できます。

## ✨ 主な機能

- **背景画像管理**: 画像をアップロードして背景として使用
- **テキスト設定**: キャラクター名、セリフ、フォントサイズ・色の詳細設定
- **ウィンドウスタイル**: スタンダード、ファンタジー、サイバーの3種類のテーマ
- **位置調整**: ウィンドウやテキストの細かい位置調整機能
- **シーン管理**: 複数シーンの作成・管理・並び替え（ドラッグ&ドロップ対応）
- **画像出力**: 単体/全シーンの画像保存（PNG、ZIP一括出力）
- **データ管理**: CSVでのインポート/エクスポート機能

## 🚀 クイックスタート

### 1. 環境構築

```bash
# リポジトリのクローン
git clone https://github.com/Charonartist/visual-novel-creator.git
cd visual-novel-creator

# 依存関係のインストール
pip install -r requirements.txt
```

### 2. サーバー起動

```bash
python app.py
```

ブラウザで `http://localhost:5000` にアクセスしてください。

## 📁 ファイル構成

```
visual-novel-creator/
├── app.py                    # Flaskサーバー（プロキシ機能付き）
├── requirements.txt          # Python依存関係
├── index.html               # メインのWebアプリケーション
├── static/
│   ├── sample_scenario_corrected.csv  # サンプルシナリオファイル
│   └── windows/
│       └── standard_window.png        # ウィンドウ画像
└── README.md                # このファイル
```

## 🎯 使い方

### 基本的な流れ

1. **背景画像をアップロード**: 左パネルから画像ファイルを選択
2. **テキスト設定**: キャラクター名とセリフを入力
3. **スタイル調整**: ウィンドウスタイル、フォント、位置を設定
4. **画像として保存**: 作成したシーンを画像として出力

### 高度な機能

- **シーン管理**: 右パネルでシーンの切り替え・削除・並び替え
- **位置微調整**: 矢印ボタンでウィンドウとテキストの位置を細かく調整
- **一括設定**: 現在の設定を他の全シーンに適用
- **CSV管理**: シナリオデータのインポート/エクスポート

## 🎨 ウィンドウスタイル

- **スタンダード**: シンプルな黒背景
- **ファンタジー**: 金色の装飾枠付き
- **サイバー**: 水色のネオン風

## 📊 CSVフォーマット

サンプルCSVファイル（`static/sample_scenario_corrected.csv`）を参考にしてください：

```csv
scene,character,character_color,dialog,font_size,font_color
opening,ナレーター,#FFFFFF,～とある学園の放課後～,24px,#FFFFFF
opening,主人公 太郎,#FF6B6B,（今日も一日が終わった……）,16px,#FFFFFF
```

## 🛠️ 技術仕様

- **フロントエンド**: HTML5, CSS3, JavaScript
- **バックエンド**: Python Flask
- **画像処理**: HTML5 Canvas, html2canvas
- **ファイル出力**: JSZip（ZIP生成）

## 📝 ライセンス

MITライセンスの下で公開されています。

## 🙏 謝辞

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>