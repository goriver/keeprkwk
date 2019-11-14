import requests

from bs4 import BeautifulSoup


class GetCleanedData:

    def __init__(self):
        pass

    def school_notices(self, title, writer, date, depart, attach, attach_link, article_image, article_text):
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
        print(self.title)
        print(self.writer)
        print(self.date)
        print(self.depart)
        print(str(self.attach))
        print(str(self.attach_link))
        print(str(self.article_image))
        print(self.article_text)
        print('--------------------------------------------------------------')

    def clean_crawling(self, tmp_soup, category_num):
        tmp_category = category_num

        # 장학 공지사항 제목
        title = tmp_soup.find(id='article_title')
        tmp_title = title.text

        # 장학 공지사항 글쓴이
        writer = tmp_soup.find(class_="writer-wrap")
        tmp_writer = writer.text.strip()

        # 장학 공지사항 날짜
        dates= tmp_soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-of-type(2) > td:nth-of-type(1)'
        )

        for date in dates:
            tmp_date = date.text

        # 장학 공지사항 부서
        departments = tmp_soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-of-type(3) > td:nth-of-type(1)'
        )
        for department in departments:
            tmp_depart = department.text

        # 장학 공지사항 첨부파일
        # -- 비어도 이미 빈 파일 선언됨
        attachments = tmp_soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-of-type(4) > td > a'
        )
        tmp_attach = []
        tmp_attach_link = []
        for attach in attachments:
            tmp_attach.append(attach.text)
            tmp_attach_link.append(attach.get('href'))

        article_board = tmp_soup.find(id='view-detail-data')
        # article_board = tmp_soup.select('#view-detail-data')
        # 세부 내용 이미지 담아놓는 tmp_article_image
        article = article_board.select('#view-detail-data > p > img')
        tmp_article_image = []
        for art_image in article:
            tmp_article_image = art_image
        content = tmp_soup.find(id='view-detail-data').text
        if(len(content)==0): # null이면 is not null 대신 씀
            content = ''

        tmp_ary = self.school_notices(title=tmp_title, writer=tmp_writer, date=tmp_date, depart=tmp_depart,
                                       attach=tmp_attach, attach_link=tmp_attach_link,
                                       article_image=tmp_article_image, article_text=content)
        return tmp_ary



class WebCrawling:
    def __init__(self):
        pass

    def website_crawling(self, tmp_url):  # 학교 사이트의 url을 불러온다.

        page_num = 0
        category_num = 0
        if(tmp_url == 'https://www.kookmin.ac.kr/site/resource/board/academic/'):
            page_num = 65
            category_num = 1 # 학사공지
        elif(tmp_url == 'https://www.kookmin.ac.kr/site/resource/board/special_lecture/'):
            page_num = 24
            category_num = 2 # 특강공지
        elif(tmp_url == 'https://www.kookmin.ac.kr/site/resource/board/scholarship/'):
            page_num = 58
            category_num = 0 # 장학공지
        for i in range(1, page_num):
            # base_url = tmp_url + '?&pn={}'
            #             # page_url = f'base'
            #             # # this_page = i-1
            #             # # page_url = f'base_url {this_page}'
            #             # # print(page_url)
            base_url = tmp_url + '?&pn={}'
            page_url = base_url.format(i - 1)
            req = requests.get(page_url)

            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            notices = soup.select(
                'td > a'
            )
            school_scholar = []
            for notice in notices:
                # 세부 내용 긁어오기
                url = tmp_url + notice.get('href')
                tmp_html = requests.get(url)
                html = tmp_html.text
                tmp_soup = BeautifulSoup(html, 'html.parser')
#-------------------------코드 수정부분---------------------------------
                school_data = GetCleanedData()
                em_scholar = school_data.clean_crawling(tmp_soup, category_num)

                notice_data = { "author" : em_scholar.writer,
                                "category" : category_num,
                                "origin_url" : page_url,
                                "title" : em_scholar.title,
                                "content" : em_scholar.article_text}
#------------------------ 값 수정하는 방법 이용 ------------------
                if( '이 필드는 blank일 수 없습니다.' in notice_data.values()):
                # if(notice_data.values() == None):
                     notice_data['content'] = em_scholar.article_image



                response = requests.post('https://kmuin.com/api/v1/notices/', data=notice_data)
                response.encoding = 'utf-8'
                print(response.json())

        #return response.json()

academic_url = 'https://www.kookmin.ac.kr/site/resource/board/academic/'
special_lecture_url = 'https://www.kookmin.ac.kr/site/resource/board/special_lecture/'
scholarship_url = 'https://www.kookmin.ac.kr/site/resource/board/scholarship/'
webCrawling = WebCrawling()
scholar_detail = webCrawling.website_crawling(academic_url)
