import requests
from bs4 import BeautifulSoup

def extract_article_content(url):
    """
    Fetch and extract visible article content from the given URL.
    Returns clean text (max 8000 characters) or None if failed.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # raises HTTPError for bad responses

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join(p.get_text(strip=True) for p in paragraphs)
        return text[:8000] if text else None

    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        return None
