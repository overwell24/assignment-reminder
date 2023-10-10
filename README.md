# 프로젝트 제목

어쩔 과제 저쩔 학점

## 만든 이유

추석 연휴기간에 과제 놓쳐서 만듦

## 사용 기술

프로그래밍 언어: `Python` <br>
활용 모듈: `selenium`, `BeautifulSoup`, `requests` <br>
API: Telegram 봇 API 사용 <br>
작업 스케줄링: 리눅스 crontab을 사용하여 정기적인 스크립트 실행<br>

## 개발 기간

2023.10.10 ~ 2023.10.11

## 프로젝트 설명

기능별로 파일을 나눠서 구성해봤다. <br>

- scraper.py: 크롤링 + 데이터 가공
- telegram_bot.py: API 요청
- main.py: 실행 로직
- config.py: 토큰 계정 정보 분리 저장 / github에는 빠졌다 실행하려면 새로 만들어야함

config.py 형식

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
