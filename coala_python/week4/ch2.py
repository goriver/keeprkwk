# "검색어"열을 추가합니다.
# 파일의 헤더위치에 "검색어" 카테고리를 추가합니다.
# "검색어" 카테고리에 입력한 키워드를 저장해줍니다.
# *Stage4에서 완성한 수집기 프로그램은 데이터가 누적되어 저장되므로 작동확인을 위해서
# 기존의 엑셀 파일을 삭제한 후 실행해주셔야합니다.


import requests
from bs4 import BeautifulSoup


# 추가1

# 쓰기버전(w)으로 navernews.csv파일을 연다.
f = open("navernews.csv", "w")
# 데이터의 헤더부분을 입력한다.
f.write("검색어, 제목, 언론사\n")

keyword = input("검색어를 입력해주세요: ")
page = 1
for page in range(1, 4):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query="+keyword +"&start=" + str(page),

                       headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser', from_encoding='utf-8')


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
        f.write(keyword+','+title + ',' + source + '\n')


f.close()
