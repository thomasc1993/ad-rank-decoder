"""End-to-end pipeline test with mocks."""
import unittest
from unittest import mock

import main


class PipelineTest(unittest.TestCase):
    @mock.patch('storage.bigquery_loader.insert_record')
    @mock.patch('report.slack_notifier.post_message')
    @mock.patch('analysis.influence_score.run')
    @mock.patch('extract.linguistic_features.extract_linguistic_features', return_value={'primary_value_prop':'test'})
    @mock.patch('extract.vision_features.extract_visual_features', return_value={'visual_badges':['star']})
    @mock.patch('scraper.screenshot_capture.capture_and_upload', return_value='gs://bucket/image.png')
    @mock.patch('scraper.playwright_scraper.fetch_ad_html', return_value=('html', object()))
    def test_pipeline(self, *mocks):
        main.main(['test'])
        mocks[6].assert_called()  # insert_record called
        mocks[1].assert_called()  # slack notified


if __name__ == '__main__':
    unittest.main()
