import speech_recognition as sr 
import webbrowser
from datetime import datetime
import time
import playsound
import os
import random
from gtts import  gTTS

r = sr.Recognizer()

def record_audio(ask = False):
	with sr.Microphone as source:
		if ask:
			print(ask)
		print('Hey, whats up?')
		"""Capturing voice data"""
		audio = r.listen(source)
		voice_data = ''
		try:
			voice_data = recognize_google(audio)
		except sr.UnknownValueError:
			print('Could you say that again? I did not quite get that')
		except sr.RequestError:
			print('Sorry, I am unable to reach my speach service at the moment')
		return voice_data


def reply(voice_data):
	if 'what is your name' in voice_data:
		print('My friends call me Tomi')
	if 'what time is it' in voice_data:
		now = datetime.now() # current date and time
		time = now.strftime("%I:%M %P")
		print('the time is {}'.format(time))
	if 'what is todays date'
		now = datetime.now() # current date and time
		date = now.strftime("%A %B %d")
		print('its {}'.format(date))
	if 'search' or 'google' or 'lookup' in voice_data:
		search = record_audio('What would you like me to look up?')
		url = 'https://google.com/search?q=' + search
		webbrowser.get().open(url)
		print('Here is what I found for ' + search)
	if 'location' or 'take me to' or 'directions' in voice_data:
		location = record_audio('Where would you like to go?')
		url = 'https://google.nl/maps/place/' + location + '/&amp;'
		webbrowser.get().open(url)
		print('Showing ' + location + ' on google maps')
	if 'exit' or 'stop' or 'thank you' or 'thanks' in voice_data:
		exit()

def tomi_talsk(audio_string):
	tts = gTTS(text=audio_string, lang='en')
	r = random.randint(1, 1000000)
	audio_file = 'audio-' +str(r) + '.mp3'
	tts.save(audio_file)
	playsound.playsound(audio_file)
	print(audio_string)
	os.remove(audio_file)

time.sleep(1)
print('Hey, whats up?')
while 1:
	voice_data = record_audio()
	reply(voice_data)