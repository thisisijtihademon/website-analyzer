# crawler.py
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import tldextract

visited = set()

def is_internal_link(link, base_domain):
    parsed_link = urlparse(link)
    domain = tldextract.extract(parsed_link.netloc).domain
    return domain == base_domain

def crawl_website(start_url, max_pages=100):
    to_visit = [start_url]
    domain = tldextract.extract(start_url).domain
    pages = []

    while to_visit and len(pages) < max_pages:
        url = to_visit.pop()
        if url in visited:
            continue

        try:
            res = requests.get(url, timeout=5)
            if res.status_code != 200:
                continue

            visited.add(url)
            pages.append((url, res.text))

            soup = BeautifulSoup(res.text, 'html.parser')
            for a_tag in soup.find_all('a', href=True):
                link = urljoin(url, a_tag['href'])
                if is_internal_link(link, domain) and link not in visited:
                    to_visit.append(link)
        except:
            continue

    return pages
