import requests
from lxml import etree
import os

if __name__ == '__main__':
    url = 'https://pic.netbian.com/4kdongman/index_7.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50 '
    }
    page_text = requests.get(url=url, headers=headers).text
    # 手动设定响应数据的编码格式
    # page_text.encoding = 'utf-8'
    tree = etree.HTML(page_text)
    # 实例化对象
    li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')
    # 创建文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    for li in li_list:
        img_src = 'https://pic.netbian.com' + li.xpath('./a/@href')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        page_text = requests.get(url=img_src, headers=headers).text
        tree_1 = etree.HTML(page_text)
        # 解决中文乱码
        img_src = 'https://pic.netbian.com' + tree_1.xpath('//*[@id="img"]/img/@src')[0]
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = 'picLibs/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '下载成功！！！')
