from urllib import request
import time
import os

#将SCKEY填入下面
SCKEY = ''


def getIP():
    url = 'http://members.3322.org/dyndns/getip'
    response = request.urlopen(url)
    data = response.read()
    data = str(data, encoding = "utf-8")
    return data


def sendToWechat(title, content):
    url = 'https://sc.ftqq.com/' + SCKEY + '.send?text=' + title + '&desp=' + content
    response=request.urlopen(url)
    data=response.read()
    data=str(data, encoding = "utf-8")
    print(data)


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
