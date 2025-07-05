"""Orchestrate daily scraping and analysis."""
from pathlib import Path
from scraper import playwright_scraper, screenshot_capture
from extract import parse_html, vision_features, linguistic_features, feature_union
from storage import bigquery_loader
from analysis import influence_score
from report import scorecard_generator, slack_notifier


def main(keywords=None):
    keywords = keywords or Path('config/keywords.txt').read_text().splitlines()
    for kw in keywords:
        html, page = playwright_scraper.fetch_ad_html(kw)
        gs_uri = screenshot_capture.capture_and_upload(page, kw)
        html_feats = parse_html.parse_ad(html)
        visual = vision_features.extract_visual_features(gs_uri)
        text = html_feats.get('headline', '') + ' ' + html_feats.get('description', '')
        ling = linguistic_features.extract_linguistic_features(text)
        record = feature_union.merge_features(kw, html_feats, visual, ling)
        bigquery_loader.insert_record(record)
    influence_score.run()
    markdown, headlines = scorecard_generator.generate()
    slack_notifier.post_message(markdown)


if __name__ == '__main__':
    main()
