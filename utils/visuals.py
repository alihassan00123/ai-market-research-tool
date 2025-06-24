import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
import spacy
from textblob import TextBlob
import streamlit as st
import spacy.cli
spacy.cli.download("en_core_web_sm")  # ✅ Safe for Streamlit Cloud

# ✅ Cache and load spaCy NLP model
@st.cache_resource
def load_nlp():
    return spacy.load("en_core_web_sm")

nlp = load_nlp()

# ✅ 1. Sentiment Analysis
def get_sentiment(text):
    """
    Analyze sentiment polarity of the input text using TextBlob.
    Returns one of: Positive, Neutral, or Negative.
    """
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    if score > 0.1:
        return "Positive"
    elif score < -0.1:
        return "Negative"
    else:
        return "Neutral"

# ✅ 2. Top Keywords (Bar Chart)
def generate_insight_chart(text):
    """
    Generate a bar chart of the top 10 frequent words (min length > 5).
    """
    words = [word.lower() for word in text.split() if len(word) > 5]
    common = Counter(words).most_common(10)
    if not common:
        return None

    labels, values = zip(*common)
    fig, ax = plt.subplots()
    ax.barh(labels, values, color='skyblue')
    ax.set_title('Top 10 Frequent Keywords')
    ax.invert_yaxis()
    return fig

# ✅ 3. Top Noun Phrases (Bar Chart)
def generate_noun_phrases_chart(text):
    """
    Extract top noun phrases using spaCy and plot a horizontal bar chart.
    """
    doc = nlp(text)
    phrases = [chunk.text.lower() for chunk in doc.noun_chunks if len(chunk.text) > 2]
    common = Counter(phrases).most_common(10)
    if not common:
        return None

    labels, values = zip(*common)
    fig, ax = plt.subplots()
    ax.barh(labels, values, color='salmon')
    ax.set_title('Top 10 Noun Phrases')
    ax.invert_yaxis()
    return fig

# ✅ 4. Word Cloud
def generate_wordcloud(text):
    wc = WordCloud(width=600, height=300, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc)
    ax.axis("off")
    plt.tight_layout()
    return fig
