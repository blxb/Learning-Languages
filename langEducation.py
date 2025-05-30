import sounddevice as sd # library for recording sound
import speech_recognition as sr # library for speech recognition
import scipy.io.wavfile as wav # library for working with .wav files
import random as rand # library for using random function to choose words randomly from list later on
from googletrans import Translator # library for translating certain texts or words
import time # library that mainly is being used for making the script wait using time.sleep function
import sys # library that in this script is being used for script to terminate the process

AUDIO_DURATION = 5 # variable for how long the speech audio recording should go (right now it is set to 5 seconds, but you can set it to how many seconds you want to)
SAMPLE_RATE = 44100 # variable for audio's freqency or whatever it is supposed to do..

# small word dictionary and depending on the difficulity the words complexity increases.
words_by_level = {
    "easy": ["кот", "собака", "яблоко", "молоко", "солнце"],
    "medium": ["банан", "школа", "друг", "окно", "жёлтый"],
    "hard": ["технология", "университет", "информация", "произношение", "воображение"]
}

# A simple greeting using prints to make sure what's user is up to here.
print("Hello there! Welcome to Russian Language Education\n")
time.sleep(3)
print("Here you will learn russian words and also try to translate them\n")
time.sleep(3)
print("let's begin!\n") # using \n to leave some space for each print that we do so that user wouldn't be disorientated in script

time.sleep(1.5)

# asks which difficulity user wants to have (depending from that list again)
askDiff = input("Which level would you prefer to use? Easy, Medium or Hard?\n ")
selectedDiff = askDiff.lower() # using lowercase because in the list difficulities are all typed in lower cases and if it wouldnt use .lower then the script won't really find the word from that list.
if selectedDiff not in words_by_level: # checking if what user entered in terminal is not valid
    print("Reply with a level difficulty rather than something else.\n")
    sys.exit()
else:
    word = rand.choice(words_by_level[selectedDiff]) # selecting a random word from the list depending on which difficulity level did user prefer to use.

# list of languages that you can use to translate words with (you can add more languages aswell just use language codes too)
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

# asking user to which language he would prefer to translate randomly selected word to
askLang = input("Which language would you like to translate the word to?\n ").strip()
selectedLang = askLang.capitalize()

# again basically checking if what user prompted is valid now
if selectedLang in availableLanguages:
    lang_code = availableLanguages[selectedLang][0]
    print(f"You selected {selectedLang}. Language code is '{lang_code}'.")
else:
    print("Please choose a valid language from the list.\n")
    sys.exit()

print(f"The word you have to try translate to {selectedLang} is: {word}")

time.sleep(2)
print("Speak...\n")
# now we are recording an audio file and during recording user has to say the translation
recording = sd.rec(
  int(AUDIO_DURATION * SAMPLE_RATE),
  samplerate=SAMPLE_RATE,
  channels=1,
  dtype="int16")
sd.wait()

# converting recording to .wav file so we could recognize what user said
wav.write("transcriptOutput.wav", SAMPLE_RATE, recording)
print("Recording is finished, now recognizing\n")

time.sleep(2)

# with recognizer we transcribe what user said in the audio file
recognizer = sr.Recognizer()
with sr.AudioFile("transcriptOutput.wav") as source: # you can name the audio file however you want, only just leave .wav the same as it was before it is important.
    audio = recognizer.record(source)
    
try:
    text = recognizer.recognize_google(audio, language=lang_code)
    print("You said:", text) # and now we print what user said in the audio file
except sr.UnknownValueError:
    print("Couldn't recognize the speech \n")
    sys.exit()
except sr.RequestError as e:
    print(f"Server's error: {e}")
    sys.exit()
    
print("Now Translating your text to Russian language...\n")

time.sleep(2)

# now translating what user said to the dictionary's language (mine's for testing is Russian - "ru")
translator = Translator()
translated = translator.translate(text, dest="ru")

translatedText = translated.text

# we check if user translated the word correctly (using .lower because the dictionary in list is all written in lowercase)
if translatedText.lower() == word:
    print("You got it right!\n")  # following with a simple dialogue that congrats the user for getting it right
    time.sleep(2)
    print("Great Job!!\n")
    time.sleep(2)
    print("See you next time :)")
