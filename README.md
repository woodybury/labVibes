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

`sudo pip3 install -U spacy`

For the raspberry pi there is not enought memory to make spacy. Follow these steps to update swap file size, boot options, and memory split:

#### Increase swap file size

`sudo nano /etc/dphys-swapfile`

change `CONF_SWAPSIZE=100` to `CONF_SWAPSIZE=1024`

`sudo /etc/init.d/dphys-swapfile stop` and `sudo /etc/init.d/dphys-swapfile start`

#### Change boot options

`sudo raspi-config` choose the console option via Boot Options => Desktop / CLI => Console Autologin

#### Update memory split

`sudo raspi-config` choose advanced Options => Memory Split and set to 16

DON'T FORGET TO UNDO THESE STEPS AFTER INSTALL => large swap sizes corrupt memory cards :) and we need the GPU for the videos later.

Download the english model

`sudo python3 -m spacy download en`