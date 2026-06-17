from app.nlp.query_processor import QueryProcessor

p = QueryProcessor()
r =p.process("I'm tired because my subscription was cancelled and i want refund")

print(r)