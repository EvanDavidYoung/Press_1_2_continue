from decipher import *
# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # import speech_recognition as sr 
    import speech_recognition as sr
    r = sr.Recognizer()
    sample_audio = sr.AudioFile('TestFile/test.wav')
    with sample_audio as audio_file:
        audio_content = r.record(audio_file)
    print(type(audio_content))
    print(r.recognize_google(audio_content))

    # with sr.Microphone() as source:                # use the default microphone as the audio source
    #     audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

    # try:
    #     print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
    # except LookupError:                            # speech is unintelligible
    #     print("Could not understand audio")

    # r = sr.Recognizer()
    # mic = sr.Microphone()
    
    # with mic as audio_file:
    #     print("Speak Please")

    #     r.adjust_for_ambient_noise(audio_file)
    #     audio = r.listen(audio_file)

    #     print("Converting Speech to Text...")
    #     print("You said: " + r.recognize_google(audio))


print(decipher("Hi I just need a Prescription but for tires in the auto department"))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
