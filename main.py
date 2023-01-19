import pyttsx3
import PyPDF2
x = 1

speaker = pyttsx3.init()
while x == 1:
        print("Enter the speed rate of the voice(check sample with choice 2)")
        voicerate = int(input())
        speaker.setProperty('rate', voicerate)
        print("DO YOU WANT [1]FEMALE or [2]MALE Voice")
        v = int(input())
        if v == 1:
            voices = speaker.getProperty('voices')
            speaker.setProperty('voice', voices[1].id)

        print(
            "ENTER THE CHOICE(2 for checking voice rate)\n#1[DO you want to convert a pdf into audio]\n#2[[Do u want to convert your text into audio]")
        choice = int(input())
        if choice == 1:
            print("Enter teh file location path of the pdf you wanna convert to speech")
            path = str(input())
            try:
                pdf = open(path, "rb")
            except FileNotFoundError:
                print("path is not valid..No readable pdf found")
            finally:
                pass

            pdfReader = PyPDF2.PdfFileReader(pdf)
            pages = pdfReader.numPages
            print("from which page do want the text to be converted to speech from 0-" + str(pages))
            pg = int(input())
            for i in range(pg, pages):
                page = pdfReader.getPage(i)
                text = page.extractText()
                speaker.say(text)
                speaker.runAndWait()
        if choice == 2:
            f = open("tts.txt", "w+")
            f.close()
            print("Type Phrases to be converted into speech")
            with open("tts.txt", "w") as f:
                f.write(input())
            f = open("tts.txt", "r")
            contents = f.read()
            print(contents)
            speaker.say(contents)
            speaker.runAndWait()
        else:
            print("wrong choice by USER")
        print("do u wanna try again [1] else [0]")
        x = int(input())