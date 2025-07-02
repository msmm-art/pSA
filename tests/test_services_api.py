import unittest
from fastapi.testclient import TestClient
from psa.SentimentAnalyzer import SentimentType
from psa.Services import app

class TestServicesAPI(unittest.TestCase):

        def setUp(self):
            self.client = TestClient(app)

        def test_api_sentiment_positive(self):
            response = self.client.get("/sentiment", params={"input": "I quite enjoy the summer"})
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(data["sentiment"], SentimentType.POSITIVE.__str__())

        def test_api_sentiment_negative(self):
            response = self.client.get("/sentiment", params={"input": "I don't like the summer"})
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertEqual(data["sentiment"], SentimentType.NEGATIVE.__str__())



if __name__ == '__main__':
    unittest.main()
