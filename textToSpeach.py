from gtts import gTTS
from io import BytesIO
import pygame

def speak(text, language='en'):
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    return mp3_fo

pygame.init()
pygame.mixer.init()
sound = speak("Hola! ¿me escuchas? ¿me oyes? ¿me sientes?")
pygame.mixer.music.load(sound, 'mp3')
pygame.mixer.music.play()

#language = "es"
#text = "Hola! ¿me escuchas? ¿me oyes? ¿me sientes?"
#speech = gTTS(text=text, lang=language, slow=False, tld="com.mx")
#speech.save("TTS.mp3")