import wikipedia


def query(query: str, lang: str = "en"):
    wikipedia.set_lang(lang)

    res = wikipedia.search(query, results=1)
    if len(res) == 0:
        return "No search results."
    try:
        wikipedia_page = wikipedia.page(res[0], auto_suggest=False)
    except wikipedia.PageError:
        return f"Unable to load page {res[0]}."
    content = wikipedia_page.content

    return content
