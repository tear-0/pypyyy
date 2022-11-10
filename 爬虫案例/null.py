import random
   
def random_header(self):
    """
        随机生成请求头
        :return: headers
    """
    headers = {'Referer': 'https://www.zhipin.com/c101020100/?ka=sel-city-101020100'}
    headers['cookie'] = random.choice(self.cookies)
    headers['user-agent'] = random.choice(self.user_agents)
    return headers


random_header()