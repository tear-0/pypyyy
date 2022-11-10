import asyncio
import time


async def func1():
    print("你好啊，我叫阎晓明")
    #time.sleep(3)   #当程序出现了同步操作的时候，异步就中断了
    await asyncio.sleep(3)  #异步操作代码  awaait挂起
    print("你好啊，我叫阎晓明")

async def func2():
    print("你好啊，我叫冯晓宇")
    await asyncio.sleep(5)
    print("你好啊，我叫冯晓宇")

async def func3():
    print("你好啊，我叫炸蔬菜")
    await asyncio.sleep(4)
    print("你好啊，我叫炸蔬菜")
async def main():
    #第一种写法
    #f1 = func1()
    #await f1 #  一般await挂起操作放在协程对象前面
    # 第二中写法（推荐）
    tasks = [
        func1(),
        func2(),
        func3()
    ]
    await asyncio.wait(tasks)


if __name__  == "__main__":
    # f1 = func1()
    # f2 = func2()
    # f3 = func3()
    # tasks = [
    #     f1,f2,f3
    # ]
    t1 = time.time()
    #一次性启动多个任务（协程）
    asyncio.run(main())
    t2 = time.time()
    print(t2-t1)


