"""Train logistic regression model."""
try:
    from sklearn.linear_model import LogisticRegression
except ModuleNotFoundError:  # pragma: no cover
    LogisticRegression = None
try:
    from google.cloud import bigquery
except ModuleNotFoundError:  # pragma: no cover
    bigquery = None

MODEL_FILE = 'model.pkl'


def train():
    if LogisticRegression is None or bigquery is None:
        print("Training dependencies missing; skipping model training")
        return
    client = bigquery.Client()
    query = 'SELECT * FROM `ads_dataset.top_ads`'
    df = client.query(query).to_dataframe()
    X = df[['reading_grade_level']]
    y = (df['ad_rank'] == 1).astype(int)
    model = LogisticRegression().fit(X, y)
    import joblib
    joblib.dump(model, MODEL_FILE)
