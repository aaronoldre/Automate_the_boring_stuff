import bs4
import requests


def getAmazonPrice(productURL):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    res = requests.get(productURL, headers = headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # add try and except
    # elems = soup.select('#buyNew_cbb > div:nth-child(1) > div:nth-child(2)')
    # print(elems)
    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/')
print('The price is ' + price)

# look at weather.gov
# pull weather from all climbing areas for upcoming weekend?
# pull images from xkcd

