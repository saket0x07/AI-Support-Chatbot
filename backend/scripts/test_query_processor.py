from app.nlp.query_processor import QueryProcessor

processor = QueryProcessor()

q=["How do i cancle my subsciption ?","What is the price of the premium plan ?","How do i upgrade my subscription ?","How do i downgrade my subscription ?","How do i change my subscription ?","How do i get help with my account ?","How do i report an error ?","How do i get support ?","What is the price of the premium plan ?","What's the refund policy","Which Platform does cloudflow integrate with?","Show all Support Integration"]


for query in q:
    print(f"\n Query: {query}")
    print(processor.process(query))