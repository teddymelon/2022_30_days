# -*- coding: UTF-8 -*-
# Python 2.x引入httplib模块
# import httplib
# Python 3.x引入http.client模块
import http.client

import json

def process(request, token, audioFile) :

    # 读取音频文件
    with open(audioFile, mode = 'rb') as f:
        audioContent = f.read()

    host = 'nls-gateway-ap-southeast-1.aliyuncs.com'

    # 设置HTTP请求头部
    httpHeaders = {
        'X-NLS-Token': token,
        'Content-type': 'application/octet-stream',
        'Content-Length': len(audioContent)
        }


    # Python 2.x使用httplib
    # conn = httplib.HTTPConnection(host)

    # Python 3.x使用http.client
    conn = http.client.HTTPConnection(host)

    conn.request(method='POST', url=request, body=audioContent, headers=httpHeaders)

    response = conn.getresponse()
    print('Response status and response reason:')
    print(response.status ,response.reason)

    body = response.read()
    try:
        print('Recognize response is:')
        body = json.loads(body)
        print(body)

        status = body['status']
        if status == 20000000 :
            result = body['result']
            print('Recognize result: ' + result)
        else :
            print('Recognizer failed!')

    except ValueError:
        print('The response is not json format string')

    conn.close()



appKey = '填寫AppKey'
token = '從Ali的智能語音總覽取得測試用Token'

# 服务请求地址
url = 'http://nls-gateway-ap-southeast-1.aliyuncs.com/stream/v1/asr'

# 音频文件
audioFile = r'C:\Users\ted\Desktop\程式練習\Python\2022_30天_操作\nls-sample-16k.wav'
format = 'pcm'
sampleRate = 16000
enablePunctuationPrediction  = True
enableInverseTextNormalization = True
enableVoiceDetection  = False

# 设置RESTful请求参数
request = url + '?appkey=' + appKey
request = request + '&format=' + format
request = request + '&sample_rate=' + str(sampleRate)

if enablePunctuationPrediction :
    request = request + '&enable_punctuation_prediction=' + 'true'

if enableInverseTextNormalization :
    request = request + '&enable_inverse_text_normalization=' + 'true'

if enableVoiceDetection :
    request = request + '&enable_voice_detection=' + 'true'

print('Request: ' + request)


process(request, token, audioFile)
