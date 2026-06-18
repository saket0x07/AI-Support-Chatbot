from app.nlp.intent_classifier import IntentClassifier
classifier = IntentClassifier()
queries=["i forgot my password","whats the refund policy","im getting timeout error","how to enable 2fa","Show all Support Integration","How do i cancel my subscription","How do i upgrade my subscription","How do i get support"]
for query in queries:
    print(classifier.classify(query))