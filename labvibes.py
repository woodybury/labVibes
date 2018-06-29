import os
import time
# import cv2
import webbrowser
# import threading
import listening
import nlp
# import simpleaudio as sa
import speech_recognition as sr

if os.uname()[1] == 'raspberrypi':
    raspi = True
else:
    raspi = False

# searchsound = sa.WaveObject.from_wave_file('sound/search.wav')

r = sr.Recognizer()

if raspi:
    mic = sr.Microphone(1)
else:
    mic = sr.Microphone()

path =  os.getcwd()

def recognize_phrase():
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
        phrase = response['text']
        print ('phrase is: ' + phrase)

        # nlp
        video = nlp.similarity(phrase)

        # play returned video
        video_file = 'file://' + path + '/videos/' + video

        playvideo(video_file)

        # t = threading.Thread(target=playvideo, args = (video_file,))
        # t.daemon = True
        # t.start()

def playvideo(video_file):
    if raspi:
        # os.system('pkill chromium-browser')
        # video_cmd = 'chromium-browser --app=' + video_file + ' &'
        os.system('pkill omxplayer')
        video_cmd = 'omxplayer --loop ' + video_file + ' &'
        os.system(video_cmd)
        time.sleep(1)
    else:
        webbrowser.open(video_file)

    # Open CV imshow is throwing error when called not on the main thread. Trying omxplayer and chromium instead
    # cap = cv2.VideoCapture(video_file)
    #
    # while(cap.isOpened()):
    #     ret, frame = cap.read()
    #
    #     cv2.imshow('Lab Vibes',frame)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    #
    # cap.release()
    # cv2.destroyAllWindows()

if __name__ == "__main__":

    while (1):
        print ('listening for keyword projector')
        listening.recognition(recognize_phrase, 'projector')
