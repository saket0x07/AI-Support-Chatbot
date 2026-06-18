from app.nlp.intent_classifier import IntentClassifier
from app.nlp.ner import NERExtract
from app.nlp.sentiment import SentimentAnalyzer

class QueryProcessor:

    def __init__(self):
        self.intent_classifier = IntentClassifier()
        self.ner_extractor = NERExtract()
        self.sentiment_analyzer = SentimentAnalyzer()

    def detect_query_type(self,query:str):
        query = query.lower().strip()

        if any(keyword in query for keyword in["list","all","show","Which platform","Which provider","integration","integrations","connectors","apis"]):
            return "list_question"
        if query.startswith(("how","how do","how can","steps","guide","procedure")):
            return "how_to"
        if any(keyword in query for keyword in["compare","vs","versus","differences","difference"]):
            return "comparison"
        if query.startswith(("what","which","who","where","when","why","can","does","is","are")):
            return "fact_question"
        return "general_question"        


    def detect_complexity(self,query:str):
        words=len(query.split())
        if words < 5:
            return "simple"
        elif words < 15:
            return "medium"
        else:
            return "complex"  
        

    def process(self,query:str):
        intent = self.intent_classifier.classify(query)
        ner = self.ner_extractor.extract(query)
        sentiment = self.sentiment_analyzer.analyze(query)
        query_type=self.detect_query_type(query)
        complexity=self.detect_complexity(query)
        return {
            "intent":intent,
            "ner":ner,
            "sentiment":sentiment,
            "query_type":query_type,
            "complexity":complexity
        }