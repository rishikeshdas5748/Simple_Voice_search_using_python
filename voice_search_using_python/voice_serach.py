import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()

with sr.Microphone() as source2:
    print("Say what to open: ")
    print("2Speak now -:")
    audio2 = r2.listen(source2, phrase_time_limit=2)
    text2 = r2.recognize_google(audio2)
    url2 = 'https://www.'+text2+'.com/'
    wb.get().open_new(url2)
    print("1Speak now:")
    with sr.Microphone() as source1:

        audio = r1.listen(source1, phrase_time_limit=5)
        if 'YouTube' in r1.recognize_google(audio):
            text = r1.recognize_google(audio)
            print("We are opening : {}".format(text))
            url = 'https://www.youtube.com/'
            wb.get().open_new(url)
            exit(0)
        elif 'Google' in r1.recognize_google(audio):
            text = r1.recognize_google(audio)
            print("We are opening : {}".format(text))
            url = 'https://www.google.com/'
            wb.get().open_new(url)
            exit(0)
        else:
            print("Didn't match with the programmed links..!!")
