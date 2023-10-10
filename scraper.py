from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
from config import TodoConfig


class Scraper:

    def __init__(self) -> None:
        pass

    def get_todo_list(self):
        driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()))

        driver.get("https://cyber.inhatc.ac.kr/index.jsp")

        # 팝업 창 처리
        main = driver.window_handles
        for i in main:
            if i != main[0]:
                driver.switch_to.window(i)
                driver.close()
        driver.switch_to.window(main[0])

        # frame 이동으로 NoSuchElementException 오류 해결
        driver.switch_to.frame(driver.find_element(
            By.XPATH, "/html/frameset/frame"))
        # driver.find_element(By.XPATH, '//*[@id="imagePop"]/div[1]/div[1]/a[1]').click()
        driver.execute_script('setImgCookie()')

        # 아이디와 비밀번호
        user_id = TodoConfig.user_id
        user_passwd = TodoConfig.user_pw

        # 아이디 입력란 찾기 및 입력
        id_input = driver.find_element(By.XPATH, '//*[@id="id"]')
        id_input.clear()
        id_input.send_keys(user_id)

        # 비번 입력란 찾기 및 입력
        pw_input = driver.find_element(By.XPATH, '//*[@id="pw"]')
        pw_input.clear()
        pw_input.send_keys(user_passwd)

        login_button = driver.find_element(
            By.XPATH, '//*[@id="loginForm"]/fieldset/p/a')
        login_button.click()

        # 할일 목록 요청
        driver.execute_script('viewTodayList()')
        time.sleep(2)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        li_list = soup.find_all(
            'li', {'style': 'float: none; list-style: none; position: relative; width: 220px;'})

        data = []
        sorted_data = {}
        todo_lsit = ""

        for li in li_list:
            text = li.get_text(strip=True, separator='    ')
            data = text.split("    ")

            # 첫 번째 요소를 기준으로 그룹화
            deadline = "[" + data[1].strip() + "]"
            if deadline not in sorted_data:
                sorted_data[deadline] = []

            data[3] = ' '.join(data[3].split(" ")[1:])
            del data[2]
            del data[1]
            sorted_data[deadline].append(data)

        # 결과 출력
        for key, value in sorted_data.items():
            key += "\n"
            todo_lsit += key

            value_string = "\n".join([" ".join(item) for item in value])
            value_string += "\n"
            todo_lsit += value_string

        todo_lsit = todo_lsit.rstrip('\n')
        return todo_lsit

    def get_cafeteria_menu(self):
        pass
