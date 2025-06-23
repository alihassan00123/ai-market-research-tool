import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
import spacy

# Load English NLP model (spaCy)
nlp = spacy.load("en_core_web_sm")

# ✅ 1. Top Keywords (Bar Chart)
def generate_insight_chart(text):
    words = [word.lower() for word in text.split() if len(word) > 5]
    common = Counter(words).most_common(10)
    labels, values = zip(*common)

    fig, ax = plt.subplots()
    ax.barh(labels, values, color='skyblue')
    ax.set_title('Top 10 Frequent Keywords')
    ax.invert_yaxis()
    return fig

# ✅ 2. Top Noun Phrases (Bar Chart)
def generate_noun_phrases_chart(text):
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

# ✅ 3. Word Cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    return fig
