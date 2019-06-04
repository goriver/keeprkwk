import requests
from bs4 import BeautifulSoup
import re


class ScolarObj:
    def __init__(self, title,writer, date, depart, attach, attach_link, article_image, article_text):
        # article_text
        # 파이썬 생성자
        self.title = title
        self.writer = writer
        self.date = date
        self.depart = depart
        self.attach = attach
        self.attach_link = attach_link
        self.article_image = article_image
        self.article_text = article_text



class ScolarCrawling:
    # 학교 사이트의 url을 불러온다



    req = requests.get('https://www.kookmin.ac.kr/site/resource/board/scholarship/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_lists = soup.select(
        'td > a'
    )
    scolarDetail=[]
    for list in my_lists:
        # 세부 내용 긁어오기
        url = 'https://www.kookmin.ac.kr/site/resource/board/scholarship/' + list.get('href')
        tmp_html = requests.get(url)
        html = tmp_html.text
        tmp_soup = BeautifulSoup(html, 'html.parser')
        # boardview class
        board = tmp_soup.find("div", {"class": "boardview"})
        # 장학 공지사항 제목
        title = tmp_soup.find(id='article_title')

        tmp_title = title.text

        # 장학 공지사항 글쓴이
        writer = board.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-child(1) > td:nth-child(4) > span'
        )
        for w in writer:
            tmp_writer =w.text
        # 장학 공지사항 날짜
        date = tmp_soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-child(2) > td:nth-child(2)'
        )
        for d in date:
            tmp_date =d.text
        # 장학 공지사항 부서
        depart = tmp_soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-child(3) > td:nth-child(2)'
        )
        for de in depart:
            tmp_depart=de.text
        #장학 공지사항 첨부파일
        attach = tmp_soup.select(
            '#content_body > section > div.boardview > table > tbody > tr:nth-child(4) > td > a'
        )
        tmp_attach = []
        tmp_attach_link=[]
        for at in attach:
            tmp_attach.append(at.text)
            tmp_attach_link.append(at.get('href'))


        # 장학 공지사항 내용
        articles = tmp_soup.find(id='view-detail-data')
        # 내용 이미지 담아놓는 tmp_article_image
        article = articles.select('#view-detail-data > p > img')
        for art_image in article:
            tmp_article_image = art_image
            # tmp_article_image +=arti_image로 하면 오류


        # 내용 켁스트 담아놓는 tmp_
        contents = str(articles.find_all("p"))
        contents = re.sub('<.+?>', '', contents, 0).strip()
        tmp_article_text=[]
        for content in contents:
            tmp_article_text += content




        em = ScolarObj(tmp_title, tmp_writer, tmp_date, tmp_depart, tmp_attach, tmp_attach_link, tmp_article_image, tmp_article_text)
        scolarDetail.append(em)

    for detail in scolarDetail:
        print("{}".format(detail.article_text))