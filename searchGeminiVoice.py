import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS
from dotenv import load_dotenv

# Configs and initializations
load_dotenv()
genai.configure(api_key=os.environ['API_KEY'])
model = genai.GenerativeModel("gemini-1.5-flash")
r = sr.Recognizer()
language = "en"

# Voice Recognition
def record_text():
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            return MyText
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("Unkown error ocurred.")

# Send prompt to Gemini
def voice_search(text):
    response = model.generate_content(text)
    return response

# Save the response and save it to mp3 file
def voice_response(text):
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("TTS.mp3")

# This will be replaced for a wake up word
text = record_text()
print(text)
if(text != None):
    gemini_search = voice_search(text)
    voice_response(gemini_search.text)

# Reproduce the response
os.system("start TTS.mp3")