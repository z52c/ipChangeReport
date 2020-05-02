from urllib import request
import time
import os
import sys

#将SCKEY填入下面
SCKEY = 'SCU95384T96970d1e816d46892bc2a33e3f95a2eb5ea3164b6ee74'


def getIP():
    try:
        url = 'http://members.3322.org/dyndns/getip'
        response = request.urlopen(url)
        data = response.read()
        data = str(data, encoding = "utf-8")
        return data
    except:
        print('getIp failed wait 1 minute')
        time.sleep(1*60)
        return getIP()


def sendToWechat(title, content):
    try:
        url = 'https://sc.ftqq.com/' + SCKEY + '.send?text=' + title + '&desp=' + content
        response=request.urlopen(url)
        data=response.read()
        data=str(data, encoding = "utf-8")
        print(data)
    except:
        print(sys.exc_info()[0])
        print('sendToWechat failed wait 1 minute')
        time.sleep(1*60)
        sendToWechat(title, content)


if __name__ == '__main__':
    if not os.path.exists('ip') :
        with open('ip','w') as f:
            pass
    while True:
        ipAddr = getIP()
        with open('ip','r') as f:
            ipOld = f.read()
        if ipAddr != ipOld:
            with open('ip','w') as f:
                f.write(ipAddr)
            print('ipchanged')
            sendToWechat('ipchanged',ipAddr)
            print('sent')
        time.sleep(60*30)
