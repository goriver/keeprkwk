import requests
from bs4 import BeautifulSoup

class SchoolNotice:
    def __init__(self, title, writer, date, department, attachment, attachment_link, article_image, article_text):
        self.title = title
        self.writer = writer
        self.date = date
        self.department = department
        self.attachment = attachment
        self.attachment_link = attachment_link
        self.article_image = article_image
        self.article_text = article_text
        # 이 클래스 사실 안으로 넣으라고 했는데 이렇게 선언한 이유는,
        # 홈페이지 모두 같은 요소를 가지고 있어서 각 홈페이지 별로 클래스를 선언하는 것 보다
        # 요렇게 하면 더 효율적이지 않을까하는 생각을 했어요!!
        # 만약 개인적으로 구상했던 부분이 있는데 이게 같이 작동되지 않는다면 바꾸도록 할게요!!
        # 협업을 해야하는데 갠플중인건가요 저 혹시...?ㅠㅠㅠㅠㅠ


class CleanDetailScholarship:
    def clean_scholarship(soup):
        tmp_title = soup.find(id='article_title')
        # 장학 공지사항 글쓴이
        writers = soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-child(1) > td:nth-child(4) > span'
        )
        for writer in writers:
            tmp_writer = writer.text
            # 장학 공지사항 날짜
        dates = soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-child(2) > td:nth-child(2)'
        )
        for date in dates:
            tmp_date = date.text
        # 장학 공지사항 부서
        departments = soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-child(3) > td:nth-child(2)'
        )
        for department in departments:
            tmp_department = department.text
        # 장학 공지사항 첨부파일
        attachments = soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-child(4) > td > a'
        )
        tmp_attachment = []
        tmp_attachment_link = []
        for attachment in attachments:
            tmp_attachment.append(attachment.text)
            tmp_attachment_link.append(attachment.get('href'))
        # 장학 공지사항 내용
        articles = soup.find(id='view-detail-data')
        # 세부 내용 이미지 담아놓는 tmp_article_image
        article = articles.select('#view-detail-data > p > img')
        tmp_article_image = []
        for art_image in article:
            tmp_article_image = art_image
        content = soup.find(id='view-detail-data').text
        em = soup.__init__(tmp_title, tmp_writer, tmp_date, tmp_department,
                           tmp_attachment, tmp_attachment_link, tmp_article_image, content)


class CrawlingNotice:
    def __init__(self, url):
        self.url = url


    if(url == 'https://www.kookmin.ac.kr/site/resource/board/academic/'):
       print('ok')



    if(url.text):


        def academic_crawling(url):
        def special_lecture_crawling(url):
        def scholar_crawling(url)::
            for i in range(1, 57):
                base_url = url
                page_url = base_url.format(i - 1)
                req = requests.get(page_url)
                html = req.text
                soup = BeautifulSoup(html, 'html.parser')
                scholar_notices = soup.select(
                    'td > a'
                )
                for scholar in scholar_notices:
                    # 세부 내용 긁어오기
                    url = 'https://www.kookmin.ac.kr/site/resource/board/scholarship/' + scholar.get('href')
                    tmp_html = requests.get(url)
                    html = tmp_html.text
                    tmp_soup = BeautifulSoup(html, 'html.parser')
                    # school_scholarship.append(ScholarshipNotice.clean_crawling(tmp_soup))
                    #
        def






class WepPage:
    school_academic = []
    school_special_lecture = []
    school_scholarship = []
    url_basic = 'https://www.kookmin.ac.kr/site/resource/board/{}'
    academic_basic = url_basic.format('special_lecture/?&pn={}')
    special_lecture_basic = url_basic.format('academic/?&pn={}')
    scholarship_basic = url_basic.format('scholarship/?&pn={}')
    school_scholarship = CrawlingNotice.__init__(scholarship_basic)


# url 구분하는 로직 짜기
# 각 url 별로 나와야 하는 부분 추출하기
# 나온 부분 각각 obj 이용해서 list에 담기