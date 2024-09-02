from faster_whisper import WhisperModel

#add subtitles to videos
model_size = "medium"
model = WhisperModel(model_size)

segments, info = model.transcribe("final_audio.mp3", word_timestamps=True)
segments = list(segments)

subtitles = []

for segment in segments:
    for word in segment.words:
        #format timecodes for SRT file
        start_time = "{:.3f}".format(word.start)
        end_time = "{:.3f}".format(word.end)

        subtitles.append({
            'word':word.word.upper(),
            'start':start_time,
            'end': end_time
        })

 # Write subtitles to an SRT file
    with open("sub.srt", 'w', encoding='utf-8') as srt_file:
        index = 1
        for subtitle in subtitles:
            srt_file.write("{}\n".format(index))
            srt_file.write("{} --> {}\n".format(subtitle['start'], subtitle['end']))
            srt_file.write("{}\n\n".format(subtitle['word']))
            index += 1
