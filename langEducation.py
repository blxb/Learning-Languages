import sounddevice as sd
import speech_recognition as sr
import scipy.io.wavfile as wav
import random as rand
from googletrans import Translator
import time
import sys

AUDIO_DURATION = 5
SAMPLE_RATE = 44100

words_by_level = {
    "easy": ["кот", "собака", "яблоко", "молоко", "солнце"],
    "medium": ["банан", "школа", "друг", "окно", "жёлтый"],
    "hard": ["технология", "университет", "информация", "произношение", "воображение"]
}

print("Hello there! Welcome to Russian Language Education\n")
time.sleep(3)
print("Here you will learn russian words and also try to translate them\n")
time.sleep(3)
print("let's begin!\n")

time.sleep(1.5)

askDiff = input("Which level would you prefer to use? Easy, Medium or Hard?\n ")
selectedDiff = askDiff.lower()
if selectedDiff not in words_by_level:
    print("Reply with a level difficulty rather than something else.\n")
else:
    word = rand.choice(words_by_level[selectedDiff])

availableLanguages = {
    "Russian": ["ru"],
    "English": ["en"],
    "Spanish": ["es"],
    "Portugese": ["pt"],
    "Indonesian": ["id"],
    "Italian": ["it"],
    "Turkish": ["tr"],
}

print("Available languages:")
for lang in availableLanguages:
    print(f"- {lang}")

askLang = input("Which language would you like to translate the word to?\n ").strip()
selectedLang = askLang.capitalize()

if selectedLang in availableLanguages:
    lang_code = availableLanguages[selectedLang][0]
    print(f"You selected {selectedLang}. Language code is '{lang_code}'.")
else:
    print("Please choose a valid language from the list.\n")

print(f"The word you have to try translate to {selectedLang} is: {word}")

time.sleep(2)
print("Speak...\n")
recording = sd.rec(
  int(AUDIO_DURATION * SAMPLE_RATE),
  samplerate=SAMPLE_RATE,
  channels=1,
  dtype="int16")
sd.wait()

wav.write("transcriptOutput.wav", SAMPLE_RATE, recording)
print("Recording is finished, now recognizing\n")

time.sleep(2)

recognizer = sr.Recognizer()
with sr.AudioFile("transcriptOutput.wav") as source:
    audio = recognizer.record(source)
    
try:
    text = recognizer.recognize_google(audio, language=lang_code)
    print("You said:", text)
except sr.UnknownValueError:
    print("Couldn't recognize the speech \n")
    sys.exit()
except sr.RequestError as e:
    print(f"Server's error: {e}")
    sys.exit()
    
print("Now Translating your text to Russian language...\n")

time.sleep(2)

translator = Translator()
translated = translator.translate(text, dest="ru")

translatedText = translated.text

if translatedText.lower() == word:
    print("You got it right!\n")
    time.sleep(2)
    print("Great Job!!\n")
    time.sleep(2)
    print("See you next time :)")