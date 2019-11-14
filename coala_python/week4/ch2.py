# "�˻���"���� �߰��մϴ�.
# ������ �����ġ�� "�˻���" ī�װ��� �߰��մϴ�.
# "�˻���" ī�װ��� �Է��� Ű���带 �������ݴϴ�.
# *Stage4���� �ϼ��� ������ ���α׷��� �����Ͱ� �����Ǿ� ����ǹǷ� �۵�Ȯ���� ���ؼ�
# ������ ���� ������ ������ �� �������ּž��մϴ�.


import requests
from bs4 import BeautifulSoup


# �߰�1

# �������(w)���� navernews.csv������ ����.
f = open("navernews.csv", "w")
# �������� ����κ��� �Է��Ѵ�.
f.write("�˻���, ����, ��л�\n")

keyword = input("�˻�� �Է����ּ���: ")
page = 1
for page in range(1, 4):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query="+keyword +"&start=" + str(page),

                       headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser', from_encoding='utf-8')


    # �����̳�: ul.type01 > li
    # �������: a._sp_each_title
    # ��л�: span._sp_each_source

    # 1. �����̳� ����
    articles = html.select("ul.type01 > li")

    # 2. ��� ������ ����

    for ar in articles:
        title = ar.select_one("a._sp_each_title").text
        source = ar.select_one("span._sp_each_source").text

        title = title.replace(",", "")
        source = source.replace(",", "")

        # ����(title)�� ��л�(source)�� ,�� �����Ͽ� ���ݴϴ�.
        f.write(keyword+','+title + ',' + source + '\n')


f.close()
