from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class IntentClassifier:
    def __init__(self):
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.intents = {
           "billing":["refund policy","payment failed","invoice","payment","transaction","tax","discount","coupon","pricing details","payment method","price","cost"],
           "subscription":["cancel","upgrade","downgrade","change","plan","subscription","plan change","subscription change","renew subscription","renew plan"],
           "authentication":["login","logout","password","reset password","change password","two factor authentication","2fa","two step verification","2sv","forgot password","security question"],
           "integration":["zendesk integration","salesforce integration","jira integration","microsoft dynamics integration","slack integration","hubspot integration","supported integration"],
           "api":["api","api documentation","api key","api access","api limits","api rate limit","api authentication","api call","api endpoint","api structure"],
           "support":["contact","support","help","support team","contact support","contact us"],
           "troubleshoot":["system error","timeout issue","application crash","application freeze","application not responding","unexpected exception"]
           
        }
        self.intent_embeddings = {}
        for intent,examples in self.intents.items():
            embeddings=self.model.encode(examples)
            self.intent_embeddings[intent]=np.mean(embeddings,axis=0)

    def classify(self,query:str):
        query_embeddings = self.model.encode([query])[0]
        best_intent="general"
        best_score=-1
        for intent,embedding in self.intent_embeddings.items():
            score = cosine_similarity([query_embeddings], [embedding])[0][0]
            if score > best_score:
                best_score = score
                best_intent = intent
        return best_intent
    