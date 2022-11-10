# from asyncio import tasks
import requests
import asyncio
import aiohttp
import json
import aiofiles
# http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}

# http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}  -->所有章节的url

# 1.同步操作：访问getCatalog  拿到所有章节的cid和名称
# 2.异步操作：访问getChapterContent  下载所有的文章内容
async def aiodownload(cid,b_id,title):
    data = {
        "book_id":b_id,
        "cid":f"{b_id}|{cid}",
        "need_bookinfo":1
    }
    data = json.dumps(data)
    url = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:#首先要建立一个session对象，然后用session对象去打开网页
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open(title,mode="w",encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])#把小说内容写出
            #dic['data']['novel']['content']


async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:#  item就是对应每一个章节的名称和cid
        title = item['title']
        cid = item['cid']
        #准备异步任务
        tasks.append(aiodownload(cid,b_id,title))
    #asyncio.run(asyncio.wait(tasks))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    b_id = "4306063500"
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+ b_id +'"}'
    asyncio.run(getCatalog(url))