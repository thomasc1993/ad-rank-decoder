"""Generate Markdown scorecard with GPT suggestions."""
import os

try:
    import openai
except ModuleNotFoundError:  # pragma: no cover
    openai = None

try:
    from google.cloud import bigquery
except ModuleNotFoundError:  # pragma: no cover
    bigquery = None


def generate():
    if bigquery is None:
        scores = []
    else:
        client = bigquery.Client()
        query = 'SELECT * FROM `ads_dataset.influence_scores` ORDER BY delta DESC LIMIT 5'
        scores = client.query(query).to_dataframe().to_dict('records')
    prompt = 'Suggest headlines based on these scores: ' + str(scores)
    if openai is not None:
        openai.api_key = os.getenv('OPENAI_API_KEY')
        # Placeholder API
        headlines = ['Great Sale', 'Best Prices', 'Shop Now']
    else:
        headlines = []
    markdown = '# Scorecard\n' + str(scores)
    return markdown, headlines
