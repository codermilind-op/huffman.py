
# def solveMeFirst(a,b):
#     while a and b:
#         a= num1
#         b=num2
#         sum1=sum(a+b)
#
# num1 = int(input())
# num2 = int(input())
# res = num1+num2
# print(res)


	# Hint: Type return a+b below
# print(sum1)


# !/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# #
# # Complete the 'compareTriplets' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts following parameters:
# #  1. INTEGER_ARRAY a
# #  2. INTEGER_ARRAY b
# #
#
# def compareTriplets(a, b):
#     if a and b:
#         a[0] > b[0]
#         a[2] < b[2]
#         return 1
#     else:
#         a[1] = b[1]
#         return None
# #
# # a=int(input())
# # b=int(input())
# a[0]=int(input())
# a[1]=int(input())
# a[2]=int(input())
# b[0]=int(input())
# b[1]=int(input())
# b[2]=int(input())
# print(a,b)
#
#
#
#
#
#
#     # Write your code here
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     a = list(map(int, input().rstrip().split()))
#
#     b = list(map(int, input().rstrip().split()))
#
#     result = compareTriplets(a, b)
#
#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()




import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()