from moviepy.editor \
    import VideoFileClip, concatenate_videoclips, vfx, CompositeVideoClip, CompositeAudioClip, AudioFileClip, ImageClip
import os

os.chdir('test_media')

gc_file_name = 'png.png'
audio_file_name = 'song.mp3'
clip_file_name = 'video.mkv'

gc = ImageClip(gc_file_name)\
    .set_pos(("center", "center")).subclip()
audio = AudioFileClip(audio_file_name).subclip()
clip = VideoFileClip(clip_file_name).subclip(4, 9)

min_length = min(audio.duration, clip.duration)
gc = gc.subclip(0, min_length).resize(height=clip.h)
audio = audio.subclip(0, min_length)
clip = clip.subclip(0, min_length)


comp_audio = CompositeAudioClip([clip.audio, audio])
clip.audio = comp_audio

final_clip = CompositeVideoClip([clip, gc])\
    .set_duration(min_length)

os.chdir('..')
os.chdir('test_movies')

final_clip.write_videofile('movie.mp4')