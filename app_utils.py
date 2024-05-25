import nltk
from nltk.data import find
from nltk.sentiment import SentimentIntensityAnalyzer



def download_nltk_vader_lexicon():
    """
    Checks if the NLTK Vader lexicon is available. If not, downloads it.
    
    This function checks if the NLTK Vader lexicon is available in the NLTK data
    directory. If it's not found, it downloads the lexicon. NLTK (Natural Language
    Toolkit) provides tools and resources for working with human language data.
    The Vader lexicon is a lexicon for sentiment analysis.

    Args:
        None

    Returns:
        None
    """
    try:
        # Check if the NLTK Vader lexicon is available
        nltk.data.find('sentiment/vader_lexicon')
    except LookupError:
        # If the lexicon is not found, download it
        nltk.download('vader_lexicon')



def analyze_mood(text):
    """
    Analyze the mood (positive or negative) of a given text.

    Args:
        text (str): The input text to analyze.

    Returns:
        str: The mood of the text, either "Positive" or "Negative".
    """
    # Download the NLTK Vader lexicon
    download_nltk_vader_lexicon()

    # Initialize SentimentIntensityAnalyzer for sentiment analysis
    analyzer = SentimentIntensityAnalyzer()

    # Perform sentiment analysis on the text
    sentiment_scores = analyzer.polarity_scores(text)

    # Determine mood based on the compound sentiment score
    if sentiment_scores["compound"] < 0:
        return "Negative"
    else:
        return "Positive"
