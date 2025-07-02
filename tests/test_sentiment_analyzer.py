import unittest
from psa import SentimentAnalyzer
from psa.SentimentAnalyzer import SentimentType
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class SentimentAnalyzerTest(unittest.TestCase):
    def test_Negative(self):
        prediction = SentimentAnalyzer.predictSentiment("I hate the summer")
        self.assertEqual(prediction["sentiment"], SentimentType.NEGATIVE.__str__())

    def test_Positive(self):
        prediction = SentimentAnalyzer.predictSentiment("I quite like the summer")
        print(f"Prediction: {prediction}")
        self.assertEqual(prediction["sentiment"], SentimentType.POSITIVE.__str__())

    def test_Positive_withLogits(self):
        prediction = SentimentAnalyzer.predictSentiment("I quite like the summer", outputLogit=True)
        print(f"Prediction: {prediction}")
        self.assertEqual(prediction["sentiment"], SentimentType.POSITIVE.__str__())
        logits = prediction["logits"]
        self.assertIsNotNone(logits)
        self.assertTrue(logits.shape == (1, 2))


if __name__ == '__main__':
    unittest.main()
