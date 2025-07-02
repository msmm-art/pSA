import torch
import transformers
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

def predictSentiment(input = None, outputLogit = False):
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
        return prediction, logits
    return prediction