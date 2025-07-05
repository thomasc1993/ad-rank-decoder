# ad-rank-decoder
Multimodal Python pipeline that scrapes the top Google Ads result, uses GPT-4o (vision + text) to extract persuasion cues, ranks which language and visual elements propel ads to position #1, and delivers daily influence scorecards with ready-to-push copy suggestions.

`fetch_ad_html` now accepts an optional `exclude_url` parameter so the scraper can skip any ad whose main link contains a specified URL. This lets the pipeline focus on competitor ads even when the primary slot is occupied by your own domain.
