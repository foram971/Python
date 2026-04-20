import pyttsx3

# Initialize the converter
engine = pyttsx3.init()

# Text to be spoken
text = 'Hello! This is a text-to-speech conversion using pyttsx3.'

# Saying the text
engine.say(text)

# Wait until speaking is finished
engine.runAndWait()