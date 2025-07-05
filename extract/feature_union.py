"""Merge visual and linguistic features."""
from datetime import datetime


def merge_features(keyword: str, html_features: dict, visual: dict, linguistic: dict) -> dict:
    record = {
        **html_features,
        **visual,
        **linguistic,
        "keyword": keyword,
        "scrape_ts": datetime.utcnow().isoformat(),
        "ad_rank": 1
    }
    return record
