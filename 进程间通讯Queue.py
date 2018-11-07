from multiprocessing import Queue,Process
import time

def write(q):
    print('写入')
    for value in "ABCDEF":
        print('写入%s'%(value,))
        q.put(value,timeout=1)
        time.sleep(2)
    print('写入结束')

def read(q):
    print('开始读')
    while True:
        value= q.get()
        if value == None:
            break
        print('读出%s'%(value,))
        print("读出结束")


if __name__ == '__main__':
    print('主进程开始')

    q = Queue(3)
    p1 = Process(target = write,args=(q,))
    p2 = Process(target=read,args=(q,))
    p1.start()
    p2.start()

    print('主进程结束')