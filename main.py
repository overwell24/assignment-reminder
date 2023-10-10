from scraper import Scraper
from telegram_bot import TelegramBot


def main():
    scraper = Scraper()
    todo_list = scraper.get_todo_list()
    print(todo_list)

    bot = TelegramBot()
    # Telegram으로 메시지 보내기
    response = bot.send_telegram_message(todo_list)

    if response['ok']:
        print("텔레그램으로 메시지가 전송되었습니다.")
    else:
        print("텔레그램 메시지 전송에 실패했습니다.")


if __name__ == "__main__":
    main()
