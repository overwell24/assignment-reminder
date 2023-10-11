# 어쩔 과제 저쩔 학점

인하공전 과제 알림이

## 프로젝트 작동화면

<img src="https://github.com/overwell24/assignment-reminder/assets/129687688/d7b8e452-7a1d-4209-8bc1-705b4b80747d" width="40%" height="40%" >
<br>

## 프로젝트 소개

해야할 과제를 텔레그램을 통해 알려준다.

## 만든 이유

추석 연휴기간 동안 과제 놓쳐서 만듦 <br>
~~이거 만들다가 학교 못감 아 내 학점~~

## 사용 기술

프로그래밍 언어: `Python` <br>
활용 모듈: `selenium`, `BeautifulSoup`, `requests` <br>
API: Telegram 봇 API 사용 <br>
작업 스케줄링: 리눅스 `crontab`을 사용하여 정기적인 스크립트 실행<br>

## 개발 기간

2023.10.10 ~ 2023.10.11

## 프로젝트 구조

기능별로 파일을 나눠서 구성해봤다. <br>

- scraper.py: 크롤링 + 데이터 가공
- telegram_bot.py: API 요청
- main.py: 실행 로직
- config.py: 토큰, 계정 정보 분리 저장

## 프로젝트 실행 가이드

config.py 새로만든다.

```python
# 텔레그램 API
class TelegramConfig:
    API_TOKEN = ""
    CHAT_ID = 1234

# 로그인 정보
class TodoConfig:
    user_id = ""
    user_pw = ""
```

의존성 모듈을 설치한다.

```bash
pip install selenium
pip install webdriver-manager
pip install chromedriver_autoinstaller

pip install requests
pip install beautifulsoup4
```

## 알게 된 거 정리

- 셀레니움 버전별 사용방법
- 텔레그램 API 사용법
- Python 메소드(클래스 메소드, 인스턴스 메소드)

### 셀레니움 버전별 사용방법

셀레니움 3

```python
driver.find_element_by_class_name("")
driver.find_element_by_id("")
driver.find_element_by_css_selector("")
driver.find_element_by_name("")
driver.find_element_by_tag_name("")
driver.find_element_by_xpath("")
driver.find_element_by_link_text("")
driver.find_element_by_partial_link_text("")
# 복수형 find_elements_by
```

셀레니움4

```python
driver.find_element(By.CLASS_NAME, "")
driver.find_element(By.ID, "")
driver.find_element(By.CSS_SELECTOR, "")
driver.find_element(By.NAME, "")
driver.find_element(By.TAG_NAME, "")
driver.find_element(By.XPATH, "")
driver.find_element(By.LINK_TEXT, "")
driver.find_element(By.PARTIAL_LINK_TEXT, "")
# 복수형 find_elements
```

### 텔레그램 API 사용법

1. 봇 생성: BotFather 검색 후 봇 생성

2. 봇 등록: 그룹 or 채널 생성 후 만든 bot 초대해서 admin 등록

3. chat_id 얻기: (봇 생성때 얻은 토큰)

   ```
   https://api.telegram.org/bot{{token}}/getUpdates
   ```

4. 테스트

   ```python
   import requests

   # 메시지 보내기
   API_TOKEN = "YOUR_BOT_TOKEN_HERE"
   chat_id = "YOUR_CHAT_ID_HERE"

   # 텔레그램 API URL
   send_message_url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"

   # 메시지 파라미터
   message_params = {
       'chat_id': chat_id,
       'text': '안녕하세요! 이것은 텔레그램 봇 메시지입니다.',
   }

   # 메시지 전송
   response = requests.get(send_message_url, params=message_params)

   # 응답 확인
   if response.status_code == 200:
       print("메시지가 성공적으로 전송되었습니다.")
   else:
       print("메시지 전송 실패:", response.text)

   ```
