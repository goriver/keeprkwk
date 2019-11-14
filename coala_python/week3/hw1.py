import requests
from bs4 import BeautifulSoup
# 컨테이너, 제목, 저자를 선택하는 선택자를 찾아냅니다.
# 파이썬을 활용해서 데이터 수집기를 만들어냅니다.
# (심화)1-20위, 21-40위, ... , 81-100위 서적을 모두 수집할 수 있는 요청값을 찾아 수집기를 만들어 냅니다.
titles = []
writers = []
for n in range(1, 6):
    html = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(n),
                        headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(html.text, 'html.parser')


    books = soup.select("div.lst_thum_wrap li") # 컨테이너

    for book in books:
        title = book.select_one("div.lst_thum_wrap li a strong").text.strip()
        writer = book.select_one("div.lst_thum_wrap li span.writer").text.strip()


        titles.append(title)
        writers.append(writer)

for i in titles:
    print(i)

print("="*50)
for j in writers:
    print(j)




