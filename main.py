import pyttsx3                            #text to speech (install)
import speech_recognition as sr           #recognizes voice (install)
import webbrowser                         #performs web search (built-in)
import datetime                           #date and time (built-in)
import pyjokes                            #collection of python jokes over the internet
import pywhatkit
import random
import wikipedia
from bs4 import BeautifulSoup
import requests


def sptext():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio_file = r.listen(source)
        print("Time over, thank you!")
        try:
            data = r.recognize_google(audio_file)
            return data        
        except sr.UnknownValueError:
            return "Sorry, didn't understood"

def autext(audiofile):
    r=sr.Recognizer()
    audio_file=sr.AudioFile(f"audio/{audiofile}")
    with audio_file as source:
        print("Recognizing...")
        audio_file = r.record(source)
        try:
            data = r.recognize_google(audio_file)
            return data
        except sr.UnknownValueError:
            return "Sorry, didn't understood"

def txspeech(text,voicemode=140):    #140 robo, 66 seductive, 136 low gossip
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate',175)
    engine.setProperty('voice', voices[voicemode].id)
    engine.say(f"{text}")
    engine.runAndWait()

def datentime(inp):
    temp=datetime.datetime.now()
    if inp==1:
        return temp.strftime("%I %M %p")
    elif inp==2:
        return temp.strftime("%d %B %Y")
    elif inp==3:
        return temp.strftime("%A")
    elif inp==4:
        return temp.strftime("%Y")
    elif inp==5:
        hour=int(temp.strftime("%H"))
        if (hour<12):  return "Good Morning Sir"
        elif (hour>=12 and hour<=14):  return "Good Afternoon Sir"
        else:  return "Good Evening Sir"

def misc(inp):
    if inp==1:
        misclis1=['Physically? Mentally? Financially? I am not sure what you mean', 'So much better now that you are with me', 'Armed and ready!', 'Much better than I deserve', 'Each day is better than the next', 'Everything is fine when you are around', 'Getting better with every passing second', 'Dangerously close to being fabulous', 'Not as good as you', 'Surviving, I guess', 'I am sober!', 'I will leave that up to your imagination', 'On a scale of one to punching someone in the face, I am at 7 point 5', 'Alright so far, but there is plenty of time for things to get bad']
        return random.choice(misclis1)
    elif inp==2:
        misclis2=['Old enough to know better, but still too young to care', 'Younger than I look', 'It is a secret', "You see, I don’t really believe in age or numbers", 'It is a trade secret', 'Not old enough, I guess', 'Oh dear, I have lost count!', 'I am between zero and death!', 'The last person who asked me that is still in the hospital', 'Unfortunately, I am not old enough to be on my deathbed. Sorry', 'Not old at all', 'I have lost track of how many days old I am']
        return random.choice(misclis2)

def game(inp):
    if inp==1:
        dice=random.choice([1,2,3,4,5,6])
        return f"I rolled {dice}"
    elif inp==2:
        playerscore=0
        compscore=0
        while(compscore!=3 and playerscore!=3):
            txspeech('rock, paper, scissor',mode)
            comprps=random.choice(['rock','paper','scissor'])
            print("Your turn...")
            playerrps=sptext().lower()
            if("quit" or "stop") in playerrps:
                break
            elif('rock' in playerrps):
                if(comprps=='paper'):
                    compscore+=1
                elif(comprps=='scissor'):
                    playerscore+=1
                txspeech(f"I chose {comprps}",mode)
            elif('paper' in playerrps):
                if(comprps=='scissor'):
                    compscore+=1
                elif(comprps=='rock'):
                    playerscore+=1
                txspeech(f"I chose {comprps}",mode)
            elif('scissor' in playerrps):
                if(comprps=='rock'):
                    compscore+=1
                elif(comprps=='paper'):
                    playerscore+=1
                txspeech(f"I chose {comprps}",mode)
            else:
                txspeech("Choose again",mode)
                continue
            print(f"Computer: {compscore}\nPlayer: {playerscore}")   
        if compscore==3:
            print("Computer wins")
            return "Better luck next time boss"
        elif playerscore==3:
            print("Player wins")
            return "Congratulations boss, you won"
        else:
            return "See you next time, boss"
    elif inp==3:
        pass      

def normalconv(inp):
    if inp==1:
        return "Hello boss, how are you ?"
    elif inp==2:
        reply=["that's awesome, boss", "that's great, boss", "superb boss", "that's excellent, boss", "cool"]
        return random.choice(reply)
    elif inp==3:
        return "you're welcome, boss"
    
def curse(inp):
    if inp==1:
        curselis1=["beti chod", "Teri Pan Di phudich chote da lund", "madar chod", "saala", "bhen chod", "gaandu", "huut ka patha","chhipkali ke gaand ke pasinae","tatoo ke saw daagar","randi chod", "bhen ka takka","choot ya", "randi", "bhosdi ke","bhen ke lund","Teri Maa Ki Choot"]
        random.shuffle(curselis1)
        fingaaali =""
        for gaali in curselis1[:4]:
            fingaaali+=gaali + ","
        return fingaaali
        madhav=["siddhi chod", "chaaru chod"]
        joydeep=["mahataa chod"]
    elif inp==2:
        return "muski pohonchi um, gaand me daali aah, lund se nikla waah, hawa me pakdi, zameen me patki, khich pitch khich pitch khich pitch, muski teri ma ki choot, hum badae mazboot hum badae mazboot hum badae mazboot"
    elif inp==3:
        if int(datetime.datetime.now().strftime("%H"))<12:
            greet="Good Morning"
        else:
            greet="Good Evening"
        intro = f"{greet} Sir, My name is Peter and I am a creation of some genious mind, My boss's roll number is 2022 Bachelors of Technology in Computer Science 0 2 3, My boss's name is Dhruv Khanna and he is from Yamuna Nagar Haryana, In joint entrance examination my boss's all india rank in common rank list is 6958, his twelveth school name is Sant Nischal Singh Public School which is affilated to Central Board of Secondary Education in which he scored 95.6 percentage"
        return intro

def search(inp,testdata):
    if inp==1:
        testdata = testdata.replace("petre","")
        testdata = testdata.replace("peter","")
        testdata = testdata.replace("google","")
        testdata = testdata.replace("search","")
        try:
            txspeech("This is what i found on google,", mode)
            pywhatkit.search(testdata)
            result = wikipedia.summary(testdata,1)
            return result
        except:
            return "no speakable output"
    elif inp==2:
        testdata = testdata.replace("petre","")
        testdata = testdata.replace("peter","")
        testdata = testdata.replace("youtube","")
        testdata = testdata.replace("search","")
        result = "https://www.youtube.com/results?search_query=" + testdata
        webbrowser.open(result)
        pywhatkit.playonyt(testdata)
        return "Done boss"
    elif inp==3:
        testdata = testdata.replace("petre","")
        testdata = testdata.replace("peter","")
        testdata = testdata.replace("wikipedia","")
        testdata = testdata.replace("search","")
        result=wikipedia.summary(testdata,2)
        txspeech("according to wikipedia",mode)
        print(result)
        return result
    elif inp==4:
        testdata = testdata.replace("petre","")
        testdata = testdata.replace("peter","")
        testdata = testdata.replace("what is","")
        url=f"https://www.google.co.in/search?q={'+'.join(testdata)}&client=....XynMBHWN-DtwQ_AUoAHOECAEQAg&biw=1440&bih=820&dpr=3"
        r=requests.get(url)
        
    
if __name__ == '__main__':
    mode=66
    start=sptext().lower()
    if(("peter" or "petre" or "wake up" or 'beta') in start):
        txspeech("How can I help you boss",mode)
        ans=True
        while(ans):
            testdata = sptext().lower()
            if(testdata=="Sorry, didn't understood".lower()):
                continue
            else:
                if ('quit' or 'sleep' or 'bye' or 'go to sleep') in testdata:
                    ans=False
                    txspeech("See you soon boss, till then bye", mode)
                elif ('hello' or 'hi') in testdata:
                    txspeech(normalconv(1),mode)
                elif ('fine' or 'i am fine' or "i'm fine" or 'i am good' or 'excellent' or 'supeb') in testdata:
                    txspeech(normalconv(2),mode)
                elif ('thanks' or 'thank you') in testdata:
                    txspeech(normalconv(3),mode)
                #date and time related responses
                elif 'time' in testdata:
                    txspeech(datentime(1),mode)
                elif 'date' in testdata:
                    txspeech(datentime(2),mode)
                elif 'day' in testdata:
                    txspeech(datentime(3),mode)
                elif 'year' in testdata:
                    txspeech(datentime(4),mode)
                elif ('wish' or 'wish me') in testdata:
                    txspeech(datentime(5),mode)
                elif ('temperature' or 'weather') in testdata:
                    txspeech(search(4,testdata),mode)
                elif "repeat" in testdata:
                    txspeech("After you boss, say something",mode)
                    flag=True
                    while(flag):
                        rep=sptext().lower()
                        if rep!=("Sorry, didn't understood".lower()):
                            txspeech(rep,mode)
                            flag=False
                        else:
                            txspeech("Please say again",mode)
                            continue
                #voice change
                elif ('robo' or 'robotic' or 'machine') in testdata:
                    mode=140
                    txspeech("Switched to robotic mode",mode)
                elif('whisper' or 'speak low' or 'talking to loud' or 'talk low' or 'to loud' or 'talking too loud') in testdata:
                    mode=136
                    txspeech("Switched to whisper mode",mode)
                elif('normal' or 'switch to normal' or 'default voice' or 'default sound' or 'default mode') in testdata:
                    mode=66
                    txspeech("Switched to default mode",mode)
                elif('how are you' or 'how you doing' or 'how are you doing') in testdata:
                    txspeech(misc(1),mode)
                elif('how old' or 'how old are you' or "age") in testdata:
                    txspeech(misc(2),mode)
                #games 
                elif('dice' or 'roll a dice' or 'roll dice') in testdata:
                    txspeech(game(1),mode)
                elif('rock' or 'paper' or 'scissor' or 'scissors' or 'rock paper and scissors') in testdata:
                    txspeech(game(2),mode)
                elif ('gali' or 'gaali' or 'curse' or 'madhav') in testdata:
                    txspeech(curse(1),mode)
                elif ('muski' or 'uski') in testdata:
                    txspeech(curse(2),mode)
                elif("intro") in testdata:
                    txspeech(curse(3),mode)
                elif('google' or 'search google') in testdata:
                    txspeech(search(1,testdata),mode)
                elif('youtube' or 'search youtube') in testdata:
                    txspeech(search(2,testdata),mode)
                elif('wikipedia' or 'search wikipedia') in testdata:
                    txspeech(search(3,testdata),mode)
                elif("+" or "-" or "*" or "into" or "/" or "power") in testdata:
                    try:
                        if "+" in testdata:
                            m=testdata.find("+")
                            ans=int(testdata[m-2]) + int(testdata[m+2])
                            txspeech(ans,mode)
                        elif "-" in testdata:
                            m=testdata.find("-")
                            ans=int(testdata[m-2]) - int(testdata[m+2])
                            txspeech(ans,mode)
                        elif("*") in testdata:
                            m=testdata.find("*")
                            ans=int(testdata[m-2]) * int(testdata[m+2])
                            txspeech(ans,mode)
                        elif("into") in testdata:
                            m=testdata.find("into")
                            ans=int(testdata[m-2]) * int(testdata[m+5])
                            txspeech(ans,mode)
                        elif "/" in testdata:
                            m=testdata.find("/")
                            ans=int(testdata[m-2]) / int(testdata[m+2])
                            txspeech(ans,mode)
                        elif "power" in testdata:
                            m=testdata.find("power")
                            ans=int(testdata[m-2])**int(testdata[m+6])
                            txspeech(ans,mode)
                    except:
                        txspeech("Sorry, couldn't recognize the expression",mode)
                        
                    
        

    elif(len(start)==0):
        pass
        


    # print(sptext())
    # print(autext("harvard.wav"))
    # txspeech("i cannot answer that")




