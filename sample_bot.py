#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import json

url = "https://25b4v0hwdg.execute-api.us-east-2.amazonaws.com/development/sendPseudoOrder"

pos = "buy"
while True:
	s = requests.session()
	params = {
		"BotId": "ec2_local",
  		"MarketName": "bitFlyer",
 	 	"Position": pos,
  		"Product": "FX_BTC_JPY"
	}
	r =  s.post(url, data=params)
	print(json.dumps(params))
	print(r)
	if pos == "buy":
		pos = "sell"
	else:
		pos = "buy"
	time.sleep(60)
