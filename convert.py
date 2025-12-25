import subprocess

# 入力ファイル名と出力ファイル名を指定
input_file = "./116.mov"  # 変換したいMOVファイル名
output_file = "./116.mp4" # 出力したいMP4ファイル名

# FFmpegのコマンド
# -i: 入力ファイル
# -vcodec libx264: ビデオコーデックにH.264を指定
# -acodec aac: オーディオコーデックにAACを指定
command = [
    "ffmpeg",
    "-i", input_file,
    "-vcodec", "libx264",
    "-acodec", "aac",
    # ここに'-strict -2'を追加します
    "-strict", "-2", 
    output_file
]

try:
    # コマンドを実行
    subprocess.run(command, check=True)
    
    print(f"✅ 変換が完了しました: {output_file}")

except subprocess.CalledProcessError as e:
    print(f"❌ FFmpegの実行中にエラーが発生しました: {e}")
except FileNotFoundError:
    print("❌ エラー: FFmpegがシステムに見つかりません。FFmpegがインストールされているか、パスが正しく設定されているか確認してください。")