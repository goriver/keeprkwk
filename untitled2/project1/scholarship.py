import requests
from bs4 import BeautifulSoup
import time



req = requests.get('https://www.kookmin.ac.kr/site/resource/board/scholarship/')

html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    'td > a'
)

# 변수 list에 담기
title_data = []
url_data = []
writer_data = []
date_data = []
depart_data = []
linkTitle_data=[]
linkUrl_data=[]


for title in my_titles:

    # 세부 내용 긁어오기
    url = 'https://www.kookmin.ac.kr/site/resource/board/scholarship/' + title.get('href')
    # url 모으기
    url_data.append(url)
    tmp_html = requests.get(url)
    html = tmp_html.text
    tmp_soup = BeautifulSoup(html, 'html.parser')
    # boardview class
    table = tmp_soup.find("div", {"class": "boardview"})
    # table에서 우리가 원하는 거 찾을 수 있음( 좀 더 축소함'

    article = table.find(id = "#article_title")
    for r in article:
        print(r.text)

    title_data.append('article.text')  # title 모으기


    writer = table.select(
        '#content_body > section > div.boardview > table > tbody > tr:nth-child(1) > td:nth-child(4) > span'
    )
    for wr in writer:
        print(wr)
        writer_data.append('wr.text')  # 글쓴이 모으기

    date = table.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-child(2) > td:nth-child(2)'
    )
    for da in date:
        date_data.append('da.text')  # 작성일 모으기

    depart = table.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-child(3) > td:nth-child(2)'
    )

    for de in depart:
        depart_data.append(de.text)  # 부서




    attach = table.select(
        '#content_body > section > div.boardview > table > tbody > tr:nth-child(4) > td > a'
     )
    for link in attach:
        linkTitle_data.append(link.text)
        linkUrl_data.append(link.get('href'))
    # 24시간 잠들었다가 다시 실행하기
    time.sleep(86400)














