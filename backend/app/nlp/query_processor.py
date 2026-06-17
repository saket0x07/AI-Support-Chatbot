from app.nlp.intent_classifier import IntentClassifier
from app.nlp.ner import NERExtract
from app.nlp.sentiment import SentimentAnalyzer

class QueryProcessor:

    def __init__(self):
        self.intent_classifier = IntentClassifier()
        self.ner_extractor = NERExtract()
        self.sentiment_analyzer = SentimentAnalyzer()

    def process(self,query):
        intent = self.intent_classifier.classify(query)
        ner = self.ner_extractor.extract(query)
        sentiment = self.sentiment_analyzer.analyze(query)
        return {
            "intent":intent,
            "ner":ner,
            "sentiment":sentiment
        }