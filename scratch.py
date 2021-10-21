import os
import random
import pyttsx3
import time
guess = 0
restart = "yes"
chances = 3
start = "yes"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
speak("To stop the background music, go to your music player and press PAUSE button")
print("To stop the background music, go to your music player and press PAUSE button")
speak("Welcome to Squid game")
print("---------------------------------Welcome to Squid game---------------------------------")
os.startfile('WAV1.wav')
speak("I am Front man")
print("I am Front man")
speak("Do you want to play the game")
print("Do you want to play the game")
start = input("yes or no: ")
if start in  ("YES","yes","Y","y"):
    speak("If yes, Enter your name")
    name = input("Enter your name: ") 
    print("                             ")
    speak("Rules are simple!!!...")
    print("Rules are simple!!!...")
    speak("Rule 1 : Choose a number from given range")
    print("Rule 1 : Choose a number from given range")
    speak("Rule 2 : If my number and your numbers are same, then you win")
    print("Rule 2 : If my number and your numbers are same, then you win")
    speak("Rule 3 : If not, you will be eliminated")
    print("Rule 3 : If not, you will be eliminated")
    speak(name  + ", Your player ID is 001")
    print(name  + ", Your player ID is 001")
    print("                             ")
    speak("Player 001, on which level do you wish to play")
    print("Player 001, on which level do you wish to play")
    speak("as a begginer")
    speak("or, as a intermediate")
    speak("or, as a pro")
    # speak("Press  1 for Begginer     (Range from 1 to 15)")
    print("Press  1 for Begginer     (Range from 1 to 15)")
    # speak("Press  2 for Intermediate (Range from 1 to 20)")
    print("Press  2 for Intermediate (Range from 1 to 20)")
    # speak("Press  3 for Pro          (Range from 1 to 25)")
    print("Press  3 for Pro          (Range from 1 to 25)")
    # speak(",    Player 001 ")
    os.startfile('WAV2.wav')
    time.sleep(14)
    option = int(input("1,2, or 3: "))
    if option == 1:
        print("                             ")
        print("Player 001, choose a number between 1 to 15")
        speak("Player 001, choose a number between 1 to 15")
        speak(", you have 3 attempts")
        print("you have 3 attempts")
        print("Green light means right")
        print("Red   light means wrong")
        n = 15
        to_be_guessed = int(n*random.random())+1
        while chances>=0:
            time.sleep(1)
            print("                             ") 
            guess = int(input("Enter your number: "))
            os.startfile('WAV3.wav')
            time.sleep(8)
            if guess!= to_be_guessed:
                if guess>0:
                    if guess>to_be_guessed:
                        chances = chances-1
                        print("Red light")
                        os.startfile('WAV4.wav')
                        time.sleep(3)
                        # print("large")
                        if chances == 0:
                            time.sleep(2)
                            speak("No attempts left")
                            print("No attempts left")
                            break
                    elif guess<to_be_guessed:
                        chances = chances-1
                        print("Red light")
                        os.startfile('WAV4.wav')
                        time.sleep(3)
                        # print("small")
                        if chances == 0:
                            time.sleep(2)
                            speak("No attempts left")
                            print("No attempts left")
                            break 
            else:
                print("Green light")
                os.startfile('WAV5.wav')
                time.sleep(3)
                speak("Player 001, Congragulations, You won") 
                os.startfile('WAV7.wav')
                time.sleep(1)
                print(name + " Congragulations, You won")
                print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
                exit()
        
        print("                             ")        
        speak(name + ", do you want a 2nd chance?")
        print(name + ", do you want a 2nd chance?")
        restart = input("yes or no: ")
        chances = 3
        if restart in ("yes","YES","y","Y"):
            n=n*2
            to_be_guessed = int(n*random.random())+1
            speak("Player 001, your range will be doubled")
            speak("Now, you should choose a number between 1 to 30")
            print("Now, you should choose a number between 1 to 30")
            while chances>=0:
                print("                             ")
                guess = int(input("Enter your number: "))
                os.startfile('WAV3.wav')
                time.sleep(8)
                if guess!=to_be_guessed:
                    if guess>0:
                        if guess>to_be_guessed:
                            chances = chances-1
                            print("Red light")
                            os.startfile('WAV4.wav')
                            time.sleep(3)
                            print(chances," attempts left")
                            # speak("Player 001, Your number is greater than my number")
                            print("Hint:Your number is greater than my number")
                            if chances == 0:
                                time.sleep(2)
                                speak("No attempts left")
                                print("No attempts left")
                                os.startfile('WAV6.wav')
                                time.sleep(4)
                                speak("Player 001, eliminated")
                                print("Player 001, eliminated")
                                print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
                                os.system('shutdown/s')
                                exit()
                        elif guess<to_be_guessed:
                            chances = chances-1
                            print("Red light")
                            os.startfile('WAV4.wav')
                            time.sleep(3)
                            print(chances," attempts left")
                            # speak(name + ", Your number is smaller than my number")
                            print("Hint:Your number is smaller than my number")
                            if chances == 0:
                                time.sleep(2)
                                speak("No attempts left")
                                print("No attempts left")
                                os.startfile('WAV6.wav')
                                time.sleep(4)
                                speak("Player 001, eliminated")
                                print("Player 001, eliminated")
                                print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
                                os.system('shutdown/s')
                                exit()
                else:
                    print("Green light")
                    os.startfile('WAV5.wav')
                    time.sleep(3)
                    speak("Player 001 , Congragulations, You won") 
                    os.startfile('WAV7.wav')
                    time.sleep(1)
                    print(name + " Congragulations, You won")
                    print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
                    exit()
        else:
            os.startfile('WAV6.wav')
            time.sleep(4)
            speak("Player 001, ELiminated")
            print("Player 001, ELiminated")
            print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
            os.system('shutdown/s')
            exit()
    elif option == 2:
        print("                             ")
        speak("Player 001, choose a number between 1 to 20")
        print("Player 001, choose a number between 1 to 20")
        speak(", you have 3 attempts")
        print("you have 3 attempts")
        print("Green light means right")
        print("Red   light means wrong")
        n = 20
        to_be_guessed = int(n*random.random())+1
        while chances>=0:
            time.sleep(1)
            print("                             ")
            guess = int(input("Enter your number: "))
            os.startfile('WAV3.wav')
            time.sleep(8)
            if guess!= to_be_guessed:
                if guess>0:
                    if guess>to_be_guessed:
                        chances = chances-1
                        print("Red light")
                        os.startfile('WAV4.wav')
                        time.sleep(3)
                        # print("large")
                        if chances == 0:
                            time.sleep(2)
                            speak("No attempts left")
                            print("No attempts left")
                            break
                    elif guess<to_be_guessed:
                        chances = chances-1
                        print("Red light")
                        os.startfile('WAV4.wav')
                        time.sleep(3)
                        # print("small")
                        if chances == 0:
                            time.sleep(2)
                            speak("No attempts left")
                            print("No attempts left")
                            break 
            else:
                print("Green light")
                os.startfile('WAV5.wav')
                time.sleep(3)
                speak("Player 001, Congragulations, You won") 
                os.startfile('WAV7.wav')
                time.sleep(1)
                print(name + " Congragulations, You won")
                print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
                exit()

        print("                             ")    
        speak(name + ", do you want a 2nd chance?")
        print(name + ", do you want a 2nd chance?")
        restart = input("yes or no: ")
        chances=3
        if restart in ("yes","YES","y","Y"):
            n=n*2
            to_be_guessed = int(n*random.random())+1
            speak("Player 001, your range will be doubled")
            speak("Now, you should choose a number between 1 to 40")
            print("Now, you should choose a number between 1 to 40")
            while chances>=0:
                print("                             ")
                guess = int(input("Enter your number: "))
                os.startfile('WAV3.wav')
                time.sleep(8)
                if guess!=to_be_guessed:
                    if guess>0:
                        if guess>to_be_guessed:
                            chances = chances-1
                            print("Red light")
                            os.startfile('WAV4.wav')
                            time.sleep(3)
                            print(chances," attempts left")
                            print("Hint: Your number is greater than my number")
                            if chances == 0:
                                time.sleep(2)
                                speak("No attempts left")
                                print("No attempts left")
                                os.startfile('WAV6.wav')
                                time.sleep(4)
                                speak("Player 001, eliminated")
                                print("Player 001, eliminated")
                                print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
                                os.system('shutdown/s')
                                exit() 
                        elif guess<to_be_guessed:
                            chances = chances-1
                            print("Red light")
                            os.startfile('WAV4.wav')
                            time.sleep(3)
                            print(chances," attempts left")
                            print("Hint:Your number is smaller than my number")
                            if chances == 0:
                               time.sleep(2)
                               speak("No attempts left")
                               print("No attempts left")
                               os.startfile('WAV6.wav')
                               time.sleep(4)
                               speak("Player 001, eliminated")
                               print("Player 001, eliminated")
                               print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
                               os.system('shutdown/s')
                               exit()
                else:
                    print("Green light")
                    os.startfile('WAV5.wav')
                    time.sleep(3)
                    speak("Player 001 , Congragulations, You won") 
                    os.startfile('WAV7.wav')
                    time.sleep(1)
                    print(name + " Congragulations, You won")
                    print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
                    exit()
        else:
            os.startfile('WAV6.wav')
            time.sleep(4)
            speak("Player 001, ELiminated")
            print("Player 001, ELiminated")
            print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
            os.system('shutdown/s')
            exit()
    elif option == 3:
        print("                             ")
        speak("Player 001, choose a number between 1 to 25")
        print("Player 001, choose a number between 1 to 25")
        speak(", you have 3 attempts")
        print("you have 3 attempts")
        print("Green light means right")
        print("Red   light means wrong")
        n = 25
        to_be_guessed = int(n*random.random())+1
        while chances>=0:
            time.sleep(1)
            print("                             ")
            guess = int(input("Enter your number: "))
            os.startfile('WAV3.wav')
            time.sleep(8)
            if guess!= to_be_guessed:
                if guess>0:
                    if guess>to_be_guessed:
                        chances = chances-1
                        print("Red light")
                        os.startfile('WAV4.wav')
                        time.sleep(3)
                        # print("large")
                        if chances == 0:
                            time.sleep(2)
                            speak("No attempts left")
                            print("No attempts left")
                            break
                    elif guess<to_be_guessed:
                        chances = chances-1
                        print("Red light")
                        os.startfile('WAV4.wav')
                        time.sleep(3)
                        # print("small")
                        if chances == 0:
                            time.sleep(2)
                            speak("No attempts left")
                            print("No attempts left")
                            break 
            else:
                print("Green light")
                os.startfile('WAV5.wav')
                time.sleep(3)
                speak("Player 001, Congragulations, You won") 
                os.startfile('WAV7.wav')
                time.sleep(1)
                print(name + " Congragulations, You won")
                print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
                exit()

        print("                             ")     
        speak(name + ", do you want a 2nd chance?")
        print(name + ", do you want a 2nd chance?")
        restart = input("yes or no: ")
        chances=3
        if restart in ("yes","YES","y","Y"):
            n=n*2
            to_be_guessed = int(n*random.random())+1
            speak("Player 001, your range will be doubled")
            speak("Now, you should choose a number between 1 to 50")
            print("Now, you should choose a number between 1 to 50")
            while chances>=0:
                print("                             ")
                guess = int(input("Enter your number: "))
                os.startfile('WAV3.wav')
                time.sleep(8)
                if guess!=to_be_guessed:
                    if guess>0:
                        if guess>to_be_guessed:
                            chances = chances-1
                            print("Red light")
                            os.startfile('WAV4.wav')
                            time.sleep(3)
                            print(chances," attempts left")
                            # speak(name + ", Your number is greater than my number")
                            print("Hint:Your number is greater than my number")
                            if chances == 0:
                                time.sleep(2)
                                speak("No attempts left")
                                print("No attempts left")
                                os.startfile('WAV6.wav')
                                time.sleep(4)
                                speak("Player 001, eliminated")
                                print("Player 001, eliminated")
                                print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
                                os.system('shutdown/s /t 0')
                                exit()
                        elif guess<to_be_guessed:
                            chances = chances-1
                            print("Red light")
                            os.startfile('WAV4.wav')
                            time.sleep(3)
                            print(chances,", attempts left")
                            # speak(name + " Your number is smaller than my number")
                            print("Hint:Your number is smaller than my number")
                            if chances == 0:
                               time.sleep(2)
                               speak("No attempts left")
                               print("No attempts left")
                               os.startfile('WAV6.wav')
                               time.sleep(4)
                               speak("Player 001, eliminated")
                               print("Player 001, eliminated")
                               print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
                               os.system('shutdown/s')
                               exit()
                else:
                    print("Green light")
                    os.startfile('WAV5.wav')
                    time.sleep(3)
                    speak("Player 001 , Congragulations, You won") 
                    os.startfile('WAV7.wav')
                    time.sleep(1)
                    print(name + " Congragulations, You won")
                    print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
                    exit() 
        else:
            os.startfile('WAV6.wav')
            time.sleep(4)
            speak("Player 001, ELiminated")
            print("Player 001, ELiminated")
            print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
            os.system('shutdown/s')
            exit()                                
elif start in ("NO","no","N","n"):
    print("we feel pity... to say Goodbye like this")
    speak("we feel pity... to say Goodbye like this")
    print("---------------------------------Created By Prajwal S U | © 2021 All Rights Reserved---------------------------------")
            
#Created By Prajwal S U | © 2021 All Rights Reserved 
        
                  





