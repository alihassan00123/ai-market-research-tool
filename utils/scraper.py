import requests
from bs4 import BeautifulSoup

def extract_article_content(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join(p.text for p in paragraphs)
        return text[:8000]  # Limit size for GPT
    except:
        return None