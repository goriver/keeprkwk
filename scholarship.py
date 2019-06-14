import requests
from bs4 import BeautifulSoup


class InstanceOfHomepage:
    def scholar_notice(self, title, writer, date, depart, attach, attach_link, article_image, article_text):
        # 공지사항 인스턴스
        # 여기는 처음에 동현님이 말씀해주신 부분이랑 약간 달라욤...
        # 왜냐하면 홈페이지 코드를 자세히 보닌깐 boardview 부분은 다 똑같은 항목을 출력해야 하더라고요...!!
        # 그래서 제가 상속이나 이런거 쓸 실력이 되지는 못해서 해결책으로 이렇게 해봤어요!!
        # 변수도 obj이렇게 쓰지 말라고 하셨는데 instance라고 일단은 익숙해지려고 써놨어요! 최종 제출할때는 수정할게욤
        self.title = title
        self.writer = writer
        self.date = date
        self.depart = depart
        self.attach = attach
        self.attach_link = attach_link
        self.article_image = article_image
        self.article_text = article_text


class CleanHomepage:
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
        school_scholar = InstanceOfHomepage()
        em_scholarship = school_scholar.scholar_notice\
                        (tmp_title, tmp_writer, tmp_date, tmp_depart, \
                         tmp_attach, tmp_attach_link, tmp_article_image, content)
        return em_scholarship
    # print했을때 none이긴 하지만, 출력이 되긴 됨


class WebCrawling():
    def website_crawling(self, school_url):# 학교 사이트의 url을 불러온다.
        crawling_scholar = []
        # >>>> 출력이 되는거 확인되면 해야할 것
        # if(school_url == 'https://www.kookmin.ac.kr/site/resource/board/scholarship/'):
        #     for i in range(각각 마지막 페이지)로 하는 함수 호출하기
        # elif(school_url == 'https://www.kookmin.ac.kr/site/resource/board/academic/'):
        #     함수
        # elif(school_url == 'https://www.kookmin.ac.kr/site/resource/board/special_lecture/'):
        #     함수
        for i in range(1,57):
            base_url = school_url +'?&pn={}'
            page_url = base_url.format(i - 1)
            req = requests.get(page_url)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            notices = soup.select(
                'td > a'
            )
            # 세부 내용 긁어오기
            for notice in notices:
                url = school_url + notice.get('href')
                tmp_html = requests.get(url)
                html = tmp_html.text
                tmp_soup = BeautifulSoup(html, 'html.parser')
                scholarship = CleanHomepage()
                tmp_scholar=scholarship.clean_crawling(tmp_soup)
                # em_scholarship
                crawling_scholar.append(tmp_scholar)
        for detail in crawling_scholar:
            print("{}".format(detail.title))
        #return crawling_scholar


crawling_scholarship = WebCrawling()
scholarship_url = 'https://www.kookmin.ac.kr/site/resource/board/scholarship/'
academic_url = 'https://www.kookmin.ac.kr/site/resource/board/academic/'
special_lecture = 'https://www.kookmin.ac.kr/site/resource/board/special_lecture/'
scholar_detail = crawling_scholarship.website_crawling(academic_url)
#                 crawling_scholar이 들어옴
# for detail in crawling_scholarship:
#     print("{}".format(detail.title))
