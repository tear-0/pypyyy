import os

import requests
from lxml import etree

url = "https://www.hongxiu.com/chapter/23776959709227004/63830509708437319"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 '
}


def jiexi(uurl):
    # 解析html
    page_content = requests.get(url=uurl, headers=headers).content
    page_text = str(page_content, 'utf-8')
    # print(page_text)
    tree = etree.HTML(page_text)
    # 书名
    # print("书名: 《" + ''.join(tree.xpath('//*[@class="last-nav act"]/text()')) + "》")
    # 打印文章标题
    # print("标题: " + ''.join(tree.xpath('//*[@class="j_chapterName"]/text()')))
    # 打印文章字数
    # print("字数: " + ''.join(tree.xpath('//*[@class="j_chapterWordCut"]/text()')))
    # 打印文章内容
    # print(''.join(tree.xpath('//*[@class="ywskythunderfont"]/p//text()')))
    book__name = '/' + ''.join(tree.xpath('//*[@class="j_chapterName"]/text()')) + '.txt'
    with open('./爬轻之文库小说/' + book_name + book__name, 'wb') as fp:
        fp.write(bytearray(''.join(tree.xpath('//*[@class="ywskythunderfont"]/p//text()')), 'utf-8'))
    # print(''.join(tree.xpath('//*[@class="j_chapterName"]/text()')), "写入成功!!!")
    uuurl = "https://www.hongxiu.com" + ''.join(tree.xpath('//*[@id="j_chapterNext"]/@href'))
    # for i in range(nu):
    #     return jiexi(uuurl)
    return uuurl


if __name__ == "__main__":
    fpage_content = requests.get(url=url, headers=headers).content
    fpage_text = str(fpage_content, 'utf-8')
    # print(page_text)
    ftree = etree.HTML(fpage_text)
    # 书名
    # print("书名: 《" + ''.join(ftree.xpath('//*[@class="last-nav act"]/text()')) + "》")
    book_name = ''.join(ftree.xpath('//*[@class="last-nav act"]/text()'))
    os.mkdir('./爬轻之文库小说')
    if not os.path.exists('./爬轻之文库小说/' + book_name):
        os.mkdir('./爬轻之文库小说/' + book_name)
    n = int(input("请输入爬取的章节: "))
    s = jiexi(url)
    # print("下一章链接是: ")
    # 打印50章
    for i in range(n):
        s = jiexi(s)
        finsh = "▓" * int(i / (n / 50))
        progress = i / (n / 100) + i + 2
        print("\r{:^3.0f}%[{}{}]".format(progress, finsh, ' ' * int(50 - i / (n / 50))), end="")
    print("结束了!!!")
