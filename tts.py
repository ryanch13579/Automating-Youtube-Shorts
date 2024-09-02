import elevenlabs
from moviepy.editor import VideoFileClip

#api key
elevenlabs.set_api_key("a5e1464b8ddccbb5ef563bd0cf3edf67")

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