"""调用multiprocessing的Que模块"""
import multiprocessing
from multiprocessing import Queue
import json

class Work(object):
    def __init__(self,queue):
        self.queue=queue

    def send(self,message):
        if not isinstance(message,str):
            message=json.dumps(message)   # 使用Json字符串序列化
        self.queue.put(message)

    def recieve(self):
        while 1:
            result=self.queue.get()
            # 获取队列对象queue传入的message
            # 由于接收的message可能不是一个字符串，所以要异常捕获
            # 如果传入的是Json格式，则通过loads反序列化接收，否则直接传给res接收
            try:
                res=json.loads(result)
            except:
                res=result
            print("接收到的信息为%s" % res)





if __name__ == '__main__':
    # 创建一个队列对象，在进程对象运行的函数中调用队列对象
    queue=multiprocessing.Queue()
    work=Work(queue)
    # 创建一个进程对象
    send=multiprocessing.Process(target=work.send,args=({"message":"这是一条测试消息"},))
    recieve=multiprocessing.Process(target=work.recieve)



    send.start()
    recieve.start()
