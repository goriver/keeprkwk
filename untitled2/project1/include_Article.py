import requests
from bs4 import BeautifulSoup


class Scholarship:
    def __init__(self, title, writer, date, depart, attach, attach_link, article_image, article_text):
        # 공지사항 인스턴스
        self.title = title
        self.writer = writer
        self.date = date
        self.depart = depart
        self.attach = attach
        self.attach_link = attach_link
        self.article_image = article_image
        self.article_text = article_text

    def clean_crawling(self, tmp_soup):
        # 장학 공지사항 제목
        title = tmp_soup.find(id='article_title')
        tmp_title = title.text
        # 장학 공지사항 글쓴이

        writers = tmp_soup.select('#content_body > section > div.boardview > table > '
                                  'tbody > tr:nth-child(1) > td:nth-child(4) > span')
        for writer in writers:
            tmp_writer = writer.text
        # 장학 공지사항 날짜
        dates = tmp_soup.select('#content_body > section > div.boardview > table > '
                                'tbody > tr:nth-child(2) > td:nth-child(2)')
        for date in dates:
            tmp_date = date.text
        # 장학 공지사항 부서
        departments = tmp_soup.select('#content_body > section > div.boardview > table > '
                                      'tbody > tr:nth-child(3) > td:nth-child(2)')
        for department in departments:
            tmp_depart = department.text
        # 장학 공지사항 첨부파일
        attachments = tmp_soup.select('#content_body > section > div.boardview > table > '
                                      'tbody > tr:nth-child(4) > td > a')
        tmp_attach = []
        tmp_attach_link = []
        for attachment in attachments:
            tmp_attach.append(attachment.text)
            tmp_attach_link.append(attachment.get('href'))
        # 장학 공지사항 내용
        articles = tmp_soup.find(id='view-detail-data')
        # 세부 내용 이미지 담아놓는 tmp_article_image
        articles = articles.select('#view-detail-data > p > img')
        tmp_article_image = []
        for article_image in articles:
            tmp_article_image = article_image
        # 세부 내용 text
        content = tmp_soup.find(id='view-detail-data').text
        school_scholar = Scholarship()
        em_scholarship = school_scholar.__init__(tmp_title, tmp_writer, tmp_date, tmp_depart, tmp_attach, tmp_attach_link, tmp_article_image, content)
        return em_scholarship


class WebCrawling():
    def __init__(self):
        pass

    def website_crawling(self):# 학교 사이트의 url을 불러온다.
        crawling_scholar = []
        for i in range(1,57):
            #base_url = 'https://www.kookmin.ac.kr/site/resource/board/scholarship/'+'?&pn={}'
            base_url = 'https://www.kookmin.ac.kr/site/resource/board/scholarship/?&pn={}'
            page_url = base_url.format(i - 1)
            req = requests.get(page_url)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            notices = soup.select(
                'td > a'
            )

            # 세부 내용 긁어오기
            for notice in notices:
                url = 'https://www.kookmin.ac.kr/site/resource/board/scholarship/' + notice.get('href')
                tmp_html = requests.get(url)
                html = tmp_html.text
                tmp_soup = BeautifulSoup(html, 'html.parser')
                scholarship = Scholarship()
                crawling_scholar.append(scholarship.clean_crawling(tmp_soup))
                # crawling_scholar 리스트에 값 넣기

        return crawling_scholar


crawling_scholarship = WebCrawling()
scholar_detail = crawling_scholarship.website_crawling()
for detail in scholar_detail:
    print("{}".format(detail.title))
