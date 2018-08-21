from threading import Lock
from threading import Thread
import time


# 定义全局变量
num = 100

# 创建锁
lock = Lock()

def run(n):
    print('子线程开始执行')
    global num
    global lock
    for i in range(1000000):
        # 100 = 100 + 6
        # 100 = 100 - 9
        # num = 91
        # 获取锁
        # try:
        #     lock.acquire()
        #     num = num + n
        #     num = num - n
        # finally:
        #     # 操作完成之后需要释放锁
        #     lock.release()

        # 使用上下文管理器, 会自动的获取锁，自动的释放锁。
        with lock:
            num = num + n
            num = num - n

    time.sleep(1)
    # print(num)
    print('子线程结束执行')


if __name__ == '__main__':
    print('主线程开始执行')
    t1 = Thread(target=run, args=(6,))
    t2 = Thread(target=run, args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('num=', num)

    print('主线程结束执行')