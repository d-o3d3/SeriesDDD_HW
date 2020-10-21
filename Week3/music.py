import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

tr_list = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in tr_list:
    rank = tr.select_one('td.number').text.split('\n')[0]
    title = tr.select_one('.info > a.title.ellipsis').text.strip()
    singer = tr.select_one(' td.info > a.artist.ellipsis').text
    print(rank, title, singer)
