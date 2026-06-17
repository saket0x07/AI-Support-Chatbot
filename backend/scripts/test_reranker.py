from app.rag.reranker import Reranker

docs=["How to reset password","How to change password","How to upgrade subscription","How to downgrade subscription","How to cancel subscription","How to contact support","How to get help","How to file a complaint","How to get a refund","How to get a discount"]

reranker=Reranker()

r=reranker.rerank(query=" Refund policy",docs=docs)

print(r)