import pyttsx3
import speech_recognition as sr 
def speak(text):
    engine = pyttsx3.init()
    voices=engine.getProperty("voices")
    print(voices)
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',170)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining ...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source,timeout=10,phrase_time_limit=6)
    
    try:
        query= r.recognize_google(audio,'en')
        print("User Said.",query)
    except Exception as e:

        print("Error -:",e)
        return ""
    return query.lower()



speak("Hello, I am your Alpha Assistance")