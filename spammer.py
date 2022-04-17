import colorama
from colorama import *
import datetime
import requests
import json
from os import system
import os
import time


print('''

█▀▄ █ █▀ █▀▀ █▀█ █▀█ █▀▄
█▄▀ █ ▄█ █▄▄ █▄█ █▀▄ █▄▀

█▀ █▀█ ▄▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀█
▄█ █▀▀ █▀█ █░▀░█ █░▀░█ ██▄ █▀▄
''')

print(Fore.RED + 'version 0.1 by wannacry')
print(Fore.WHITE)
print('')
print('')
print("Welcome, choose option:")
print('''
1 - Start attack
2 - Add tokens
3 - Token track
''')
x = int(input('$ '))
defaultMessage = '''
```
@everyone it's time to die in pings, join us in telegram https://t.me/dsspambywannacry
```
'''

defaultMessage1 = '''
```
@everyone it's time to die in pings join us in telegram https://t.me/dsspambywannacry
```
'''
exitMenu = '''\nTo return to the menu, use the combination Ctrl + C.'''
spamMenu = '''\n[1] - Spam in 1 chat.
[2] - Spam to all chats.'''
modeMenu = '''\n[1] - Custom settings.
[2] - Default settings.'''

tokenTrackMenu = '''\n[1] - Check 1 token.
[2] - Automatic check and writing to tokens.txt.
'''

addMenu = '''\n[1] - Add tokens.'''

def spam(defaultMessage, defaultMessage1):
	sessionName = 'Server spam'
	errorLog = open('errorlogs.txt', 'a+')
	print(exitMenu)
	print(spamMenu)
	try:
		select = str(input('\nSelect: '))
		if select == '1':
			channelID = input('\nChannel ID: ')
			print(modeMenu)
			mode = str(input('\nSelect: '))
			if mode == '1':
				messages1 = input('\nMessage [1]: ')
				messages2 = input('\nMessage [2]: ')
			else:
				messages1 = defaultMessage
				messages2 = defaultMessage1
			print('\nSpam started.')
			with open('tokens.txt','r') as handle:
				tokens = handle.readlines()
				while True:
					data = any(tokens)
					if data == True:
						for x in tokens:
							token = x.rstrip()
							headers = {'Authorization': token}
							json1 = {'content': messages1}
							json2 = {'content': messages2}
							req = requests.post(f'https://discord.com/api/v9/channels/{channelID}/messages', json=json1, headers=headers)
							if req.status_code in statuses:
								req = requests.post(f'https://discord.com/api/v9/channels/{channelID}/messages', json=json2, headers=headers)
								if req.status_code not in statuses:
									errorLog.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n")
							else:
								errorLog.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n")
					else:
						print('\nNo tokens.')
		elif select == '2':
			serverID = input('\nServer ID: ')
			print(modeMenu)
			mode = str(input('\nSelect: '))
			if mode == '1':
				messages1 = input('\nMessage [1]: ')
				messages2 = input('\nMessage [2]: ')
			else:
				messages1 = defaultMessage
				messages2 = defaultMessage1
			print('\nSpam started.')
			channels = []
			tokenSH = []
			with open('tokens.txt','r') as handle:
				tokens = handle.readlines()
				for x in tokens:
					token = x.rstrip()
					tokenSH.append(token)
				data1 = any(tokenSH)
				if data1 == True:
					headers = {'Authorization': tokenSH[0]}
					request = requests.get(f'https://discord.com/api/v9/guilds/{serverID}/channels', headers=headers)
					if request.status_code == 200:
						for channel in request.json():
							if channel["type"] == 0:
								channels.append(channel['id'])
					else:
						errorLog.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {request.status_code}] [Message: {request.json()}\n")
					data2 = any(channels)
					if data2 == True:
						while True:
							for channelID in channels:
									for token in tokenSH:
										headers = {'Authorization': token}
										json1 = {'content': messages1}
										json2 = {'content': messages2}
										req = requests.post(f'https://discord.com/api/v9/channels/{channelID}/messages', json=json1, headers=headers)
										if req.status_code in statuses:
											req = requests.post(f'https://discord.com/api/v9/channels/{channelID}/messages', json=json2, headers=headers)
											if req.status_code not in statuses:
												errorLog.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n")
										else:
											errorLog.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n")
		elif select == '3':
			print(menu)
			select = str(input('\nSelect: '))
			if select == '1':
				print(helpSpamEN)
			elif select == '2':
				print(helpSpamRU)
			else:
				print('\nInvalid option.') 
		else:
			print('\nIvalid option.')
	except KeyboardInterrupt:
		print('\nExit...')
	errorLog.close()
	nextCode = input('\nPress key to continue.')
	
def tokenTrack():
	sessionName = 'Token track'
	errorLog = open('errorlogs.txt', 'a+')
	print(exitMenu)
	print('\nThis item will allow you to find out the token of the account to which your IP was linked.')
	print(tokenTrackMenu)
	try:
		select = str(input('\nSelect: '))
		if select == '1':
			login = input('\nLogin: ')
			password = input('\nPassword: ')
			infoLogin = {
				'captcha_key': None,
				'gift_code_sku_id': None,
				'login': login,
				'login_source': None,
				'password': password,
				'undelete': False
				}
			req = requests.post('https://discord.com/api/v8/auth/login', json=infoLogin)
			if req.status_code in statuses:
				info = req.json()
				token = info['token']
				print(f'\nToken: {token}')
			else:
				errorLog.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n")
				print('\nError.')
		elif select == '2':
			file = open('tokens.txt', 'a')
			while True:
				login = input('\nLogin: ')
				password = input('\nPassword: ')
				infoLogin = {
					'captcha_key': None,
					'gift_code_sku_id': None,
					'login': login,
					'login_source': None,
					'password': password,
					'undelete': False
					}
				req = requests.post('https://discord.com/api/v8/auth/login', json=infoLogin)
				if req.status_code in statuses:
					info = req.json()
					token = info['token']
					print(f'Token: {token}')
					file.write(token + '\n')
				else:
					errorLog.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n")
					print('\nError.')
		elif select == '3':
			print(menu)
			select = str(input('\nSelect: '))
			if select == '1':
				print(helpTrackEN)
			elif select == '2':
				print(helpTrackRU)
			else:
				print('\nInvalid option.')
		else:
			print('\nInvalid option.')
	except KeyboardInterrupt:
		print('\nExit...')
	errorLog.close()
	nextCode = input('\nPress key to continue.')
	
def add():
	sessionName = 'Manager'
	print(exitMenu)
	print(addMenu)
	try:
		select = str(input('\nSelect: '))
		if select == '1':
			file1 = open('tokens.txt', 'a')
			while True:
				token = str(input('\nToken: '))
				file1.write(f'{token}\n')
				print('Token added.')
		elif select == '2':
			file2 = open('webhooks.txt', 'a')
			while True:
				webhook = str(input('\nWebhook: '))
				file2.write(f'{webhook}\n')
				print('Webhook added.')
		elif select == '3':
			file1 = open('tokens.txt', 'w')
			file1.close()
		elif select == '4':
			file2 = open('tokens.txt', 'w')
			file2.close()
		elif select == '5':
			with open('tokens.txt', 'r') as handle:
				tokens = handle.readlines()
				for x in tokens:
					token = x.rstrip()
					print(token)
		elif select == '6':
			with open('webhooks.txt', 'r') as handle:
				webhooks = handle.readlines()
				for x in webhooks:
					webhook = x.rstrip()
					print(webhook)
		elif select == '7':
			print(menu)
			select = str(input('\nSelect: '))
			if select == '1':
				print(helpAddEN)
			elif select == '2':
				print(helpAddRU)
			else:
				print('\nInvalid option.')
		else:
			print('\nInvalid option.')
	except KeyboardInterrupt:
		print('\nExit...')
	nextCode = input('\nPress key to continue.')

	
if x == 1:
	spam(defaultMessage, defaultMessage1)
if x == 2:
	add()
	
if x == 3:
	tokenTrack()