import requests
import wikipedia
import pywhatkit


def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results



def search_on_google(query):
    pywhatkit.search(query)


def youtube(video):
    pywhatkit.playonyt(video)


def get_news():
    news_headline = []
    result = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey"
                          f"=f30cff34200c4ff29abb9bc3e84d7798").json()
    articles = result["articles"]
    for article in articles:
        news_headline.append(article["title"])
    return news_headline[:6]


