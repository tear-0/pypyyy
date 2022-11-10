import asyncio
from asyncio import tasks

import requests


async def download(url):
    print("开始下载")
    await asyncio.sleep(2)
    requests.request(url)
    print("下载完成")


async def main():
    urls = [
        # "http://www.baidu.com",
        # "http://www.bilibili.com",
        # "http://www.taobao.com"
        "https: // zhibo.chaoxing.com / apis / live / setLivePariseCountByEnc?subroomId = 318188761980694530 & timestamp = 1665278944028 & enc = 01adc99cde8a7cf42d82abd372f50ddd"
    ]
    tasks = []
    for url in urls:
        d = download(url)
        tasks.append(d)

    # await asyncio.wait(tasks)


if __name__ == "__main__":
    asyncio.run(main())
