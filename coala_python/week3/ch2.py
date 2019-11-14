# 컨테이너 tr.athing
# 순위 tr.athing span.rank
# 제목 tr.athing a.storylink

import requests
from bs4 import BeautifulSoup

for n in range(1, 4):
    raw = requests.get("https://news.ycombinator.com/news?p="+str(n))\
        # ,
                       # headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("tr.athing")

    for ar in articles:
        rank = ar.select_one("span.rank").text
        title = ar.select_one("a.storylink").text

        print(rank, title)
