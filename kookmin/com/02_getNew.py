import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# selenium 이용해서 자동으로 웹사이트 접속하도록 만들고
# 60초마다 재 접속하도록 하기
# getNew.py에 접속해서 __init__ 함수를 이용해서 scolarDetail[]안에 다 넣기
# -> 상속 공부하기
# 근데 같은 파일 다른 패키지(맞나요? 이클립스에서는 그냥 클래스인데 파이참은 처음이라) 상속 가능한가요?
# 물어볼 것
# 1. 파이썬 자바의 인터페이스 OR 다형성 처럼 링크 받아서 각각 저장 가능한가(공식 문서에는 객체지향 언어라고 하긴 하던데용)

# 2. 게시판 목록을 저장할 것이라면 장고를 이용하면 되는 것인가??
# -> jsp에서는 my-sql만 사용해서 해봤...어요!!

# 3. SELENIUM을 이용해서 60초 마다 업데이트 할때 while을 이용하면 되는것인가?
# -> 인터넷에서는 공간을 많이 차지해서 나쁜 방법이라고 하던뎅
# 4. 결정적으로 로딩이 매우 느림...ㅠㅠ

class __name__ == '__main__':
# 이거 main 맞낭...?
    while:
        driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application')

        driver.implicitly_wait(3)

        for i in range(57):
        base_url = 'https://www.kookmin.ac.kr/site/resource/board/scholarship/?&pn={}'
        page_url = base_url.format(i + 1 - 1)
        req = driver.get(page_url) #<- 변동
        req.encoding = 'utf-8'
        html =req.text
        soup = BeautifulSoup(html, 'html.parser')
        my_lists = soup.select(
            'td > a'
        )

        ScolarCrawling.getDetail(my_lists)
        # 여기서 안전하게 getHomepage로 이동해서 저장시키는게 목표입니당!
        time.sleep(3600)
# 1시간 잠들고 다시 실행


