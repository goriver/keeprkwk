import requests
from bs4 import BeautifulSoup


class Scholarship:
    def scholar_notices(self, title, writer, date, depart, attach, attach_link, article_image, article_text):
        # 공지사항 객체
        self.title = title
        self.writer = writer
        self.date = date
        self.depart = depart
        self.attach = attach
        self.attach_link = attach_link
        self.article_image = article_image
        self.article_text = article_text

    def clean_crawling(self, board_detail, tmp_soup):
        # 장학 공지사항 제목
        title = tmp_soup.find(id='article_title')
        tmp_title = title.text

        # 장학 공지사항 글쓴이
        writer = board_detail.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-child(1) > td:nth-child(4) > span'
        )
        for w in writer:
            tmp_writer = w.text
        # 장학 공지사항 날짜
        date = tmp_soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-child(2) > td:nth-child(2)'
        )
        for d in date:
            tmp_date = d.text
        # 장학 공지사항 부서
        depart = tmp_soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-child(3) > td:nth-child(2)'
        )
        for de in depart:
            tmp_depart = de.text
        # 장학 공지사항 첨부파일
        attach = tmp_soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-child(4) > td > a'
        )
        tmp_attach = []
        tmp_attach_link = []
        for at in attach:
            tmp_attach.append(at.text)
            tmp_attach_link.append(at.get('href'))
        # 장학 공지사항 내용
        articles = tmp_soup.find(id='view-detail-data')
        # 세부 내용 이미지 담아놓는 tmp_article_image
        article = articles.select('#view-detail-data > p > img')
        tmp_article_image = []
        for art_image in article:
            tmp_article_image = art_image

        content = tmp_soup.find(id='view-detail-data').text

        tmp_ary = Scholarship.scholar_notices(tmp_title, tmp_writer, tmp_date, tmp_depart, tmp_attach,
                                       tmp_attach_link, tmp_article_image, content)
        return tmp_ary

class WebCrawling():
    def __init__(self):
        pass

    def website_crawling(self):# 학교 사이트의 url을 불러온다.
        school_scholar = []
        for i in range(1,57):
            base_url = 'https://www.kookmin.ac.kr/site/resource/board/scholarship/?&pn={}'
            page_url = base_url.format(i - 1)
            req = requests.get(page_url)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            notices = soup.select(
                'td > a'
            )
            for notice in notices:
            # 세부 내용 긁어오기
                url = 'https://www.kookmin.ac.kr/site/resource/board/scholarship/' + notice.get('href')
                tmp_html = requests.get(url)
                html = tmp_html.text
                tmp_soup = BeautifulSoup(html, 'html.parser')
                # boardview class
                board = tmp_soup.find("div", {"class": "boardview"})
                # 공지사항 각 객체에 넣는 함수 호출하기

                em_scholar = scholarship.clean_crawling(board, tmp_soup)
                school_scholar.append(em_scholar)
        return school_scholar



scholar_detail = WebCrawling.website_crawling()
for detail in scholar_detail:
    print("{}".format(detail.article))
    # 문제점. 함수 호출이 안됨 ( 매개변수 self를 넣었는데 그게 문제인가요...?)
    # Traceback (most recent call last):
    #   File "C:/Users/NoteBook/PycharmProjects/untitled2/project1/include_Article.py", line 95, in <module>
    #     scholar_detail = WebCrawling.website_crawling(url)
    # TypeError: website_crawling() missing 1 required positional argument: 'base_url'