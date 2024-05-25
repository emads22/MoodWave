import speech_recognition as sr
from app_utils import analyze_mood


def convert_audio_to_text(audio_file=None):
    # Create a recognizer object
    recognizer = sr.Recognizer()

    # Load audio file
    audio_file = "chile.wav"

    # Load audio file as audio data
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    text = recognizer.recognize_google(audio)

    return text
    

def testing_function():
    
    # Recognize speech using Google Speech Recognition
    try:
        text = convert_audio_to_text()
        # Perform sentiment analysis on the text to determine mood
        text_mood = analyze_mood(text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what was said.")
    except sr.RequestError as e:
        print("Sorry, I couldn't request results from Google Speech Recognition service; {0}".format(e))
    finally:  

        # Print the original text
        print(f'\n- Audio text is:\n=>', text)

        # Print the mood after sentiment analysis
        print(f'\n- After sentiment analysis, this text is:\n=>', end=" ")
        print(text_mood)


if __name__ == "__main__":
    testing_function()