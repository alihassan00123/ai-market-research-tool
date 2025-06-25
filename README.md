# 🧠 AI-Powered Market Research Tool

This project is an AI-powered market research assistant that extracts article content from URLs, analyzes it using GPT-4 or GPT-3.5, and provides visual insights like keyword charts, sentiment analysis, and word clouds — all inside a Streamlit web app.

---

## 🚀 Features

- 🌐 **URL Input** – Fetch article text from public news or competitor websites
- 🧠 **GPT-Based Summary** – Summarizes the article into business-relevant insights
- 📊 **Top Keywords Chart** – Bar chart of most frequent words
- 💬 **Noun Phrase Chart** – Highlights key topics using spaCy NLP
- ☁️ **Word Cloud** – Visual cloud of commonly used words
- 📈 **Sentiment Analysis** – Classifies tone as Positive, Negative, or Neutral
- 🖥️ **Streamlit Interface** – Clean and interactive UI ready for deployment
- 🔒 **Secure API Key Loading** – Uses Streamlit secrets or environment variables

---

## 📁 Project Structure

```bash
├── app.py                    # Main Streamlit app
├── requirements.txt          # Required packages
├── runtime.txt               # Python version (for Streamlit Cloud)
├── utils/
│   ├── __init__.py
│   ├── scraper.py            # Web content extractor
│   ├── analysis.py           # GPT summary engine
│   └── visuals.py            # Chart & NLP functions
└── README.md                 # You are here!


## 🧰 Requirements
- Python 3.8+
- OpenAI API Key
- Internet connection

## 🔧 Installation

```bash
pip install -r requirements.txt
```

## 🔑 Set API Key

```bash
export OPENAI_API_KEY=your_key_here
```

## ▶️ Run the App

```bash
streamlit run app.py
```

## 📦 Output
- GPT-generated business summary
- Bar chart of top keywords
- Noun phrase analysis
- Word cloud
- Sentiment label: ✅ Positive / ❗️Negative / ⚖️ Neutral
---
Created with ❤️ by AI Tools Co.
