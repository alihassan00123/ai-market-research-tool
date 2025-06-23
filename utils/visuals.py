import matplotlib.pyplot as plt
from collections import Counter

def generate_insight_chart(text):
    words = [word.lower() for word in text.split() if len(word) > 5]
    common = Counter(words).most_common(10)
    labels, values = zip(*common)

    fig, ax = plt.subplots()
    ax.barh(labels, values, color='skyblue')
    ax.set_title('Top 10 Frequent Keywords')
    return fig