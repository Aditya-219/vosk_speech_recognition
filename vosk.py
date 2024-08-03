from vosk import Model, KaldiRecognizer
import pyaudio

# Load your existing chatbot routes and functions here

model = Model("./vosk/vosk-model-small-hi-0.22")
recognizer = KaldiRecognizer(model, 16000)
#vosk-model-small-hi-0.22
#use this for hindi model with path directory

#here is the rate of audio input
mic = pyaudio.PyAudio()
stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16,
                  input=True, frames_per_buffer=8192)
stream.start_stream()

#loop to print the word
while True:
    data = stream.read(4096)

    if recognizer.AcceptWaveform(data):
        print(recognizer.Result()[14:-3])
