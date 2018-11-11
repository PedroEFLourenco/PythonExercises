import requests
from bs4 import BeautifulSoup

'''
For this one I feel the need to leave some comments because NYT website has
changed a lot since Python Practice created this exercise, and their solution
is no longer quite up to par with the reality

So, we are doing the hardwork in getTitles(pageCode):
    - get all HTML elements with the tag "article"
    - then going to the h2 inside those elements, if existing and get the text,
      corresponding to the article's title.

This is not a bulletproof solution. I came to this solution basically from
looking into the website and trying to find an acceptable solution

Tried many things:
* going for all <span> elements -> gave a lot of gargabe not related to
                                   articles
* going for <span> elements with class="balancedHeadline" -> weirdly returned
                                                             nothing
* going for all <h2> elements -> Almost acceptable since, from what I saw in a
                                glimpse, every title is in a h2 element
                                but still some garbage.


Finally, since they use the <article> element, I guessed going for those
elements would fit the exercise definition and went for it.
Which doesn't mean that when you look at this it is not already outdated
as the "official" solution is today :D

'''


def getPage():
    html = requests.get("https://www.nytimes.com/").text
    return html


def getTitles(pageCode):
    htmlParser = BeautifulSoup(pageCode, "html.parser")
    articles = htmlParser.find_all('article')
    titles = [article.h2.text for article in articles
              if article.h2 is not None]
    return titles


def main():
        page = getPage()
        titles = getTitles(page)
        print("\n".join(titles))


main()
