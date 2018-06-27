import os
from pocketsphinx import pocketsphinx
from sphinxbase.sphinxbase import *
import pyaudio

# continue listening with sphinx
def recognition(keyphrase_function, key_phrase):

    # Start a pyaudio instance
    p = pyaudio.PyAudio()
    # Create an input stream with pyaudio - if on raspi use index 1 for google voice hat mic
    if os.uname()[1] == 'raspberrypi':
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, input_device_index=1, frames_per_buffer=1024)
        print('stream started on rpi')
    else:
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
        print ('stream started')

    # Start the stream
    stream.start_stream()

    modeldir = "data/files/sphinx/models"

    # Create a decoder with certain model
    config = pocketsphinx.Decoder.default_config()
    # Use the mobile voice model (en-us-ptm) for performance constrained systems
    if os.uname()[1] == 'raspberrypi':
        config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us-ptm'))
    else:
        config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us'))

    config.set_string('-dict', os.path.join(modeldir, 'en-us/cmudict-en-us.dict'))
    config.set_string('-keyphrase', key_phrase)
    config.set_string('-logfn', 'data/files/sphinx.log')
    config.set_float('-kws_threshold', 1)

    # Process audio chunk by chunk. On keyword detected perform action and restart search
    decoder = pocketsphinx.Decoder(config)
    decoder.start_utt()
    # Loop forever
    while True:
        # Read 1024 samples from the buffer
        buf = stream.read(1024, exception_on_overflow = False)
        # If data in the buffer, process using the sphinx decoder
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break
        # If the hypothesis is not none, the key phrase was recognized
        if decoder.hyp() is not None:
            decoder.end_utt()
            stream.stop_stream()    # Stop Audio Recording
            stream.close()          # Close Audio Recording
            keyphrase_function()    # Call back

            return True