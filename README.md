# Audio Mood Analyzer

## Overview
Audio Mood Analyzer is a web application designed to facilitate the analysis of audio content. Users can upload audio files of various formats, and the application employs advanced Natural Language Processing (NLP) techniques to transcribe the speech within these files into text. Leveraging NLP's capabilities, particularly sentiment analysis, the system then evaluates the mood expressed in the transcribed text, providing users with insights into the emotional content of the audio. This process enables users to gain a deeper understanding of the sentiment conveyed in the spoken content, offering valuable applications in fields such as market research, customer feedback analysis, and emotional content evaluation.

## Features
- **Audio Upload**: Users can upload audio files in mp3 or wav format.
- **Speech to Text Conversion**: Converts the uploaded audio to text using Google Speech Recognition.
- **Mood Analysis**: Analyzes the mood of the transcribed text as either positive or negative.

## Setup
1. Clone the repository.
2. Navigate to the project directory:

   ```bash
   cd path/to/project/directory
   ```

3. Ensure Anaconda or Miniconda is installed on your system.
4. Create a Conda environment using the provided `environment.yml` file:

   ```bash
   conda env create -f environment.yml
   ```

5. Activate the Conda environment:

   ```bash
   conda activate mood_analysis_env
   ```

## Usage
1. Run the script using:
    
   ```bash
   streamlit run main.py
   ```

2. Open your web browser and navigate to the local URL provided by Streamlit to interact with the application.
3. Upload an audio file and click the "Analyze Mood" button to view the mood analysis.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.