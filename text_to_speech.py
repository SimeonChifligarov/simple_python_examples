import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    print('🔊 Text to Speech (offline)')
    text = input('Въведи текст за прочитане: ')
    speak(text)
