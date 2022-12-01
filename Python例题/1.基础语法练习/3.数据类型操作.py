#1.#将字符串“a.e.f.j,j,s,u,o"转换成列表并进行倒叙，最终输出字符串
str1="a.e.f.j,j,s,u,o"
list1=str1.split(".") #split函数返回一个列表，且无法进行空字符分割，默认空格
print(list1)
list2=list1[3].split(",")
print(list2)
del list1[3]
list3=list1+list2
print(list3)
list3.sort(reverse=True) #返回值为None,不能直接打印
print((list3))
str2="".join(list3) #join方法返回拼接的字符串值
print(str2)
print("-"*20)

list5=[1,2,3,4,5]
str5=str(list5)
print(str5)
print(type(str5))

print("-"*20)


help(issubclass)
"""看方法文档的方法"""

print('-'*20)

