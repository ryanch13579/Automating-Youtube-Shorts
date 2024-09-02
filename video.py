import math
import random
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips

#combine the 2 clips together
input_audio1 = AudioFileClip("didyouknow.mp3")
input_audio2 = AudioFileClip("audio.mp3")

final_audio = concatenate_audioclips([input_audio1,input_audio2])
final_audio = final_audio.write_audiofile("final_audio.mp3")

#find duration of the audio clip
duration = AudioFileClip("final_audio.mp3").duration
duration = math.ceil(duration)

print(f"The duration of the audio file is {duration:.2f} seconds.")

#create visuals
clip = VideoFileClip("video.mp4")

#find duration of the video
vid_duration = clip.duration
vid_duration = math.floor(vid_duration)
print(f"The duration of the video file is {vid_duration:.2f} seconds.")


#pick a random point in the video
random_time = random.uniform(5, vid_duration-5)
random_time = math.floor(random_time)
print(f"The randomly selected point is at {random_time:.2f} seconds.")

#cut the video at that point which satisfy the audio file
final_clip = clip.subclip(random_time, random_time + duration)
final_clip = final_clip.without_audio()
final_clip = final_clip.write_videofile("output.mp4", fps = 60)
