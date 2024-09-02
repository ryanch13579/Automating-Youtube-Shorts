from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip

input_video = "output.mp4"
input_audio = "final_audio.mp3"
input_text = "sub.srt"

# Load video and audio clips
video_clip = VideoFileClip(input_video)
audio_clip = AudioFileClip(input_audio)

# Set audio of the video clip to the loaded audio clip
video_clip = video_clip.set_audio(audio_clip)

# Open srt file
with open(input_text, 'r') as srt_file:
    subtitles = srt_file.read().strip().split('\n\n')

# Create TextClip for each subtitle
text_clips = [
    TextClip(lines[2], fontsize=60, color='white', stroke_color="black", stroke_width= 1, font="Roboto", bg_color="black")
        .set_pos('center')
        .set_duration(float(end) - float(start))
        .set_start(float(start))
    for subtitle in subtitles
    for lines in [subtitle.split('\n')]
    for start, end in [map(lambda x: float(x), lines[1].split(' --> '))]
]

# Composite the video with the subtitles
final_clip = CompositeVideoClip([video_clip] + text_clips)
final_clip = final_clip.crop(x1=300,y1=0,x2=950,y2=1000)


# Write the result to a file
final_clip.write_videofile("success.mp4")
