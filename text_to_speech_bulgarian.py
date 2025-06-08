from gtts import gTTS
import os
import tempfile
import platform


def speak_bulgarian(text):
    tts = gTTS(text=text, lang='bg')

    # Временно .mp3 файлче
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        temp_path = fp.name
        tts.save(temp_path)

    # Пускане в зависимост от операционната система
    if platform.system() == 'Windows':
        os.system(f'start {temp_path}')
    elif platform.system() == 'Darwin':  # macOS
        os.system(f'afplay {temp_path}')
    else:  # Linux
        os.system(f'mpg123 {temp_path} || play {temp_path}')


if __name__ == '__main__':
    print('🔊 Прочитане на текст на български (gTTS)')
    text = input('Въведи текст: ')
    if text.strip():
        speak_bulgarian(text)
    else:
        print('⚠️ Няма въведен текст.')
