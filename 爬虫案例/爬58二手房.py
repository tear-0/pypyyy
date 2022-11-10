import requests
from lxml import etree

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50 '
    }
    url = 'https://fy.58.com/ershoufang/'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')
    fp = open('58.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.xpath('./a/div[2]/div[1]/div[1]/h3/text()')[0]
        print(title)
        fp.write(title + '\n')
