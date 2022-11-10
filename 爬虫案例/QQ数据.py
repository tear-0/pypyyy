import requests
from time import sleep
from lxml import etree
import os

from requests.models import Response

url = 'https://qun.qq.com/member.html#gid=1019527171'

headers = {
    'id':' 30119',
'uin':' 2584933784',
'version':' 1.24.33',
'aid':' 31c1f0bd-bb29-4892-96a5-04522db639e0',
'platform':' 100',
'x5Type':' 3',
'netType':' 100',
'sessionId':' session-1615539488023',
'from':' https%3A%2F%2Fqun.qq.com%2Fmember.html',
'referer':' https%3A%2F%2Fxui.ptlogin2.qq.com%2F',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50'
}

response = requests.post(header=headers,url=url).text
tree = etree.HTML(response)
maurl = tree.xpath('//*[@id="qrlogin_img"]/@src')
list = requests.post(maurl)



