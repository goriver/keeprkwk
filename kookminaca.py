import requests
from bs4 import BeautifulSoup

class ScolarObj:
    def __init__(self, article, writer, date, depart, attach, attach_link):
        # 파이썬 생성자
        self.article = article
        self.writer = writer
        self.date = date
        self.depart = depart
        self.attach = attach
        self.attach_link = attach_link



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
        article = tmp_soup.find(id='article_title')

        tmp_article = article.text  ##

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

        em = ScolarObj( tmp_article, tmp_writer, tmp_date, tmp_depart, tmp_attach, tmp_attach_link)
        scolarDetail.append(em)

    print(scolarDetail)
   #[<__main__.ScolarObj object at 0x03312F10>, <__main__.ScolarObj object at 0x035FCC70>, <__main__.ScolarObj object at 0x03319390>, <__main__.ScolarObj object at 0x036053F0>, <__main__.ScolarObj object at 0x03319DB0>, <__main__.ScolarObj object at 0x035EB9F0>, <__main__.ScolarObj object at 0x03312BF0>, <__main__.ScolarObj object at 0x033BAA50>, <__main__.ScolarObj object at 0x0338E570>, <__main__.ScolarObj object at 0x0403BED0>, <__main__.ScolarObj object at 0x03F6CA30>, <__main__.ScolarObj object at 0x04043610>, <__main__.ScolarObj object at 0x042BBCF0>, <__main__.ScolarObj object at 0x041E9AF0>, <__main__.ScolarObj object at 0x04479F30>, <__main__.ScolarObj object at 0x0330EE50>, <__main__.ScolarObj object at 0x0447C670>]


    # 왜 이렇게 출력이 되죵,,,,,
    # 그리고 list로 담아둔 것들을 그냥 파일로 저장하나요? sql같은거 안쓰고...??
























