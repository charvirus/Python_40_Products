from bs4 import BeautifulSoup
import cloudscraper


def get_exchange_rate(target1, target2):
    # url = "https://kr.investing.com/currencies/{}-{}".format(target1, target2)
    # res = requests.get(url, headers=headers)
    # content = BeautifulSoup(response.content, 'html.parser')
    # containers = content.find('span', {'data-test': 'instrument-price-last'})
    # print(res.text)

    url_base = "https://kr.investing.com/currencies/{}-{}".format(target1, target2)

    scraper = cloudscraper.create_scraper()
    html = scraper.get(url_base).content
    soup = BeautifulSoup(html, 'html.parser')
    dollar = soup.find('span', {'data-test': 'instrument-price-last'})
    print(dollar.text)


get_exchange_rate('usd', 'krw')