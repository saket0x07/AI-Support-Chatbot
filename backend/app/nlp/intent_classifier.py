class IntentClassifier:
    def classify(self,query:str):
        query=query.lower()

        if "hi" in query or "hello" in query:
            return "greeting"
        if "cancel" or "upgrade" or "downgrade" or "change" or "plan" or "subscription":
            return "subscription"
        if "billing" or "payment" or "invoice" or "receipt":
            return "billing"
        if "feature" or "feature list" or "features":
            return "feature"
        if "contact" or "support" or "help" or "support team":
            return "support"
        if "error" or "error code" or "error message" or "error code list":
            return "error"
        if "feature" or "feature list" or "features":
            return "feature"
        if "feature" or "feature list" or "features":
            return "feature"  
        return "other"  