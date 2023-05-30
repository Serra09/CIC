import whisper
import os

model = whisper.load_model("small")
result = model.transcribe(os.getcwd() + '/Documents/CIC/postfiltered1704Javi.wav')

print(result["text"])