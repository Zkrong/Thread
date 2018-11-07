import threading, time


# 创建一个条件变量实例对象
condition = threading.Condition()

# 输出偶数
def even():
    # print('输出偶数')
    # 获取锁
    # if condition.acquire():
    with condition:
        for i in range(0, 10, 2):
            print(i)

            condition.wait()

            # 通知对方
            condition.notify()
            # time.sleep(1)


# 输出奇数
def odd():
    # print('输出奇数')
    # 获取锁
    # if condition.acquire():
    with condition:
        for i in range(1, 10, 2):
            print(i)
            # 发送通知
            condition.notify()

            # 等待
            condition.wait()

            # time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=even)
    t2 = threading.Thread(target=odd)
    t1.start()
    t2.start()
