import uuid

import NewsManagment
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