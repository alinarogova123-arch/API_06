import telegram
import imghdr
import os
import random
import requests
from dotenv import load_dotenv


FIRST_COMIC_NUMBER = 1


def get_last_comic_number():
	response = requests.get("https://xkcd.com/info.0.json")
	response.raise_for_status()
	last_comic_number = response.json().get("num")

	return last_comic_number


def get_comic_text_and_image_url(comic_number):
	url = f"https://xkcd.com/{comic_number}/info.0.json"
	response = requests.get(url)
	response.raise_for_status()
	comic_image_url = response.json().get("img")
	comic_text = response.json().get("alt")

	return comic_image_url, comic_text


def upload_comic(url, token, chat_id, caption):
	bot = telegram.Bot(token=token)
	bot.send_photo(chat_id=chat_id, photo=url, caption=caption)


def main():
	load_dotenv(".env")
	token = os.environ["TELEGRAM_BOT_API_KEY"]
	chat_id = os.environ["TLGRM_CHAT_ID"]
	comic_number = random.randint(FIRST_COMIC_NUMBER, get_last_comic_number())
	comic_image_url, comic_text = get_comic_text_and_image_url(comic_number)
	upload_comic(comic_image_url, token, chat_id, comic_text)


if __name__ == "__main__":
	main()
