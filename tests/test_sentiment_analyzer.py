import unittest
from psa import SentimentAnalyzer

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class SentimentAnalyzerTest(unittest.TestCase):
    def test_Negative(self):
        prediction = SentimentAnalyzer.predictSentiment("I hate the summer")
        print(f"Prediction: {prediction}")
        self.assertEqual(prediction, "NEGATIVE")

    def test_Positive(self):
        prediction = SentimentAnalyzer.predictSentiment("I quite like the summer")
        print(f"Prediction: {prediction}")
        self.assertEqual(prediction, "POSITIVE")

    def test_Positive_withLogits(self):
        prediction, logits = SentimentAnalyzer.predictSentiment("I quite like the summer", outputLogit=True)
        print(f"Prediction: {prediction}")
        self.assertEqual(prediction, "POSITIVE")
        print(f"Logits: {logits}")
        self.assertIsNotNone(logits)
        self.assertTrue(logits.shape == (1, 2))


if __name__ == '__main__':
    unittest.main()
