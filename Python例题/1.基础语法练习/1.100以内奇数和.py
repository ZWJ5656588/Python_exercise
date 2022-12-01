#sum函数
print(sum(range(1,100,2))) #range是一种可以迭代的基本类型，且不可变
#sum（iterable[,start]),iterable——可迭代对象，start——指定的相加的参数,默认0
a=range(1,100,2)
print(type(a))  #<class 'range'>

#for循环
count=0
for number in range(100):
    if number%2==0:
        continue
    count+=number
print(count)

#while循环
count=0
number=1
while number<100 :
    if number%2!=0:
        count+=number
    number+=1
print(count)

#递归求和
def sum(x):
    if x>99:
        return 0
    else:
        return x+sum(x+2)
print((sum(1)))