import asyncio


def request(url):
    print("正在请求的url是", url)
    print("请求成功", url)
    # async修饰的函数，调用之后返回一个协程对象
    # 协程：当程序遇见了IO操作的时候，可以切换到其他任务上
    # 在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
    # 在宏观上，我们能看见的其实是多个任务一起在执行
    # 多任务异步操作

    # 上方说的操作，都是在单线程条件下


c = request(
    'https://zhibo.chaoxing.com/apis/live/setLivePariseCountByEnc?subroomId=318188761980694530&timestamp=1665278356202&enc=86edcb1a1f86e13fe1a1c866bdf874bf')


# 创建一个时间循环对象
# loop = asyncio.get_event_loop()
# #将协程对象注册到loop中，然后启动loop
# loop.run_until_complete(c)

# task的使用
# loop = asyncio.get_event_loop()
# 基于loop创建了一个task对象
# task = loop.create_task(c)
# print(task)
#  loop.run_until_complete(task)
#  print(task)

# future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

def callback_func(task):
    # result返回的就是任务对象中封装的协程对象对应函数的返回值
    print(task.result())


# 绑定回调
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
# 将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)
