import whisper
import os

model = whisper.load_model("small")
result = model.transcribe(os.getcwd() + '/Documents/CIC/Whisper/postfilteredJavi.wav')

print(result["text"])