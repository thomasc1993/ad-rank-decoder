"""Capture screenshots and upload to Cloud Storage."""

try:
    from google.cloud import storage
except ModuleNotFoundError:  # pragma: no cover
    storage = None
from datetime import datetime
from pathlib import Path

BUCKET_NAME = 'screenshots'


def capture_and_upload(page, keyword: str) -> str:
    if storage is None:
        raise ImportError("google-cloud-storage is required")
    filename = f"{keyword.replace(' ', '_')}_{datetime.utcnow().isoformat()}.png"
    path = Path('/tmp') / filename
    page.screenshot(path=path, full_page=True)
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(filename)
    blob.upload_from_filename(str(path))
    return f"gs://{BUCKET_NAME}/{filename}"
