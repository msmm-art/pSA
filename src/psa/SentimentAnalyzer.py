import torch
import transformers
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from enum import Enum

class SentimentType(Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


def predictSentiment(input:str = None, outputLogit:bool = False):
    print(f"Analyzing input {input}")
    tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
    model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

    inputs = tokenizer(input, return_tensors="pt")
    with torch.no_grad():
        try:
            out = model(**inputs)
            print("out", out)
            logits = out.logits
            print("logits", logits)
        except Exception as e:
            print(f"Error during model inference: {e}")
            return None

    predicted_class_id = logits.argmax().item()
    prediction = model.config.id2label[predicted_class_id]
    if outputLogit:
        return {"sentiment": prediction, "logits": logits}
    return  {"sentiment": prediction}