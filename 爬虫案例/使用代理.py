import requests
url = 'https://zhibo.chaoxing.com/apis/live/setLivePariseCountByEnc?subroomId=318188761980694530&timestamp' \
      '=1665278356202&enc=86edcb1a1f86e13fe1a1c866bdf874bf '
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50'
}
page_text = requests.get(url=url, headers=headers,proxies={"http":'58.220.95.31:10174'}).text
with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)