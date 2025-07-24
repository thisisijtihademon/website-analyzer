# analyzer.py
from bs4 import BeautifulSoup
from collections import Counter
import re

def analyze_page(html):
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.title.string.strip() if soup.title else 'No title'
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    meta_content = meta_desc['content'].strip() if meta_desc else 'No meta description'

    h_tags = {f'h{i}': [h.get_text(strip=True) for h in soup.find_all(f'h{i}')] for i in range(1, 7)}

    text = soup.get_text(separator=' ', strip=True)
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)
    top_keywords = Counter(words).most_common(10)

    return {
        'title': title,
        'meta_description': meta_content,
        'word_count': word_count,
        'top_keywords': top_keywords,
        **h_tags
    }
