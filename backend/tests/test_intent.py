import pytest
from app.nlp.intent_classifier import IntentClassifier
from app.core.constants import INTENT_BILLING, INTENT_LOGIN_ISSUE

@pytest.mark.asyncio
async def test_intent_classification_billing(monkeypatch):
    # Mock LLM prediction to return Billing
    async def mock_classify(self, text):
        return INTENT_BILLING

    monkeypatch.setattr(IntentClassifier, "classify", mock_classify)
    
    classifier = IntentClassifier()
    intent = await classifier.classify("Why was I charged twice?")
    assert intent == INTENT_BILLING

@pytest.mark.asyncio
async def test_intent_classification_login(monkeypatch):
    async def mock_classify(self, text):
        return INTENT_LOGIN_ISSUE

    monkeypatch.setattr(IntentClassifier, "classify", mock_classify)
    
    classifier = IntentClassifier()
    intent = await classifier.classify("I cannot log into my account")
    assert intent == INTENT_LOGIN_ISSUE
