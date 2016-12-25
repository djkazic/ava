import requests
import hashlib
import os
import simpleaudio as sa


class Audio:
    """Processes text to speech"""

    @staticmethod
    def read(text):
        sha1 = hashlib.sha1(str(text).encode('utf-8')).hexdigest()
        print("SHA1 = " + sha1)
        folder = "./cache"
        filename = folder + "/" + sha1 + ".wav"
        if not os.path.exists(folder):
            os.mkdir(folder)
        try:
            file = open(filename, 'r')
        except FileNotFoundError:
            file = open(filename, 'wb')
            data = requests.get("http://api.voicerss.org" + "?key="
                                + os.environ['VOICERSS_API']
                                + "&src=" + text.replace(" ", "%20")
                                + "&hl=en-gb"
                                + "&f=24khz_16bit_stereo"
                                + "&c=WAV", stream=True)
            for chunk in data.iter_content(1024):
                if chunk:
                    file.write(chunk)
            file.close()

        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()