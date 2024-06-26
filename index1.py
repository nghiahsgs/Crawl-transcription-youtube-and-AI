from pytube import YouTube

# Tải phụ đề từ video YouTube
yt = YouTube('https://www.youtube.com/watch?v=yonoGi64ND8')

yt.title
yt.thumbnail_url


# captions = yt.captions.get_by_language_code('jp')  # Mã ngôn ngữ của phụ đề
# yt.captions
captions = yt.captions.get_by_language_code('vi')  # Mã ngôn ngữ của phụ đề

# Lưu phụ đề vào file
with open('subtitles.srt', 'w') as f:
    f.write(captions.generate_srt_captions())
