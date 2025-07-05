# ad-rank-decoder

Ad Rank Decoder is a Python pipeline that scrapes the top Google Ads result,
uses GPT-4o (vision + text) to extract persuasion cues and rank which language
and visual elements drive ads to position #1. The pipeline delivers daily
influence scorecards with ready-to-push copy suggestions.

## Features

- Playwright scraper that captures paid ads and screenshots
- Extraction of linguistic and visual persuasion features using GPT-4o
- Storage of merged features in BigQuery
- Calculation of influence deltas for top signals
- Markdown scorecard generation and Slack notifications
- Docker and Terraform configuration for Cloud Run deployment

## Running locally

1. Install dependencies and Playwright browsers:

```bash
pip install playwright openai google-cloud-bigquery google-cloud-storage slack_sdk
playwright install chromium
```

2. Export the required environment variables:

- `OPENAI_API_KEY` – key for the OpenAI API
- `SLACK_WEBHOOK` – Slack incoming webhook URL
- Google Cloud credentials with access to BigQuery and Cloud Storage

3. Execute the pipeline:

```bash
python main.py
```

Keywords to scrape are defined in `config/keywords.txt`.

## Tests

Run the unit tests with:

```bash
python -m unittest
```

Tests mock external services so they run without cloud credentials.

## Deployment

The `infra` directory contains a `Dockerfile` and Cloud Build configuration for
building and deploying the application to Cloud Run. Terraform scripts under
`infra/terraform` provision required Google Cloud resources.
