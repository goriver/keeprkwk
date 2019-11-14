import requests
from bs4 import BeautifulSoup

# format을 활용한 bs4
for i in range(1, 57):
    base_url = 'https://www.kookmin.ac.kr/site/resource/board/scholarship/?&pn={}'
    page_url = base_url.format(i - 1)
    req = requests.get(page_url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    tmp = soup.select('td>a')
    tmp = str(tmp)
    print(tmp)

