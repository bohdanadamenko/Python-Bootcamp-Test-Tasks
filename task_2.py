import os
from moviepy.editor import VideoFileClip
from TikTokApi import TikTokApi  # for work this package need install python -m playwright install


tik_tok_url = input('Enter TikTok URL: ')  # url for example: https://www.tiktok.com/@therock/video/6829267836783971589


def tt_video_to_gif(link):
    # Downloading .mp4 file from TikTok
    with TikTokApi() as api:
        video = api.video(url=link)
        video_data = video.bytes()
        video_id = video.id
    with open(f'video_{video_id}.mp4', 'wb') as out_file:
        out_file.write(video_data)
    # Convert .mp4 to .gif
    clip = (VideoFileClip(f'video_{video_id}.mp4'))
    clip.write_gif(f'output_{video_id}.gif')
    file_path = os.path.abspath(f'output_{video_id}.gif')
    return f'GIF created. Path: {file_path}'


print(tt_video_to_gif(tik_tok_url))
