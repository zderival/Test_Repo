import uuid

import NewsManagment
import Recomendations
from NewsManagment import NewsManager, Article


def test_filter_topics():
    assert NewsManager.filter_topics(["technology","sports","business"]) == "Technology,Sports,Business"

def test_article_to_df():
    article1 = Article(
        id=uuid.uuid4(),
        title="AI Article",
        source="CNN",
        publishedAt="published_at_dt",
        url="URL",
        topic="Tech",
        author="Author"
    )

    article2 = Article(
        id=uuid.uuid4(),
        title="Tech Article",
        source="The Verge",
        publishedAt="published_at_dt",
        url="URL",
        topic="Tech",
        author="Author"
    )
    articles = [article1,article2]
    df = NewsManagment.articles_to_df(articles)
    assert df["combined"][0] == article1.title + " " + article1.source
    assert df["combined"][1] == article2.title + " " + article2.source

def test_get_recommendations(  ):
    article1 = Article(
        id=uuid.uuid4(),
        title="AI Article",
        source="CNN",
        publishedAt="published_at_dt",
        url="URL",
        topic="Tech",
        author="Author"
    )

    article2 = Article(
        id=uuid.uuid4(),
        title="Tech Article",
        source="The Verge",
        publishedAt="published_at_dt",
        url="URL",
        topic="Tech",
        author="Author"
    )
    potential_articles = [article1, article2]
    saved_article = []
    result = Recomendations.get_recommendations(saved_article,potential_articles)
    assert result == potential_articles

def test_get_recommendations_correct():
    article1 = Article(
        id=uuid.uuid4(),
        title="AI breakthrough",
        source="TechCrunch",
        publishedAt="published_at_dt",
        url="URL",
        topic="Tech",
        author="Author"
    )

    article2 = Article(
        id=uuid.uuid4(),
        title="Machine learning trends",
        source="TechCrunch",
        publishedAt="published_at_dt",
        url="URL",
        topic="Tech",
        author="Author"
    )
    article3 = Article(
        id=uuid.uuid4(),
        title="Best pasta recipes",
        source="FoodNetwork",
        publishedAt="published_at_dt",
        url="URL",
        topic="Food",
        author="Author"
    )

    article4 = Article(
        id=uuid.uuid4(),
        title="New AI tool released",
        source="TechCrunch",
        publishedAt="published_at_dt",
        url="URL",
        topic="Tech",
        author="Author"
    )
    saved_article = [article1,article2]
    potential_article = [article3,article4]
    result = Recomendations.get_recommendations(saved_article,potential_article)
    assert result[0] == article4