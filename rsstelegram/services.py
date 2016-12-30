import requests
import pdb
import unicodedata
from BeautifulSoup import BeautifulSoup

title = ''
newsurl = ''
BOT_TOKEN = '279362931:AAFGHxfBSav_KFlLEshwwPKuAr24Wq7IlAc'


def get3DJuegos():
    global title
    global newsurl

    url = 'http://www.3djuegos.com/universo/rss/rss.php?plats=1-2-3-4-5-6-7-34&tipos=noticia-analisis-avance-video-imagenes-demo&fotos=no'
    req = requests.get(url)
    soup = BeautifulSoup(''.join(req.content))
    soup = soup.contents[2].contents[1]
    data = {}
    if title != soup.item.title.string:
        title = soup.item.title.string
        newsurl = soup.item.contents[4].string
        data = {'title': title, 'newsurl': newsurl}
        return data
    return data


def sendTelegram(data):
    global BOT_TOKEN

    title = unicodedata.normalize('NFKD', data.get('title')).encode('ascii','ignore')
    link = unicodedata.normalize('NFKD', data.get('newsurl')).encode('ascii','ignore')
    mens = link
    url = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage'
    params = {'chat_id': 283391783, 'text': mens}
    req = requests.post(url, params=params)
