import requests
from lxml import etree

# 这他妈不能用花括号
urls = "https://www.umei.cc/katongdongman/dongmantupian/3.htm"  # 1.htm
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50 '
}
# c=list(range(1,6))
# for i in c:
# url= urls+str(i)+".htm"
# a=input(输入页数)
resp = requests.get(url=urls, headers=headers)
resp.encoding = 'utf-8'
tree = etree.HTML(resp.text)
li_list = tree.xpath('//div[@class="TypeList"]/ul/li')
n = 1
for li in li_list:
    img_src = li.xpath('./a/@href')[0]
    sc = requests.get(img_src)
    sc.encoding = 'utf-8'
    tree_1 = etree.HTML(sc.text)
    img_1 = tree_1.xpath('//div[@class="ImageBody"]//img/@src')[0]
    img_name = tree_1.xpath('//div[@class="ImageBody"]//img/@alt')
    f = open('tu_%s.jpg' % n, mode="wb")
    f.write(requests.get(img_1).content)
    n += 1
    print('下载成功')
