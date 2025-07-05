"""Scraper module using Playwright to fetch ad HTML for keywords."""
from typing import Tuple, Any

# Import Playwright lazily so tests can run without the package installed.
try:
    from playwright.sync_api import sync_playwright
except ModuleNotFoundError:  # pragma: no cover - fallback for test env
    sync_playwright = None

from pathlib import Path


def fetch_ad_html(keyword: str) -> Tuple[str, Any]:
    """Return first paid ad HTML and the page handle."""
    if sync_playwright is None:
        raise ImportError("playwright is required for scraping")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://www.google.com/search?q={keyword}")
        page.wait_for_timeout(3000)
        # Simplistic selector for ad container - placeholder
        ad_element = page.query_selector('div[data-text-ad]')
        html = ad_element.inner_html() if ad_element else ""
        return html, page


if __name__ == "__main__":
    for kw in Path('config/keywords.txt').read_text().splitlines():
        html, _ = fetch_ad_html(kw)
        print(kw, len(html))
