import requests
from bs4 import BeautifulSoup


class Scholarship:

    def __init__(self):
        pass

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
        return self

    def show_detail_data(self):
        print("제목 : " + self.title)
        print("글쓴이 : " + self.writer)
        print("날짜 : " + self.date)
        print("부서 : " + self.depart)
        print("첨부 : " + str(self.attach))
        print("첨부이미지 : " + str(self.attach_link))
        print("본문 : " + str(self.article_image))
        print("본문내용 : " + self.article_text)
        print()

    def clean_crawling(self, tmp_soup):

        # 장학 공지사항 제목
        title = tmp_soup.find(id='article_title')
        tmp_title = title.text

        # 장학 공지사항 글쓴이
        writer = tmp_soup.find(class_="writer-wrap")
        tmp_writer = writer.text.strip()

        # 장학 공지사항 날짜
        date = tmp_soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-of-type(2) > td:nth-of-type(1)'
        )

        for d in date:
            tmp_date = d.text

        # 장학 공지사항 부서
        depart = tmp_soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-of-type(3) > td:nth-of-type(1)'
        )
        for de in depart:
            tmp_depart = de.text

        # 장학 공지사항 첨부파일
        attach = tmp_soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-of-type(4) > td > a'
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

        tmp_ary = self.scholar_notices(title=tmp_title, writer=tmp_writer, date=tmp_date, depart=tmp_depart,
                                       attach=tmp_attach,
                                       attach_link=tmp_attach_link, article_image=tmp_article_image,
                                       article_text=content)
        return tmp_ary


class WebCrawling:
    def __init__(self):
        pass

    def website_crawling(self):  # 학교 사이트의 url을 불러온다.
        school_scholar = []
        for i in range(1, 2):
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
                # 객체 생성 없이 호출하는 부분 수정
                scholarship = Scholarship()
                em_scholar = scholarship.clean_crawling(tmp_soup)
                school_scholar.append(em_scholar)
        return school_scholar


# 객체 생성 없이 호출하는 부분 수정
webCrawling = WebCrawling()
scholar_detail = webCrawling.website_crawling()

for detail in scholar_detail:
    detail.show_detail_data()