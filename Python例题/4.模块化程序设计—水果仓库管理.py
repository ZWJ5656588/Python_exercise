#自上而下，利用主程序，子程序等框架将主要结构流程描述出来
""""编写程序fruit_warehouse,
1.添加水果信息，（名称，重量，日期等），字典套列表
2.列出当前所有水果，遍历
3.查询水果，输入水果名称，打印，if print
4.删除水果,pop & remove,操作列表
"""
def get_option():
    print("1:添加水果信息")
    print("2:显示所有水果")
    print("3:添加水果信息")
    print("4:添加水果信息")
    print("5:添加水果信息")
    while True:
        option=int(input("请输入数字1-5:"))
        if 1 <= option <= 5 :
            break
    return option


def add_friut(): #添加水果信息
    pass


def search_all_fruits():
    pass


def query_fruit():
    pass


def del_fruit():
    pass


def main():#主程序入口，其余函数均为主函数的嵌套函数
    while True:  #与break连用
        alternative=get_option()
        if alternative == 1:
            add_friut()
        elif alternative == 2:
            search_all_fruits()
        elif alternative == 3:
            query_fruit()
        elif alternative == 4:
            del_fruit()
        elif alternative == 5:
            print("退出系统")
            break
main()


