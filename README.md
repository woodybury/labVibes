# Lab Vibes for the projector

## Add videos

Put video fies in `/videos`
Add video name, file name, and description to the videos dictionary in `nlp.py`

## Dev

### Setup pocketsphix and speech recognition

Using CMU's pocketphix for keyword listening (see listening.py): https://github.com/cmusphinx/pocketsphinx-python

`sudo pip3 install pocketsphinx`

And using the speech recognition library for the google speech api after keyword: https://github.com/Uberi/speech_recognition#readme

`sudo pip3 install SpeechRecognition`

### Setup spaCy NLP

Using spaCy for speech phrase vs. video description similarity: https://github.com/explosion/spaCy

`sudo pip3 install spacy`

Download the english model

`sudo python3 -m spacy download en`
