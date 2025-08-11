from transformers import pipeline


classifier = pipeline("text-classification", model="distilbert-base-uncased")


class TextClassifier:

    @staticmethod
    def classify_document(doc_content):
        result = classifier(doc_content, truncation=True)
        return result[0]["label"], result[0]["score"]
