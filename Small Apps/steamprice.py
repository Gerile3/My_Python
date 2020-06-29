import requests
from bs4 import BeautifulSoup
import re


def check_price(word):
    """Checks price and bunch of other infos for a given game name"""
    info = {}
    url = "https://www.steamprices.com/us/search/?q=" + word + "&p=1"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
                                          'Accept': 'text/css,*/*;q=0.1',
                                          'Accept-Language': 'en-GB,en;q=0.5',
                                          'Accept-Encoding': 'gzip, deflate, br',
                                          'DNT': '1',
                                          'Connection': 'keep-alive'})
    soup = BeautifulSoup(response.content, "lxml")

    if response.status_code == 200:
        result = soup.find("div", class_="details")
        summary = soup.find("div", class_="summary")

        pic = result.find('img', class_="lazy")['data-original']
        title = result.find('h4', class_="title").text
        try:
            price = result.find("td", class_="price_curent").text
        except AttributeError:
            price = "Free"
        try:
            meta_note = summary.find("a")["data-original-title"]
            user_note = summary.find_all("a")[1]["data-original-title"]
        except TypeError:
            meta_note = "None"
            user_note = "None"

        gtype = summary.find("div", class_="pull-right").text
        date = summary.find(
            "div", class_="pull-right").span["data-original-title"]
        date = re.sub(r'<em>|</em>|<br />|<sup>|nd|</sup>', '', date)

        info.update({'Picture': pic, 'Title': title, 'Price': price,
                     'UserNote': user_note, 'MetaNote': meta_note, 'GameType': gtype, 'Date': date})

        return info


if __name__ == "__main__":
    game = check_price("dishonored")
    print(game)
