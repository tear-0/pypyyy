import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/new_search_subjects'
    param = {
        'sort': 'U',
        'range': '0,10',
        'tags': '动漫',
        'start': '0',  # 从库中的第几部电影去取
        'limit': '200',  # 一次取出的个数
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50'
    }
    response = requests.get(url=url, params=param, headers=headers)

    list_data = response.json()

    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print('完成')
