# -*- coding: UTF-8 -*-
# Python 2.x 引入httplib模块
# import httplib
# Python 3.x 引入http.client模块
import http.client
# Python 2.x 引入urllib模块
# import urllib
# Python 3.x 引入urllib.parse模块
import urllib.parse
import json
def processGETRequest(appKey, token, text, audioSaveFile, format, sampleRate) :
    host = 'nls-gateway-ap-southeast-1.aliyuncs.com'
    url = 'https://' + host + '/stream/v1/tts'
    # 设置URL请求参数
    url = url + '?appkey=' + appKey
    url = url + '&token=' + token
    url = url + '&text=' + text
    url = url + '&format=' + format
    url = url + '&sample_rate=' + str(sampleRate)
    # voice 发音人，可选，默认是xiaoyun
    # url = url + '&voice=' + 'xiaoyun'
    # volume 音量，范围是0~100，可选，默认50
    # url = url + '&volume=' + str(50)
    # speech_rate 语速，范围是-500~500，可选，默认是0
    # url = url + '&speech_rate=' + str(0)
    # pitch_rate 语调，范围是-500~500，可选，默认是0
    # url = url + '&pitch_rate=' + str(0)
    print(url)
    # Python 2.x 请使用httplib
    # conn = httplib.HTTPSConnection(host)
    # Python 3.x 请使用http.client
    conn = http.client.HTTPSConnection(host)
    conn.request(method='GET', url=url)
    # 处理服务端返回的响应
    response = conn.getresponse()
    print('Response status and response reason:')
    print(response.status ,response.reason)
    contentType = response.getheader('Content-Type')
    print(contentType)
    body = response.read()
    if 'audio/mpeg' == contentType :
        with open(audioSaveFile, mode='wb') as f:
            f.write(body)
        print('The GET request succeed!')
    else :
        print('The GET request failed: ' + str(body))
    conn.close()
def processPOSTRequest(appKey, token, text, audioSaveFile, format, sampleRate) :
    host = 'nls-gateway-ap-southeast-1.aliyuncs.com'
    url = 'https://' + host + '/stream/v1/tts'
    # 设置HTTPS Headers
    httpHeaders = {
        'Content-Type': 'application/json'
        }
    # 设置HTTPS Body
    body = {'appkey': appKey, 'token': token, 'text': text, 'format': format, 'sample_rate': sampleRate}
    body = json.dumps(body)
    print('The POST request body content: ' + body)
    # Python 2.x 请使用httplib
    # conn = httplib.HTTPSConnection(host)
    # Python 3.x 请使用http.client
    conn = http.client.HTTPSConnection(host)
    conn.request(method='POST', url=url, body=body, headers=httpHeaders)
    # 处理服务端返回的响应
    response = conn.getresponse()
    print('Response status and response reason:')
    print(response.status ,response.reason)
    contentType = response.getheader('Content-Type')
    print(contentType)
    body = response.read()
    if 'audio/mpeg' == contentType :
        with open(audioSaveFile, mode='wb') as f:
            f.write(body)
        print('The POST request succeed!')
    else :
        print('The POST request failed: ' + str(body))
    conn.close()
appKey = 'ze3vgSJXD05yENme'
token = '46d6910b290f429ea00e8988fe0ece35'
text = 'Learn to walk before you run'
# 采用RFC 3986规范进行urlencode编码
textUrlencode = text
# Python 2.x请使用 urllib.quote
# textUrlencode = urllib.quote(textUrlencode, '')
# Python 3.x请使用urllib.parse.quote_plus
textUrlencode = urllib.parse.quote_plus(textUrlencode)
textUrlencode = textUrlencode.replace("+", "%20")
textUrlencode = textUrlencode.replace("*", "%2A")
textUrlencode = textUrlencode.replace("%7E", "~")
print('text: ' + textUrlencode)
audioSaveFile = 'syAudio.wav'
format = 'wav'
sampleRate = 16000
# GET 请求方式
processGETRequest(appKey, token, textUrlencode, audioSaveFile, format, sampleRate)
# POST 请求方式
# processPOSTRequest(appKey, token, text, audioSaveFile, format, sampleRate)
