import streamlit as st
from io import BytesIO
from app_utils import speech_to_text
from analysis import analyze_mood
from constants import LOGO_FILE


def app():

    st.markdown("""
        <p>
            <span style="display: inline; font-size: 3em; font-weight: bold;">MoodWave:&nbsp;&nbsp;</span>
            <span style="display: inline; font-size: 2em; font-weight: bold;">Audio Sentiment Analyzer</span>
        </p>
    """, unsafe_allow_html=True)

    # Add logo image from a file
    st.image(str(LOGO_FILE), width=300)

    # Add hint for accepted format
    st.subheader('Upload Audio File _(*WAV format only*)_')

    # Create a file uploader widget where users can upload audio files with WAV format only
    uploaded_file = st.file_uploader(
        "Choose an audio file", type=['wav'])

    # Check if an audio file is uploaded
    if uploaded_file is not None:
        # Display the uploaded audio file
        st.audio(uploaded_file, format='audio/wav')

        # Create two columns layout for displaying the analysis button and information
        col1, col2 = st.columns(2)

        # Inside the first column
        with col1:
            # Check if the 'Analyze Mood' button is clicked
            if st.button('Analyze Mood'):
                # Show a spinner indicating that mood analysis is in progress
                with st.spinner('Analyzing the mood...'):
                    # Read the contents of the uploaded file (type <class 'bytes'>)
                    audio_data = uploaded_file.read()

                    # Convert the audio data (type <class 'bytes'>) to a BytesIO object (type <class '_io.BytesIO'>)
                    # This conversion is necessary because many audio processing libraries (like speech-recognition)
                    # and functions expect a file-like object (BytesIO provides this functionality in memory without
                    # needing to write to disk). It also allows seamless integration with functions
                    # that accept file streams for further processing.
                    audio_bytes = BytesIO(audio_data)

                    # Pass the BytesIO object to the speech_to_text function to convert audio to text
                    text = speech_to_text(audio_bytes)

                    # Perform mood analysis using the recognized text
                    mood = analyze_mood(text)

                # Display the detected mood
                if mood == "Positive":
                    st.success(f'Detected Mood:&nbsp;&nbsp;&nbsp;&nbsp;{mood}')
                elif mood == "Negative":
                    st.warning(f'Detected Mood:&nbsp;&nbsp;&nbsp;&nbsp;{mood}')
                else:  # mood == "Neutral"
                    st.info(f'Detected Mood:&nbsp;&nbsp;&nbsp;&nbsp;{mood}')

        # Inside the second column
        with col2:
            # Provide information about the analysis process
            st.markdown("### Analysis Information")
            st.markdown(
                "The mood analysis will convert the speech in your audio file to text and then determine the mood from the text.")


if __name__ == "__main__":
    app()
