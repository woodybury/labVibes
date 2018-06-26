import pyaudio
import os
import listening
# import simpleaudio as sa
import speech_recognition as sr

# searchsound = sa.WaveObject.from_wave_file('sound/search.wav')
index = pyaudio.PyAudio().get_device_count() - 1

print (index)

r = sr.Recognizer()
mic = sr.Microphone(1)


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
        print ('error')
    except sr.UnknownValueError:
        response["error"] = "unknown"
        print ('unknown')

    if response['text']:

        phrase = response['text'].replace(" ", "_")
        print ('phrase: ' + phrase)
    else:
        print('idk')

    audio.stop_stream()

if __name__ == "__main__":
    while (1):
        print ('listening for keyword projector')
        listening.recognition(recognize_search, 'projector', False)
