-- BigQuery table definition for top ads
CREATE TABLE IF NOT EXISTS `ads_dataset.top_ads` (
  scrape_ts TIMESTAMP,
  keyword STRING,
  ad_rank INT64,
  headline STRING,
  description STRING,
  paths ARRAY<STRING>,
  sitelinks ARRAY<STRING>,
  primary_value_prop STRING,
  urgency_words ARRAY<STRING>,
  social_proof BOOL,
  emotional_tone STRUCT<label STRING, intensity FLOAT64>,
  reading_grade_level FLOAT64,
  visual_badges ARRAY<STRING>
) PARTITION BY DATE(scrape_ts) CLUSTER BY keyword;
