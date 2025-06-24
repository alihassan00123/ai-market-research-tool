import streamlit as st
from utils.scraper import extract_article_content
from utils.analysis import analyze_text_with_gpt
from utils.visuals import (
    generate_insight_chart,
    generate_noun_phrases_chart,
    generate_wordcloud,
    get_sentiment  # ✅ Add this
)

st.set_page_config(page_title="AI Market Research Tool", layout="wide")
st.title("📊 AI-Powered Market Research Tool")

st.markdown("""
### 🌐 Recommended Sources You Can Analyze
- [https://www.bbc.com/news](https://www.bbc.com/news)
- [https://techcrunch.com](https://techcrunch.com)
- [https://www.reuters.com](https://www.reuters.com)
- [https://www.bloomberg.com](https://www.bloomberg.com)
- [https://finance.yahoo.com](https://finance.yahoo.com)
- [https://www.investopedia.com](https://www.investopedia.com)
- [https://www.statista.com](https://www.statista.com)
- [https://www.wsj.com](https://www.wsj.com) *(paywall may limit content)*
- [https://www.marketscreener.com](https://www.marketscreener.com)
- [https://www.seekingalpha.com](https://www.seekingalpha.com)

*Note: Try URLs that point to actual articles or reports, not homepages.*
""")

url = st.text_input("🔗 Enter article or competitor website URL:")

if st.button("Analyze"):
    if not url.strip():
        st.warning("Please enter a valid URL.")
    else:
        with st.spinner("Extracting and analyzing..."):
            article = extract_article_content(url)
            if not article:
                st.error("Failed to extract article content.")
            else:
                summary = analyze_text_with_gpt(article)

                st.subheader("🧠 GPT Summary")
                st.markdown(summary)

                st.subheader("📊 Top Keywords")
                st.pyplot(generate_insight_chart(article))

                st.subheader("🧠 Key Noun Phrases")
                noun_fig = generate_noun_phrases_chart(article)
                if noun_fig:
                    st.pyplot(noun_fig)
                else:
                    st.info("Not enough phrases to display.")

                st.subheader("☁️ Word Cloud")
                st.pyplot(generate_wordcloud(article))

                st.subheader("📈 Overall Sentiment")
                st.success(f"🧭 Sentiment: **{get_sentiment(article)}**")
