import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50'
}
url = 'https://www.baidu.com/s?ie=UTF-8&'
kw = input('输入：')
param ={
    'wd':kw
}
response = requests.get(url=url,params=param,headers=headers)

page_text = response.text
fileName = kw+'.html'
with open (fileName,'w',encoding='utf8') as fp:
    fp.write(page_text)
print(fileName,'保存成功！！！')



