import requests
from lxml import etree
import os

if __name__ == "__main__":
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'

    }
    # 创建一个文件夹
    if not os.path.exists('./resumelibs'):  # 如果不存在
        os.mkdir('./resumelibs')

    url = 'http://aspx.sc.chinaz.com/query.aspx?keyword=%E5%85%8D%E8%B4%B9&classID=864'
    page_text = requests.get(url=url,headers=headers).text

    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@id="container"]/div')

    for div in div_list:
        resume_src = 'http:'+div.xpath('./a/@href')[0]
        resume_name = div.xpath('./a/img/@alt')[0]+'.zip'

        # 对每个简历页面发起请求
        detail_text = requests.get(url=resume_src, headers=headers).text
        tree1 = etree.HTML(detail_text)
        # 解析出下载链接
        download_src = tree1.xpath('//div[@class="clearfix mt20 downlist"]/ul/li[1]/a/@href')[0]

        # 对下载链接发起请求
        down_load_resume = requests.get(url=download_src, headers=headers).content
        down_load_path = 'resumelibs/' + resume_name

        with open( down_load_path,'wb') as fp:
             fp.write(down_load_resume)
             print(resume_name,'下载成功！！！！')
