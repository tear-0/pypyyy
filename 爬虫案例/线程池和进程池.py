#线程池：一次性开辟一些线程，我们用户直接给线程池提交任务，线程任务的调度交给线程池来完成
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
def fn(name):
    for i in range(100):
        print(name,i)

if __name__ == "__main__":
    #创建线程池
    with ThreadPoolExecutor(50) as t:#创建50个线程
        for i in range(100):#提交100个任务
            t.submit(fn,name=f"线程{i}")#给线程池提交fn这个任务
        #等待线程池中任务全部执行完毕。才能继续执行（守护）
        print("123")


