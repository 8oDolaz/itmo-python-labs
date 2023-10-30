import os

import config
from dog_api import DogAPI
from speech_utils import load_model, listen, text_to_speech

import cv2
import pyttsx3
from vosk import KaldiRecognizer
from pyaudio import PyAudio, paInt16


def main():
    listener = PyAudio()
    stream = listener.open(
        format=paInt16,
        channels=1,
        rate=16_000,
        input=True,
        frames_per_buffer=8_000
    )
    stream.start_stream()

    model = load_model(config.model_dir)
    speech_recognizer = KaldiRecognizer(model, 16_000)

    tts_engine = pyttsx3.init('espeak')
    tts_engine.setProperty('voice', config.voice)

    dog = DogAPI()
    dog.next()

    text_to_speech(tts_engine, 'Starting')
    for command in listen(stream, speech_recognizer):
        match command:
            case [*_, 'покажи']:
                dog.save_image(background=True)

                background = cv2.imread(config.background_path)
                cv2.imshow(f'{dog.breed.capitalize()}', background)
                cv2.waitKey(10_000)
                cv2.destroyAllWindows()

                os.remove(config.background_path)
            case [*_, 'сохранить']:
                dog.save_image()

                text_to_speech(tts_engine, 'Saved')
            case [*_, 'дальше']:
                dog.next()

                text_to_speech(tts_engine, 'Next one')
            case [*_, 'назови', 'породу']:
                text_to_speech(tts_engine, f'{dog.breed}')
            case [*_, 'закончить']:
                text_to_speech(tts_engine, 'Goodbye!')
                break

if __name__ == '__main__':
    main()
