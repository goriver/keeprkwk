import requests
from bs4 import BeautifulSoup


# 컨테이너 없이 데이터 수집하기
html = requests.get("https://tv.naver.com/r")
soup = BeautifulSoup(html.text, "html.parser")
# video = html.select("div.inner")

titles = soup.select("dt.title")

for title in titles:
    print(title.text.strip())
print("="*50)

chanels = soup.select("dd.chn")
for ch in chanels:
    print(ch.text.strip())
print("="*50)
hits = soup.select("spna.hit")
for hit in hits:
    print(ch.text.strip())
print("="*50)

likes = soup.select("span.like")
for like in likes:
    print(like.text.strip())

print("="*50)
