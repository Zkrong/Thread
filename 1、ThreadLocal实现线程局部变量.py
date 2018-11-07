import threading
import time


# 创建ThreadLocal对象
local = threading.local()

# 全局变量
num = 0


# 对全局变量的操作
def run(x, n):
    x = x + n
    x = x - n


# 进程函数
def func(n):
    # 把全局变量加入到local中，变成局部变量
    # local.x = num
    local.x = 123
    # 调用全局变量操作函数
    for i in range(1000000):
        run(local.x, n)
    print(local.x)
    time.sleep(2)
    print('%s 完成' % (threading.current_thread().name,))



if __name__ == '__main__':
    print('主线程开始')
    # 创建子线程
    t1 = threading.Thread(target=func, args=(6,))
    t2 = threading.Thread(target=func, args=(8,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    # time.sleep(1)
    # 输出全局变量num
    print('num=',num)