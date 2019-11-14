tmp_url = 'https://www.kookmin.ac.kr/site/resource/board/academic/'
for i in range(1, 5):
    base_url = tmp_url + '?&pn={}'
    this_page = i - 1
    page_url = f'base_url{this_page}'
    print(page_url)