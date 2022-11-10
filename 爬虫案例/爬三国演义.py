import requests
from bs4 import BeautifulSoup
import lxml

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    # 先用二进制，在转成字符串“utf-8”
    page_content = requests.get(url=url, headers=headers).content
    page_text = str(page_content, 'utf-8')
    # 实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')
    li_list = soup.select('.book-mulu>ul>li')
    fp = open('./sanguo.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        # 对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url, headers=headers).content
        detail_page_text = str(detail_page_text, 'utf-8')
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_="chapter_content")
        # 解析到了章节内容             #他妈的class要加下划线！！！！！！
        content = div_tag.text
        fp.write(title + ':' + content + '\n')
        print(title, '爬取成功')
