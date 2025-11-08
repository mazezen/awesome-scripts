"""
下载 YouTube 视频
获取 Cookie 推荐使用 浏览器插件 CooKie-Editor
install ffmpeg

mac:
brew install ffmpeg
brew link ffmpeg

Linux（Ubuntu/Debian）:
sudo apt-get update && apt-get install ffmpeg
"""

import shutil
import yt_dlp
import os


link = "https://www.youtube.com/watch?v=2lAe1cqCOXo"

COOKIE_PATH = "/Users/bz/coding/awesome-scripts/download/cookie.txt"

if not os.path.exists(COOKIE_PATH):
    print(f"{COOKIE_PATH} does not exist")
    print("请先使用浏览器插件导出 YouTube 的 cookies.txt")
    exit(1)

ffmpeg_path = shutil.which("ffmpeg")
if not ffmpeg_path:
    print("ffmpeg 未找到，请检查安装")
    exit(1)

ydl_opts = {
    'outtmpl': '/Users/bz/coding/awesome-scripts/download/%(title)s.%(ext)s',
    'format': 'bestvideo[height<=720]+bestaudio/best',
    'cookiefile': COOKIE_PATH,
    'retries': 10,
    'fragment_retries': 10,
    'concurrent_fragment_downloads': 5,
    'ffmpeg_location': ffmpeg_path,
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])



