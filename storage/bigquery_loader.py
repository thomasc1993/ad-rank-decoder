"""Load records into BigQuery."""

try:
    from google.cloud import bigquery
except ModuleNotFoundError:  # pragma: no cover
    bigquery = None

TABLE_ID = 'ads_dataset.top_ads'


def insert_record(record: dict):
    if bigquery is None:
        print("BigQuery client not available; skipping insert")
        return
    client = bigquery.Client()
    table = client.get_table(TABLE_ID)
    errors = client.insert_rows_json(table, [record])
    if errors:
        raise RuntimeError(errors)
