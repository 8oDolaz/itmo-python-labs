import os
import json

import vosk


def load_model(path):
    if not os.path.exists(path):
        raise Exception('No such model found in directory. Please download one from https://alphacephei.com/vosk/models and unpack in current folder')

    return vosk.Model(path)

def speech_to_text(data_wav, recognizer):
    if recognizer.AcceptWaveform(data_wav):
        text = json.loads(recognizer.Result())
        text = text.get('text')

        return text
    
def text_to_speech(engine, text):
    engine.say(text)
    engine.runAndWait()

def listen(stream, recognizer):
    while True:
        speech = stream.read(4000, exception_on_overflow=False)

        if len(speech) > 0:
            text = speech_to_text(speech, recognizer)
            if not text is None:
                yield text.split()
