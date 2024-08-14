import wikipedia


# Получить данные о странице про язык программирования Python и вывести
# заголовок и первые 60 символов из краткого содержания статьи
def get_python_page_info():
    wikipedia.set_lang("en")
    page = wikipedia.page("Python (programming language)")
    title = page.title
    summary = page.summary[:60]

    print(f"Заголовок: {title}")
    print(f"Краткое содержание (первые 60 символов): {summary}")


# Вывести первые 40 символов из содержимого секции истории языка
def get_history_section_info():
    wikipedia.set_lang("en")
    page = wikipedia.page("Python (programming language)")
    sections = page.section('History')[:40]

    print(f"Секция истории языка: {sections}")


# Вывести заголовок и первые 140 символов из краткого содержания
# статьи на одном из языков на которых доступна статья
def get_article_in_another_language():
    wikipedia.set_lang("ru")
    page_ru = wikipedia.page("Python (programming language)")
    title = page_ru.title
    summary = page_ru.summary[:140]

    print(f"Заголовок: {title}")
    print(f"Краткое содержание (первые 140 символов): {summary}")


def main():
    get_python_page_info()
    print('\n')
    get_history_section_info()
    print('\n')
    get_article_in_another_language()


if __name__ == '__main__':
    main()
