import streamlit as st
from utils.scraper import extract_article_content
from utils.analysis import analyze_text_with_gpt
from utils.visuals import generate_insight_chart

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

if url:
    with st.spinner("🔍 Extracting content..."):
        raw_text = extract_article_content(url)

    if raw_text:
        st.subheader("📄 Extracted Content")
        st.text_area("Content Preview", raw_text[:2000], height=200)

        st.subheader("🧠 GPT-4 Market Analysis")
        insights = analyze_text_with_gpt(raw_text)
        st.write(insights)

        st.subheader("📈 Visualization")
        fig = generate_insight_chart(raw_text)
        st.pyplot(fig)
    else:
        st.warning("Failed to extract content from the URL. Please try another.")