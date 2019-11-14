import requests
from bs4 import BeautifulSoup


# 추가1

# 쓰기버전(w)으로 navernews.csv파일을 연다.
f = open("navernews.csv", "w")
# 데이터의 헤더부분을 입력한다.
f.write("제목, 언론사\n")

page = 1
for page in range(1, 4):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=코알라&start=" + str(page),
                       headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    # 컨테이너: ul.type01 > li
    # 기사제목: a._sp_each_title
    # 언론사: span._sp_each_source

    # 1. 컨테이너 수집
    articles = html.select("ul.type01 > li")

    # 2. 기사 데이터 수집

    for ar in articles:
        title = ar.select_one("a._sp_each_title").text
        source = ar.select_one("span._sp_each_source").text

        title = title.replace(",", "")
        source = source.replace(",", "")

        # 제목(title)과 언론사(source)를 ,로 구분하여 써줍니다.
        f.write(title + ',' + source + '\n')


f.close()
