# 1. 通过异常捕获获得以下字符串里面的字母字符

str_1='d52a733i2327ha244i982d23s553b245'
letters_character_list=[]
for i in str_1:
    try:
        int(i)
    except:
        letters_character_list.append(i)

print(letters_character_list)

# 2.文件操作
with open('3.txt',mode='wt',encoding='utf-8') as f:
    f.write('大海\n小海\n红海')

# 方法一  将文件内容由硬盘全部读入内存修改,wt直接覆盖
with open('3.txt',mode='wt',encoding='utf-8') as f:
      f.write('蓝海\n紫海\n黄海')








