from main.audio import Audio
import os


def main():
    print("Hello world!")
    print(os.environ)
    audio = Audio()
    audio.read("TTS test")

if __name__ == "__main__":
    main()
