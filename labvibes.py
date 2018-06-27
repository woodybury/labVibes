import pyaudio
import os
import listening
# import simpleaudio as sa
import speech_recognition as sr

# searchsound = sa.WaveObject.from_wave_file('sound/search.wav')
index = pyaudio.PyAudio().get_device_count() - 1

print (index)

r = sr.Recognizer()

if os.uname()[1] == 'raspberrypi':
    mic = sr.Microphone(1)
else:
    mic = sr.Microphone()


def recognize_search():
    # playsound = searchsound.play()
    # playsound.wait_done()
    print ('listening for phrase')
    with mic as source:
        audio = r.listen(source)
    response = {
        "success": True,
        "error": None,
        "text": None
    }
    try:
        response["text"] = r.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "unavailable"
    except sr.UnknownValueError:
        response["error"] = "unknown"

    if response['text']:

        phrase = response['text'].replace(" ", "_")
        print ('phrase: ' + phrase)

if __name__ == "__main__":
    while (1):
        print ('listening for keyword projector')
        listening.recognition(recognize_search, 'projector')