import pyttsx3		
def TTS(text):
	engine = pyttsx3.init()
	volume = engine.getProperty('volume')
	engine.setProperty('volume', volume-0.85)
	engine.say(text)
	engine.runAndWait()
