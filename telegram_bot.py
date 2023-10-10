import requests
from config import TelegramConfig


class TelegramBot:
    def __init__(self):
        self.api_token = TelegramConfig.API_TOKEN
        self.chat_id = TelegramConfig.CHAT_ID

    def send_telegram_message(self, text):
        url = f"https://api.telegram.org/bot{self.api_token}/sendMessage"
        print(url)
        params = {
            'chat_id': self.chat_id,
            'text': text,
        }
        response = requests.get(url, params=params)
        return response.json()
