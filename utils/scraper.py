import requests
from bs4 import BeautifulSoup
import streamlit as st

@st.cache_data(ttl=3600)  # Cache for 1 hour
def extract_article_content(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Focus on article-specific tags
        body = soup.find('article') or soup.find('main') or soup
        text = ' '.join(p.get_text() for p in body.find_all('p'))
        return text[:8000].strip()
    except:
        return None
