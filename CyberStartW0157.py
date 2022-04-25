import requests
import base64

url = 'https://play.cyberstart.com/challenge/W0157/Setup'
data = 'spin=new'
#send a post request to the server with cookies
r = requests.post(url, data=data, cookies={"PHPSESSID": "ff37e894b6cfcf2b6c8e3bab79b023d4"})

#seperate r by .
r = r.text.split('.')
firstNumTemp = r[0]
secondNum = r[2]
sign = r[1]
firstNumTemp = firstNumTemp.split('"')
r[0] = firstNumTemp[3]
#base64 decode all of r
for i in range(len(r)):
    r[i] = base64.b64decode(r[i])
print(r)
firstNum = int(r[0].decode('utf-8'))
secondNum = int(r[1].decode('utf-8'))
sign = r[2].decode('utf-8')
finalNum = ''
if sign == "plus":
    finalNum = (firstNum + secondNum)
if sign == "minus":
    finalNum = (firstNum - secondNum)
if sign == "times":
    finalNum = (firstNum * secondNum)
if sign == "divide":
    finalNum = (firstNum / secondNum)

submitData = 'first=' + str(firstNum) + '&second=' + str(secondNum) + '&op=' + sign + '&ans=' + str(finalNum) + '&act=%2Fflashfast%2Fanswer'
submitUrl = 'https://play.cyberstart.com/challenge/W0157/Verify'
#header info
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://play.cyberstart.com/challenge/W0157',
    'Content-type': 'application/x-www-form-urlencoded'
}
r = requests.post(submitUrl, headers=headers, data=submitData, cookies={"PHPSESSID": "ff37e894b6cfcf2b6c8e3bab79b023d4"})
print(r.text)