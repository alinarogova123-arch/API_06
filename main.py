import telegram
import imghdr
import os
import random
import requests
from dotenv import load_dotenv


FIRST_COMICS_NUMBER = 1


def get_last_comics_number():
	response = requests.get("https://xkcd.com/info.0.json")
	response.raise_for_status()
	last_comics_number = response.json().get("num")

	return last_comics_number


def get_comics_data(comics_number):
	url = f"https://xkcd.com/{comics_number}/info.0.json"
	response = requests.get(url)
	response.raise_for_status()
	comics_image_url = response.json().get("img")
	comics_text = response.json().get("alt")

	return comics_image_url, comics_text


def upload_comics(url, token, chat_id, caption):
	bot = telegram.Bot(token=token)
	bot.send_photo(chat_id=chat_id, photo=url, caption=caption)


def main():
	load_dotenv(".env")
	token = os.environ["TELEGRAM_BOT_API_KEY"]
	chat_id = os.environ["TLGRM_CHAT_ID"]
	comics_number = random.randint(FIRST_COMICS_NUMBER, get_last_comics_number())
	comics_image_url, comics_text = get_comics_data(comics_number)
	upload_comics(comics_image_url, token, chat_id, comics_text)


if __name__ == "__main__":
	main()
