'''
Author: Vincent Young
Date: 2022-10-12 04:54:01
LastEditors: Vincent Young
LastEditTime: 2022-10-12 20:47:03
FilePath: /GmailValidChecker/GmailChecker/GmailChecker.py
Telegram: https://t.me/missuo

Copyright © 2022 by Vincent, All Rights Reserved. 
'''

import requests

def verify(email, ouputAlive = None):
	url = "https://mail.google.com/mail/gxlu?email={}".format(email)
	headers = {
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
	}
	resp_headers = requests.get(url=url, headers=headers).headers
	if "Set-Cookie" in resp_headers:
		if ouputAlive == 1:
			print(email, "Alive")
		else:
			pass
	else:
		print(email, "Unregistered")