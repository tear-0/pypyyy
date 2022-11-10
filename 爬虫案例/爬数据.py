import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor

f= open("data.csv",mode="w",encoding="utf-8")
csvwriter= csv.writer(f)


def download_one_page(url):
    resp = requests.get(url)
    resp.encoding = "utf-8"
    html = etree.HTML(resp.text)
    table = html.xpath("/html/body/div[2]/div[4]/div[1]/table")[0]
    # trs = table.xpath("./tr")[1:]
    trs = table.xpath("./tr[position()>1]")
    # print(len(trs))
    for tr in trs:
        txt = tr.xpath("./td/text()")
        #对数据进行简单的处理：\\/去掉
        txt = (item.replace("\\","").replace("/","") for item in txt)
        # print(list(txt))
        csvwriter.writerow(txt)
    print(url,"提取完毕")



if __name__ == "__main__":
    #创建线程池
    with ThreadPoolExecutor(400) as t:
        for i in range(1,800):
            #把线程任务提交给线程池
            t.submit(download_one_page,f"http://www.xinfadi.com.cn/marketanalysis/0/list/{i}.shtml")
    print("全部下载完成！")
