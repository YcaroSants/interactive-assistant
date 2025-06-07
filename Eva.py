import os
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import serial
import time
import pyautogui  # <--- Adicionado

arduino = serial.Serial('COM4', 9600)  # Troca COM4 pela porta certa
time.sleep(2)  # Espera o Arduino reiniciar

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language='pt-BR')
        print("Você disse:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("😕 não entendi.")
        return ""
    except sr.RequestError:
        print("Could not connect to the recognition service.")
        return ""

# Main loop
while True:
    command = listen_command()

    if "sara" in command and "hora" in command:
        agora = datetime.now().strftime("%H:%M")
        speak(f"São {agora}, senhor.")

    elif "sara" in command and "navegador" in command:
        speak("Abrindo o navegador, senhor.")
        os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
    
    elif "sara" in command and "tchau" in command:
        speak("Até mais, Icáro!")
        break

    elif "sara" in command and "ligar" in command and "luz" in command:
        speak("ligando a luz.")
        arduino.write(b'L')

    elif "sara" in command and "apagar" in command and "luz" in command:
        speak("desligando a luz.")
        arduino.write(b'D')

    elif "sara" in command and "tela cheia" in command:
        speak("Entrando em tela cheia.")
        pyautogui.press('f11')

    elif "sara" in command and "área de trabalho" in command:
        speak("mostrando área de trabalho.")
        pyautogui.hotkey('win', 'd')

    elif "sara" in command:
        speak("estou aqui.")
