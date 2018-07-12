#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import time
import json
import sys

url = "https://25b4v0hwdg.execute-api.us-east-2.amazonaws.com/development/sendPseudoOrder"

pos = "buy"
while True:
	s = requests.session()
	headers = {"Content-Type" : "application/json"}
	params = {
		"BotId": "ec2_local_second",
  		"MarketName": "bitFlyer",
 	 	"Position": pos,
  		"Product": "FX_BTC_JPY"
	}
	json_data = json.dumps(params).encode("utf-8")
	r =  s.post(url, data=json_data)
	print(params)
	print(r)
	sys.stdout.flush()
	if pos == "buy":
		pos = "sell"
	else:
		pos = "buy"
	break
	time.sleep(60)
