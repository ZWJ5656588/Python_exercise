scores=[('张三',89,90,59),('李四',99,49,59),
        ('赵武',99,60,20),('王二麻子',40,94,59),
        ('李雷',89,90,59),('李力',89,90,69),
        ('楚犀',79,80,76),('Neo',85,90,59),
        ('Abby',89,97,96)
        ]

def handle_filter(a):
        s=sorted(a[1:])  # 对列表中第二个到最后元素的三科成绩排序,返回的是一个新列表

        # 有两科在80以上，并且有一门在60分以下
        if s[-2]>80 and s[0]<60 :
                return True
        # 有1科成绩 90以上，另外两科60以下
        if s[-1]>90 and s[1]<60:
                return True
        # 有一科在90 分以上，且三门平均分在70以下
        if s[-1]<90 and sum(s)/len(s)<70:
                return True
        return False

# filter(function,iterable)
# 对iterable的每个item进行function函数的过滤定义，function返回值是bool类型，如返回Ture则进入filter函数生成的新的迭代器

new_list=filter=list(filter(handle_filter,scores))
print(new_list)