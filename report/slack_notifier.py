"""Send daily digest to Slack."""
import os
try:
    import requests
except ModuleNotFoundError:  # pragma: no cover
    requests = None

WEBHOOK = os.getenv('SLACK_WEBHOOK')


def post_message(text: str):
    if not WEBHOOK or requests is None:
        return
    requests.post(WEBHOOK, json={"text": text})
