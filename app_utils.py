import speech_recognition as sr


def speech_to_text(audio_file):
    """
    Convert speech audio to text using Google Speech Recognition.

    Parameters:
    audio_file (BytesIO): BytesIO object containing the audio data.

    Returns:
    str: The recognized text from the speech.
    """

    try:
        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Use the in-memory audio file as the audio source
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)  # read the entire audio file

        # Recognize the speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        return text

    # Handle cases where speech is not recognized
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio."

    # Handle cases where there is an issue with the Google Speech Recognition request
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

    # Handle cases where the audio file is not found
    except FileNotFoundError:
        return "Audio File not found."

    # Handle any other exceptions that may occur
    except Exception as e:
        return f"An error occurred while converting the speech track to text; {e}"
