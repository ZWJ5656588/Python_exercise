import threading
import time

g_num = 0
mutex=threading.Lock()

def work_1(num):
    mutex.acquire()
    global g_num
    for i in range(num):
        g_num += 1
    mutex.release()
    print(f"线程1计算的结果为: {g_num}")


def work_2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print(f"线程2计算的结果为: {g_num}")


if __name__ == "__main__":
    print(f"线程创建之前g_num的值为: {g_num}")
    t1 = threading.Thread(target=work_1, args=(1000000,))
    t1.start()

    t2 = threading.Thread(target=work_2, args=(1000000,))
    t2.start()

    t1.join()

    # 等待子线程任务执行完毕后再执行主线程代码
    while len(threading.enumerate())!=1:   # 子线程没有执行完，主线程睡眠等待
        time.sleep(1)

    print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)