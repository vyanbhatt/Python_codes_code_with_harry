import pyttsx3

if __name__ == '__main__':
    while(True):
        print("Welcome to robospeaker made by vasu")
        x = input("What you want me to speak: ")
        
        
        # Initialize the speech synthesizer
        engine = pyttsx3.init()
        
        # Convert text to speech
        engine.say(x)
        engine.runAndWait()

        if(x =="q"):
            print("Bye bye bro ")
            break:
