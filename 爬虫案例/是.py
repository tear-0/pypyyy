import requests

if __name__ == '__main__':
    s = requests.get(url="https://zhibo.chaoxing.com/apis/live/setLivePariseCountByEnc?subroomId=318188761980694530&timestamp=1665278944028&enc=01adc99cde8a7cf42d82abd372f50ddd").content
    print(s)