import speech_recognition as sr	

def listen():
	# creating recognizer
	r = sr.Recognizer()
	# creating TTS engine 
	text = "" 
	with sr.Microphone() as source:                # use the default microphone as the audio source
		r.adjust_for_ambient_noise(source)
		print('working....')
		audio = r.listen(source, timeout=10.0)                   # listen for the first phrase and extract it into audio data
	try:
		text = r.recognize_google(audio)
	except LookupError:                   # speech is unintelligible
		text = ""
	print(text)    # recognize speech using Google Speech Recognition
	return text  

def confirm_listen(): 
	# creating recognizer
	r = sr.Recognizer()
	# creating TTS engine 
	# engine = ppyttsx3.init()

	text = "" 
	with sr.Microphone() as source:                # use the default microphone as the audio source
		r.adjust_for_ambient_noise(source)
		print('working....')
		# engine.say("Hi, welcome to Costco. In a couple of words, please share how I can help you today. If you would prefer to use the keypress menu, press 2. Para español, oprima nueve.")
		# engine.runAndWait()
		audio = r.listen(source, timeout=10.0)                   # listen for the first phrase and extract it into audio data
	try:
		text = r.recognize_google(audio)
		# print(decipher(text))
	except LookupError:                            # speech is unintelligible
		print("Could not understand audio")
	print(text)    # recognize speech using Google Speech Recognition
	if("yes" in text):
		return True
	if("no" in text):
		return False 
	return False 