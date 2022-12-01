import threading
import random
from concurrent.futures import ThreadPoolExecutor

# 想实现一等奖2位，二等奖5位，三等奖10位
times=[2,5,10]



lock=threading.Lock()
def luck_draw(arg)  :  # 传入(phones,prices)的元组
    lock.acquire()
    # phone_num列表中抽出一个样本为中奖,用到random.choice(),非空序列中返回一个元素
    price=random.choice(arg[1])
    phone_list=random.choices(arg[0],k=price[1])
    # 抽过一个人，把此人手机号与对应奖项移除
    prices.remove(price)
    phone_str_list=[]
    for i in phone_list:
        phones.remove(i)
        phone_str_list.append(str(i)[-5:-1])
    lock.release()
    return f"尾号是{phone_str_list}的用户，抽到了{price[0]}"

if __name__ == '__main__':
    t=ThreadPoolExecutor(3)   # 创建三个线程实现
    # 确定抽奖人数
    phone_num=int(input("请输入抽奖用户人数：").strip())
    phones=random.sample(range(13300000000,19999999999),phone_num) # 随机截取phone_num长度的片段以列表返回,表示参与抽奖的号码段
    prices=[["一等奖：iPhone12 Promax",2],["二等奖：ipad2022pro",5],["三等奖：air wetter",10]]
    # phones和prices作为元组传入线程函数对象
    result=[]
    for i in range (3): # 三个任务，每个线程分配一个
        # 创建线程任务
        t_result=t.submit(luck_draw,(phones,prices))
        result.append(t_result)

    print(result)

    # 获取线程任务结果
    for res in result:
        print(res.result())





