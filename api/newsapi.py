import os
from dotenv import load_dotenv

from newsapi import NewsApiClient


load_dotenv()

my_api_key = os.getenv('my_api_key')
newsapi = NewsApiClient(api_key=my_api_key)


# Получить и вывести список последних 10-ти новостей,
# выпущенных информационным агентством BBC
def get_latest_bbc_news():
    top_headlines = newsapi.get_top_headlines(sources='bbc-news')
    articles = top_headlines.get('articles', [])

    print("Последние 10 новостей от BBC:")
    for article in articles[:10]:
        print(f"Автор: {article['author']}")
        print(f"Заголовок: {article['title']}")
        print(f"Описание: {article['description']}")
        print(f"Дата публикации: {article['publishedAt']}")


# Получить и вывести список информационных агентств,
# публикующих новости на испанском языке
def get_spanish_news_sources():
    sources = newsapi.get_sources(language='es')
    sources_list = sources.get('sources', [])

    print("Информационные агентства, публикующие новости на испанском языке:")
    for source in sources_list:
        print(f"Название: {source['name']}\nОписание: {source['description']}")


# Получить и вывести список 5-ти последних новостей связанных с ИИ
def get_latest_ai_news():
    articles = newsapi.get_everything(q='artificial intelligence',
                                      sort_by='publishedAt')
    articles_list = articles.get('articles', [])

    print("Последние 5 новостей, связанных с ИИ:")
    for article in articles_list[:5]:
        print(f"Название: {article['title']}")
        print(f"Описание: {article['description']}")
        print(f"Дата публикации: {article['publishedAt']}")


def main():
    get_latest_bbc_news()
    print('\n')
    get_spanish_news_sources()
    print('\n')
    get_latest_ai_news()


if __name__ == '__main__':
    main()
