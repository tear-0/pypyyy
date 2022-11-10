from threading import Thread
# 第一种写法
# def func():
#     for i in range(1000):
#         print("func",i)

# if __name__ == "__main__":
#     t=Thread(target=func)#创建线程并给线程安排任务
#     t.start()   #多线程状态为可以开始工作状态，具体的执行任务时间由CPU决定
#     for i in range(1000):
#         print("main",i)


# 第二种写法
class MyThread(Thread):
    def run(self):   #固定的   -》  当线程被执行的时候，被执行的就是run()
        for i in range(1000):
            print("子线程",i)

if __name__ == '__main__':
    t=MyThread()
    # t.run()    #方法的调用
    t.start()     # 开启线程

    for i in range(1000):
        print("主线程",i)




