import elevenlabs
from moviepy.editor import VideoFileClip

#api key
elevenlabs.set_api_key("my_dumb_api_key")

#user input text
text = input("Text input:")

#create tts 
audio = elevenlabs.generate(
    text=text,
    voice = "Freya"
)

elevenlabs.save(audio, "audio.mp3")

#create visuals
clip = VideoFileClip("video.mp4")