#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time

url = "http://chanz.jp/bots/insertForwardTest.php"

pos = "buy"
while True:
	time.sleep(60)
	s = requests.session()
	params = {"user_id":"user_id2", "bot_id":"bot_id2", "market_name":"bitFlyer","position":pos}
	r =  s.post(url, data=params)
	print(params)
	if pos == "buy":
		pos = "sell"
	else:
		pos = "buy"
