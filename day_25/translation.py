#coding:utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalimt.request.v20181012 import TranslateGeneralRequest
import json
# 創建AcsClient
client = AcsClient(
"AccessKey ID",  # AccessKey ID
"Access Key Secret", # Access Key Secret
"cn-hangzhou"  # 地區ID，都是杭州
)
# 創建Request，並且調整成你自己需要的參數
request = TranslateGeneralRequest.TranslateGeneralRequest()
request.set_SourceLanguage("en")
request.set_SourceText("Nice to meet you.")
request.set_FormatType("text")
request.set_TargetLanguage("zh-tw")
request.set_method("POST")
# 發起請求，並顯示返回的Json值
response = client.do_action_with_exception(request)
print(json.loads(response))
