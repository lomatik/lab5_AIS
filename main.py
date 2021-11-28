import speech_recognition as sr
print('Select language of recognition:\n'
      'en - English\n'
      'ru - Russian\n'
      'uk - Ukrainian\n')

code = input()
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

if (code == 'en'):
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

elif(code == 'ru'):
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language='ru-RU'))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

elif(code == 'uk'):
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language='uk-UA'))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
