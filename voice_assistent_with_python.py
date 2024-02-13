#change in speak function ,we take speak_ex function
#changing name also ,we can keep any name instead of jarvis like your name or any
#for female voice
import speech_recognition as sr
import pyttsx3                    #new package speaker like speaking purpose
import datetime as dt              #for time
import pywhatkit as pk
import wikipedia as  wiki      #for data ,youtube,music
listener =sr.Recognizer()
speaker=pyttsx3.init()   #pyttsx3 function

""" RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate                       #printing current voice rate
speaker.setProperty('rate', 150)     # setting up new voice rate

"""VOICE"""
voices = speaker.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

def speak(text):
    speaker.say("Yes boss,"+ text)
    speaker.runAndWait()

def speak_ex(text):
    speaker.say(text)
    speaker.runAndWait()


va_name="pinki"               #dynamic way
speak_ex("i am your " + va_name + "tell me boss.")
def take_command():
    command=" "
    try:
        with sr.Microphone() as source:
            print("listening .....")
            voice=listener.listen(source)
            command= listener.recognize_google(voice)
            command =command.lower()
            if va_name in command:
                command=command.replace(va_name + " ", " ")
                #print(command)     # noneed this command because we taken new command user_command
                #speaker .say(command)
                #speaker .runAndWait()
                #speak(command)     # no need this line because we taken new command user_command in calling function

    except:
        print("check your microphone")
    return command

#calling  the function
while True:                  #this is for repeating purpose ,its ask again and again
    user_command=take_command()
    #print(user_command)   #  now noo need this line
    #speak(user_command)  # now  noo need this line

    #to create break we use "close"  word
    if "close" in user_command:
        print("see you again boss i will be back whenever you call me")
        speak("see you again boss i will be back whenever you call me")
        break
    #to know the time
    elif "time" in user_command:
        cur_time=dt.datetime.now().strftime("%I:%M %p")
        print(cur_time)
        speak(cur_time)
        break
    elif "play" in user_command:
        user_command=user_command.replace("play", "")
        print("playing"+user_command)
        speak("playing"+user_command+",enjoy boss.")
        pk.playonyt(user_command)
        break
    elif "search for" in user_command or "google" in user_command:
        user_command=user_command.replace("search for ", "")
        user_command=user_command.replace("google", "")
        speak("searching for" + user_command)

        pk.search(user_command)
        break
        #print(user_command)
    elif "who is" in user_command:
        user_command=user_command.replace("who is", "")
        info=wiki.summary(user_command,2)
        print(info)
        speak(info)
        #print(user_command)
        break
    elif "example" in  user_command:
        user_command=user_command.replace("example", "")
        info=wiki.summary(user_command,2)
        print(info)
        speak(info)
        break
    elif "who are you" in user_command:
        speak("iam your " + va_name + "tell me boss")
    elif "what is your name" in user_command:
        speak("my name is" + va_name + ",tell me boss")
    else:
        speak_ex("plese say it again boss")

