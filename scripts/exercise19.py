import requests
from bs4 import BeautifulSoup

'''
For this one I feel the need to leave some comments because web structures, as
I refered on exercise 17, changed a bit since the creation of the exercises.

On this exercise, I am basically going through the DOM hierarchy by creating
different parsers for each level. I was not able to find a quick way to do it
by other means .

Also, this was not rocket science, I just went through the website code and
analyzed where the article content was so I could come up with a strategy to
get to it, so there where the code in getContent(pageCode) comes from:
1- first the main content div
2- Then each of the content sections inside that div
3- Finally each of the paragraphs inside the sections

I am still getting one last line that was not supposed to, but I did not find
a quick and elegant way to get rid of it in the time I had to do this exercise
in the evening.

'''

def getPage():
    html = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture").text
    return html


def getContent(pageCode):
    pageParser = BeautifulSoup(pageCode, "html.parser")
    contentDiv = pageParser.find_all('div', class_='content')

    divParser = BeautifulSoup(str(contentDiv), "html.parser")
    contentSections = divParser.find_all('section', class_='content-section')

    paragraphParser = BeautifulSoup(str(contentSections), "html.parser")
    paragraphs = paragraphParser.find_all('p')

    text = [p.text for p in paragraphs]
    return text


def main():
        page = getPage()
        text = getContent(page)
        print("\n".join(text))


main()
