"""Scraper module using Playwright to fetch ad HTML for keywords."""
from typing import Tuple, Any

# Import Playwright lazily so tests can run without the package installed.
try:
    from playwright.sync_api import sync_playwright
except ModuleNotFoundError:  # pragma: no cover - fallback for test env
    sync_playwright = None

from pathlib import Path


def fetch_ad_html(keyword: str, exclude_url: str | None = None) -> Tuple[str, Any]:
    """Return first paid ad HTML and the page handle.

    If ``exclude_url`` is provided, any ad whose primary link contains this
    value will be skipped, allowing selection of a competitor ad in the top
    position.
    """
    if sync_playwright is None:
        raise ImportError("playwright is required for scraping")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://www.google.com/search?q={keyword}")
        page.wait_for_timeout(3000)
        ad_elements = page.query_selector_all('div[data-text-ad]')
        selected = None
        for elem in ad_elements:
            if exclude_url:
                link = elem.query_selector('a')
                href = link.get_attribute('href') if link else ""
                if href and exclude_url in href:
                    continue
            selected = elem
            break
        html = selected.inner_html() if selected else ""
        return html, page


if __name__ == "__main__":
    for kw in Path('config/keywords.txt').read_text().splitlines():
        html, _ = fetch_ad_html(kw)
        print(kw, len(html))
