import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Set the speech rate (optional)
engine.setProperty('rate', 150)  # Speech rate in words per minute

# Set the voice (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use the first voice

# Function to make the program speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Example usage
speak("welcome to robospeaker version 5.7 created by payal patil")
speak("what you want me to speak")

# You can also ask for user input and make the program speak it
while True:
    user_input = input("What would you like me to speak? ")
    if user_input.lower() == "quit":
        speak("bye bye friend see you soon")
        break
    speak(user_input)



