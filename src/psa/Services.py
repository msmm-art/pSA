from fastapi import FastAPI
from psa import SentimentAnalyzer

app = FastAPI()

@app.get("/sentiment")
def get_sentiment(input: str):
    result = SentimentAnalyzer.predictSentiment(input)
    return {"input": input, "sentiment": result}