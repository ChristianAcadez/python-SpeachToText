import speech_recognition as sr

r = sr.Recognizer()

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

def output_text(text):
    f = open("output.txt","a")
    f.write(text)
    f.write("\n")
    f.close()
    return

# this is going to be changed with a wake up word
flag = True
while(flag):
    text = record_text()
    output_text(text)
    print("wrote text")
    again = input("speak again? y/n: ")
    if(again == "n"): 
        flag = False