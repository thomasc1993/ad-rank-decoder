"""Parse ad HTML into structured fields."""

try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:  # pragma: no cover
    BeautifulSoup = None
from typing import Dict


def parse_ad(html: str) -> Dict:
    if BeautifulSoup is None:
        return {
            'headline': '',
            'description': '',
            'paths': [],
            'sitelinks': []
        }
    soup = BeautifulSoup(html, 'html.parser')
    return {
        'headline': soup.find('h3').get_text() if soup.find('h3') else '',
        'description': soup.find('div').get_text() if soup.find('div') else '',
        'paths': [a.get_text() for a in soup.find_all('span', class_='VuuXrf')],
        'sitelinks': [a.get_text() for a in soup.find_all('a', class_='sitelink')] 
    }
