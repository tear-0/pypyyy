import asyncio
import aiohttp

urls = [
    # "http://kr.shanghai-jiuxin.com/file/2021/0116/da3ad41249946f839e5587bec12d6d68.jpg",
    # "http://kr.shanghai-jiuxin.com/file/2021/0116/9f26e08deb3e32753df25bfa0f12151a.jpg",
    # "http://kr.shanghai-jiuxin.com/file/2021/0116/2fa461d518b4bfd2c1dc329105b5496b.jpg"
    "https://zhibo.chaoxing.com/apis/live/setLivePariseCountByEnc?subroomId=318188761980694530&timestamp=1665278356202&enc=86edcb1a1f86e13fe1a1c866bdf874bf"
]


async def aiodowmload(url):
    name = url.rsplit("/", 1)[1]  # 从右边切得到第【1】位置的内容
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # 请求回来了。写入文件
            with open(name, mode="wb") as f:
                f.write(await resp.content.read())

    print(name, "搞定")
    # s = aiohttp.ClientSession()  <==> requests
    # requests.get()    .post()
    # s.get()      .post()
    # 发送请求
    # 得到图片内容
    # 保存到文件


async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodowmload(url))
    await asyncio.wait(tasks)


if __name__ == "__main__":
    asyncio.run(main())
