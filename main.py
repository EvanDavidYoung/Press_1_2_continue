from decipher import *
import speech_recognition as sr	
# import pyttsx3

# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	# creating recognizer
	r = sr.Recognizer()
	# creating TTS engine 
	# engine = ppyttsx3.init()


	with sr.Microphone() as source:                # use the default microphone as the audio source
		r.adjust_for_ambient_noise(source)
		print('working....')
		# engine.say("Hi, welcome to Costco. In a couple of words, please share how I can help you today. If you would prefer to use the keypress menu, press 2. Para español, oprima nueve.")
		# engine.runAndWait()
		audio = r.listen(source, timeout=10.0)                   # listen for the first phrase and extract it into audio data
	try:
		text = r.recognize_google(audio)
		print(text)    # recognize speech using Google Speech Recognition
		print(decipher(text))
	except LookupError:                            # speech is unintelligible
		print("Could not understand audio")
	# r = sr.Recognizer()
	# mic = sr.Microphone()

	# with mic as audio_file:
	#     print("Speak Please")

	#     r.adjust_for_ambient_noise(audio_file)
	#     audio = r.listen(audio_file)

	#     print("Converting Speech to Text...")
	#     print("You said: " + r.recognize_google(audio))


	# print(decipher("Hi I just need a Prescription but for tires in the auto department"))




	# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# I need to order a glasses prescription 
# I want to get new tires 
# I want to print pictures