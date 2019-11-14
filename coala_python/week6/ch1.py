from selenium import webdriver
import time

# ũ��â(������̹�) ����
driver = webdriver.Chrome("./chromedriver")

# ���İ� ������ ����
driver.get("https://papago.naver.com")

# ������ ���� �� �ð� ����
time.sleep(0.5)

# �Է�â�� �˻��� �Է�
input_box = driver.find_element_by_css_selector("textarea#txtSource")
input_box.send_keys("seize the day")

# ���� ��ư Ŭ��
button = driver.find_element_by_css_selector("button#btnTranslate")
button.click()

# ��ư Ŭ�� �� �ð� ���� & �˻���� ���
time.sleep(0.5)
result = driver.find_element_by_css_selector("div#txtTarget").text
print(result)

# ũ��â �ݱ�
# driver.close()

