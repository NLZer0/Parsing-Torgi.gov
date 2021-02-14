import requests
from bs4 import BeautifulSoup

URL = 'https://bets-dota2.com/'
URL_JS = 'https://bets-dota2.com/scripts/bets.js?1606420992'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 YaBrowser/20.12.3.140 Yowser/2.5 Safari/537.36',
    'accept': '*/*',
    'cookie': '__cfduid=d223292203988e51003f2d34fb50731351612891726; language=ru; _ga=GA1.2.1411998921.1612891730; _gid=GA1.2.471912967.1612891730; _ym_uid=1612891732239255810; _ym_d=1612891732; _ym_isad=1; page-tab=3; d2mid=jslpcc2mrDb2lO2KPMyvZwM43lApOu; dark_theme=0; timezone=+0500; PHPSESSID=shigv3anavs35in0uhm70s62pd; cf_clearance=541679f727a65451585687cac2f04f70f2b47383-1612944750-0-150; chat-opened=1; _gat=1; chat-position-top=534px; _ym_visorc=w'
}


def get_html(url, params = None):
    r = requests.get(url, headers = HEADERS, params=params)
    r2 = requests.get(URL_JS, headers = HEADERS, params=params)
    return (r,r2)

def get_content(html): 
    soup = BeautifulSoup(html,'html.parser')
    print(html)


def parse():
    html, html_js = get_html(URL)
    if html.status_code == 200:
        get_content(html_js.text)
    else:
        print('Не удалось открыть сайт', html.status_code)

parse()

