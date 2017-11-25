import requests
import misc
from yobit import get_btc
from time import sleep
# import json


token = misc.token
url_begin = 'https://api.telegram.org/bot' + token + '/' # sendMessage?chat_id=100310279&text=hi

global last_update_id
last_update_id = 0

def get_updates():
	url = url_begin + 'getupdates'
	r = requests.get(url)
	return r.json()

def get_message():
	data = get_updates()

	last_object = data['result'][-1]
	current_update_id = last_object['update_id']

	global last_update_id
	if last_update_id != current_update_id:
		last_update_id = current_update_id
		chat_id = last_object['message']['chat']['id']
		message_text = last_object['message']['text']
		message = {'chat_id' : chat_id, 'text' : message_text}
		return message
	else: return None

def send_message(chat_id, text = 'Wait a second, please...'):
	url = url_begin + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	requests.get(url)

def main():
	# d = get_updates()
	# with open('updates.json',mode = 'w', encoding = 'utf8') as f:	json.dump(d, f, indent=4, ensure_ascii=False)
	# send_message(12, 'HEEEEEy')
	while True:
		answer = get_message()

		if answer != None:
			chat_id = answer['chat_id']
			text = answer['text']
			if text == '/btc':
			# if 'hello' or 'Hello' or 'hi' or 'Hi' in text:
				send_message(chat_id, get_btc())
			elif ''
			# send_message(chat_id, 'Hello, World?')
		else: continue

if __name__ == '__main__':
	main()