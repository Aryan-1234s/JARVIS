import imghdr
from sqlite3 import converters
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from PIL import Image



#physics law of conservation (imp)
#[https://youtu.be/77ZF50ve6rs
#https://www.youtube.com/shorts/xKmXCvjR7BY
# pno. === l130,l339]
#[bg
#https://www.youtube.com/watch?v=QsnkNYnsn2c]
#intelligence algorithm from wolframalpha
#BY ARYAN SINGH

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


#code for changing web browser from edge to chrome
webbrowser.register('chrome', None)




def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir!")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon !")

	else:
		speak("Good Evening Sir!")

	name =("Jarvis ,the first point o created by Aryan Sir!")
	speak("I am your Assistant Jarvis ")
	speak(name)
	

def username():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("HELLO!!!!!!!!!".center(columns))
	print("Welcome Mr.", uname.center(columns))
	print("-----------------".center(columns))
	
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login('priyankarana080480@gmail.com', 'password')
	server.sendmail('priyankarana080480@gmail.com', to, content)
	server.close()


if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
	clear()
	wishMe()
	username()
	
	while True:
		
		query = takeCommand().lower()
		
		# All the commands said by user will be
		# stored here in 
		#AGTYR-"97319"-3422TBQ'query' and will be
		# converted to lower case for easily
		# recognition of command
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("https://www.youtube.com/")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("https://www.google.com/")

		elif 'class 9 math solutions' in query:
			speak("Here you go to your required destination.Math")
			webbrowser.open("https://byjus.com/ncert-solutions-class-9-maths/")


		elif 'class 9 science notes' in query:
			speak("Here you go to your required destination.Science notes")
			webbrowser.open("https://byjus.com/cbse-notes/class-9-science-notes/")

		elif 'class 9 science solutions' in query:
			speak("Here you go to your required destination.Science solutions")
			webbrowser.open("https://byjus.com/ncert-solutions-class-9-science/")	




		elif 'play music' in query or "play song" in query:
			speak("Here you go with music")
			webbrowser.open("https://www.youtube.com/watch?v=q5HLqoYUUaY")

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("% H:% M:% S")
			speak(f"Sir, the time is {strTime}")

		elif 'open google' in query:
			codePath = r"C:\\ProgramFiles\\Google\\Chrome\\Application\\chrome.exe"
			os.startfile(codePath)

		elif 'email to aryan' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				to = "priyankarana080480@gmail.com"
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")



		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			name = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			name = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(name)
			print("My friends call me", name)

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query:
			speak("I have been created by Aryan Singh.")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())
			
		#elif "calculate" in query:
			
			#app_id = "Wolframalpha api id"
			#client = wolframalpha.Client(app_id)
			#indx = query.lower().split().index('calculate')
			#query = query.split()[indx + 1:]
			#res = client.query(' '.join(query))
			#answer = next(res.results).text
			#print("The answer is " + answer)
			#speak("The answer is " + answer)

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "who i am" in query:
			speak("If you talk then definitely your a human.")

		elif "why did you came to the world" in query:
			speak("Thanks to Aryan. further It's a secret")

		elif 'power point presentation' in query:
			speak("opening Power Point presentation")
			power = r"C:\\Users\\ARYAN\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
			os.startfile(power)

		elif 'what is intelligence' in query:
			speak("Indeed, very important and was needed a lot to create me")

		elif "who are you" in query:
			speak("I am your virtual assistant created by Aryan")

		elif 'reason for your creation' in query:
			speak("I was created as a practice project by Mister Aryan ")



		elif 'open bluestack' in query:
			appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
			os.startfile(appli)

		elif 'news' in query:
			
			try:
				jsonObj = urlopen('https://www.wionews.com/')
				data = json.load(jsonObj)
				i = 1
				
				speak('here are some top news from the wion')
				print('''=============== WION ============'''+ '\n')
				
				for item in data['articles']:
					
					print(str(i) + '. ' + item['title'] + '\n')
					print(item['description'] + '\n')
					speak(str(i) + '. ' + item['title'] + '\n')
					i += 1
			except Exception as e:
				
				print(str(e))

		
	

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
	
		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop jarvis from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.nl / maps / place/" + location + "")

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('jarvis.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("% H:% M:% S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("jarvis.txt", "r")
			print(file.read())
			speak(file.read(6))

		
					
		# NPPR9-FWDCX-D2C8J-"06431"-H872K-2YT43
		elif "jarvis" in query:
			
			wishMe()
			speak("Jarvis 7 point o in your service Mister by respected Aryan Sir")
			speak(name)

		elif "weather" in query:
			
			# Google Open weather website
			# to get API of Open weather
			api_key = "Api key"
			base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
			speak(" City name ")
			print("City name : ")
			city_name = takeCommand()
			complete_url = base_url + "appid =" + api_key + "&q =" + city_name
			response = requests.get(complete_url)
			x = response.json()
			
			if x["cod"] != "404":
				y = x["main"]
				current_temperature = y["temp"]
				current_pressure = y["pressure"]
				current_humidiy = y["humidity"]
				z = x["weather"]
				weather_description = z[0]["description"]
				print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
			
			else:
				speak(" City Not Found ")
			
		elif "send message " in query:
				#Twilio to use this service
				account_sid = 'Account Sid key'
				auth_token = 'Auth token'
				client = Client(account_sid, auth_token)

				message = client.messages \
								.create(
									body = takeCommand(),
									from_='Sender No',
									to ='Receiver No'
								)

				print(message.sid)

		elif "open wikipedia" in query:
			webbrowser.open("wikipedia.com")

		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(name)

		
		elif "will you be my best friend" in query or "help me" in query:
			speak("Absolutely why not?")

		elif "how are you" in query:
			speak("I'm fine, glad you me that")

		elif "i like technology" in query:
			speak("Technology is my reason for existence")

		elif "who is Aryan" in query:
			speak("An IIT aspirant who loves physics,chemistry,math and computer science! ")	

		elif "image" in query:
			img = Image.open(r"C:\\Users\\gauta\\OneDrive\\Desktop\\[.jpg") 
			img.show()

		


#A Project By Respected Aryan Singh
#-- BY ARYAN SINGH --
