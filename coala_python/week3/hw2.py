import requests
from bs4 import BeautifulSoup

for n in range(1, 4):
    # p=1, p=2, p=3으로 반복해준다.
    raw = requests.get("https://search.daum.net/search?nil_suggest=btn&w=news&DA=PGD&cluster=y&q=%EC%BD%94%EC%95%8C%EB%9D%BC&p="+str(n))
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("div.cont_inner")

    for ar in articles:
        title = ar.select_one("a.f_link_b").text
        summary = ar.select_one("p.f_eb.desc").text

        print("제목 : ",title," \n 기사요약 : ", summary)
