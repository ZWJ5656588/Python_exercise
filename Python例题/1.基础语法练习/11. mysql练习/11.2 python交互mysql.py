import pymysql
# --1.数据库连接函数
def db_connect():
    # 创建数据库对象,连接数据库
    db=pymysql.connect(host='localhost',user='root',password='',db='test')

    # 使用数据库对象创建一个游标对象(用来执行sql语句,类似于子套接字)
    cursor=db.cursor()

    # 使用游标对象执行sql语句
    # 游标对象里面的excute(sql语句)方法可以执行sql语句
    cursor.execute('select version()')

    # 使用fetchone()获取单条数据
    data=cursor.fetchone()

    # 打印数据
    print(data[0])

    # 使用db对象关闭数据库连接
    db.close()


db_connect()


# --2. 创建数据表
def db_connect2():
    # 创建数据库对象,连接数据库
    db=pymysql.connect(host='localhost',user='root',password='',db='test')

    # 使用数据库对象创建一个游标对象(用来执行sql语句,类似于子套接字)
    cursor=db.cursor()

    # 通过sql创建一个数据表
    cursor.execute('drop table if exists employee')

    # 4. 组织创建表的sql语句
    sql="""
            create table employee
            (
            first_name varchar(20) not null ,
            last_name varchar(20),
            age tinyint,
            sex varchar(1),
            income decimal(5,2),
            create_time datetime
            );
            """
    # 执行sql
    try:
        cursor.execute(sql)
    except:
        print("执行失败")
    else:
        print('执行成功')
    finally:
        db.close()


db_connect2()


# -- 插入数据









# -- 4.查询数据
def query_data():
    # 打开数据库连接
    db = pymysql.connect(host='localhost', user='root', password='root', db='test')
    # 获取游标
    cursor = db.cursor()
    # 查询语句
    sql = "select * from employee where income > %d" % 10000
    try:
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()  # 获取全部数据
        print(results)
        for row in results:
            first_name = row[0]
            last_name = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            create_time = row[5]
            # 打印结果
            print(f'first_name: {first_name}, last_name: {last_name}, age: {age}, sex: {sex}, income: {income}, '
                  f'create_time: {create_time}')
    except Exception as e:
        print(f'查询错误: {e}')
    finally:
        db.close()


if __name__ == '__main__':
    query_data()


# -- 5.数据更新
def update_table():
    db = pymysql.connect(host='localhost', user='root', password='root', db='test')
    cursor = db.cursor()
    sql = "update employee set age=age+1 where sex='%s'" % '男'   # 不能写成age+=1,mysql不支持
    try:
        cursor.execute(sql)
        db.commit()
        print('数据更新成功...')
    except Exception as e:
        print(f'更新失败: {e}')
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    update_table()