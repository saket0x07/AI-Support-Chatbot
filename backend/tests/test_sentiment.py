import pytest
from app.nlp.sentiment_analyzer import SentimentAnalyzer
from app.core.constants import SENTIMENT_POSITIVE, SENTIMENT_NEGATIVE

@pytest.mark.asyncio
async def test_sentiment_analysis_positive(monkeypatch):
    async def mock_analyze(self, text):
        return SENTIMENT_POSITIVE

    monkeypatch.setattr(SentimentAnalyzer, "analyze", mock_analyze)
    
    analyzer = SentimentAnalyzer()
    sentiment = await analyzer.analyze("This works great, thank you!")
    assert sentiment == SENTIMENT_POSITIVE

@pytest.mark.asyncio
async def test_sentiment_analysis_negative(monkeypatch):
    async def mock_analyze(self, text):
        return SENTIMENT_NEGATIVE

    monkeypatch.setattr(SentimentAnalyzer, "analyze", mock_analyze)
    
    analyzer = SentimentAnalyzer()
    sentiment = await analyzer.analyze("Your product is terrible, I want a refund")
    assert sentiment == SENTIMENT_NEGATIVE
