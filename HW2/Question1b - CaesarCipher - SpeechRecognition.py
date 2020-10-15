#for Windows users you should install the packages via the below comments
#!pip install pipwin
#!pipwin install pyaudio
#!pip install SpeechRecognition
#!pip install pyspeech
import speech_recognition as sr
#1/b
def speak():
    r = sr.Recognizer()
    m = sr.Microphone()
    
    try:
        print("A moment of silence, please...")
        with m as source: r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
       
        while True:
            print("Say something!")
            with m as source: audio = r.listen(source)
            #with m as source: audio1 = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                    # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                #value1 = r.recognize_google(audio1)
                    # we need some special handling here to correctly print unicode characters to standard output
                print("The plain text you said: {}".format(value))
                #print("You said {}".format(value1))
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            if value != "":
                break;
        while True:
            print("Say a number!")
            with m as source: audio1 = r.listen(source)
            #with m as source: audio1 = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                    # recognize speech using Google Speech Recognition
                value1 = r.recognize_google(audio1)
                #value1 = r.recognize_google(audio1)
                    # we need some special handling here to correctly print unicode characters to standard output
                print("The number you said: {}".format(value1))
                #print("You said {}".format(value1))
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            if value1 != "":
                break
    except KeyboardInterrupt:
        pass
    return format(value), int(format(value1))

def encrypt(text,s):
    result = " "
 # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        if (ord(char) == 32):
            result += chr(ord(char))
 # Encrypt uppercase characters in plain text
        elif (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 # Encrypt lowercase characters in plain text
        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += chr((ord(char) + s - 48) % 26 + 48)
    return result

def decrypt(text,s):
    result = " "
 # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        if (ord(char) == 32):
            result += chr(ord(char))
 # Encrypt uppercase characters in plain text
        elif (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
 # Encrypt lowercase characters in plain text
        elif (char.islower()):
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += chr((ord(char) - s - 48) % 26 + 48)
    return result

def start():
    #x = (input("chon phuong thuc nhap"))
    x = (input("Enter '0' to input plain text by keyboard or '1' to input plain text by speech: "))
    if x == "0":
        st = str(input("Plain Text : "))
        s = int(input("Number of positions down: "))
        print("Cipher: " , encrypt(st,s))
        print("Decrypt to text: " , decrypt(encrypt(st,s),s))
    elif x == "1":
        strr = speak()
        #s = int(input("Number of positions down: "))
        print("Cipher: " , encrypt(strr[0],strr[1]))
    else:
        start()

start()