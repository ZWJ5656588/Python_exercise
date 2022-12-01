"""async def xxx()
        result=await test()
一定记住 async与await配合使用，最后asyncio.run自动创建事件循环并且异步task执行"""

"""gather 将异步函数批量执行     参数：协程函数对象   返回值：List返回函数的结果
    run   一般用来执行主异步函数  参数：task对象     返回值：执行函数的返回结果"""

import time
import random
import asyncio


# 1.
async def test_a():
    for i in range(5):
        _start_time=time.time()
        # 此时的time.sleep是cpu级别的io过程，使程序看上去是同步，事实上sleep函数也可以异步
        time.sleep(random.random()*2)
        _end_time=time.time()
        print("这是\'test_a()\'函数的第{}循环，随机休眠时间为{}".format(i+1,_end_time-_start_time))
    return "这是一封离别信"


async def test_b():
    for i in range(5):
        _start_time=time.time()
        # 此时的time.sleep是cpu级别的io过程，使程序看上去是同步，事实上sleep函数也可以异步
        time.sleep(random.random()*2)
        _end_time=time.time()
        print("这是\'test_b()\'函数的第{}循环，随机休眠时间为{}".format(i+1,_end_time-_start_time))
    return "写下离开的原因"


async def main():  # 主函数也要声明成异步函数，接收其他协程函数的返回值
    # 使用gather函数，批量执行协程函数，将其返回值列表给到result
    start_time=time.time()
    result= await  asyncio.gather(test_a(),test_b())   # await关键字 拿到test_a(),test_b()返回值并通过gather函数成为列表
    print(result)
    end_time = time.time()
    print(f"共耗时{end_time-start_time}")

asyncio.run(main())

# 从结果我们可以看到，程序先运行test_a(),再去运行test_b() 因为sleep阻塞了线程，仍然相当于同步
# 下面对程序进行改进

print("-"*20)


# 2.
async def test_a1():
    for i in range(5):
        _start_time=time.time()
        # 此时的time.sleep是cpu级别的io过程，使程序看上去是同步，事实上sleep函数也可以异步
        await asyncio.sleep(random.random()*2)
        _end_time=time.time()
        print("这是\'test_a1()\'函数的第{}循环，随机休眠时间为{}".format(i+1,_end_time-_start_time))
    return "在你生命中扮演的角色"


async def test_b1():
    for i in range(5):
        _start_time=time.time()
        # 此时的time.sleep是cpu级别的io过程，使程序看上去是同步，事实上sleep函数也可以异步
        await asyncio .sleep(random.random()*2)
        _end_time=time.time()
        print("这是\'test_b1()\'函数的第{}循环，随机休眠时间为{}".format(i+1,_end_time-_start_time))
    return "太模糊了"


async def main1():  # 主函数也要声明成异步函数，接收其他协程函数的返回值
    # 使用gather函数，批量执行协程函数，将其返回值列表给到result
    start_time=time.time()
    result= await asyncio.gather(test_a1(),test_b1())   # await关键字 拿到test_a(),test_b()返回值并通过gather函数成为列表
    print(result)
    end_time = time.time()
    print(f"共耗时{end_time-start_time}")

asyncio.run(main1())
