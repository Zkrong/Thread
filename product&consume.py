import threading, time, random, queue

condition = threading.Condition()

# 生产者
def producer(q):
    # 无限循环生产
    while True:
        # 使用with自动管理上下文，锁
        with condition:
            # 当队列不满的时候生产
            if q.full():
                # 等待消费者消费完成
                condition.wait()
            else:
                # 执行生产操作
                value = random.randint(0, 10000)
                q.put(value)
                print('生产了%d'%value)
                time.sleep(1)
                condition.notify_all()


# 消费者
def consumer(q):
    while True:
        with condition:
            # q不为空的时候可以消费
            if q.empty():
                # 等待生产
                condition.wait()
            else:
                # 可以消费
                value = q.get()
                print('消费了%d'%value)
                time.sleep(1)
                condition.notify_all()





if __name__ == '__main__':
    # 创建q
    q = queue.Queue(100)
    # 创建生产者
    for i in range(10):
        threading.Thread(target=producer, args=(q,)).start()
    # 创建消费者
    for i in range(10):
        t2 = threading.Thread(target=consumer, args=(q,)).start()
