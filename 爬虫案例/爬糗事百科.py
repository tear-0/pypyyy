import requests
import os
import re
if __name__ == '__main__':
    if not os.path.exists('./qiutu'):
        os.mkdir('./qiutu')
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50'
    }
    pageNum=2
    for pageNum in range(3,5):
        new_url=format(url%pageNum)
        page_text = requests.get(url=new_url, headers=headers).text
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list =re.findall(ex,page_text,re.S)
    #tx=re.findall(ex, page_text, re.S)#表示多行
        for src in img_src_list:
            src='https:'+src
            img_data=requests.get(url=src,headers=headers).content
            img_name=src.split('/')[-1]
            imgpath='./qiutu/'+img_name
            with open(imgpath,'wb') as fp:
                 fp.write(img_data)
            print(img_name,'下载成功！')
