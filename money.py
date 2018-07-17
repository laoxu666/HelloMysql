import pymysql


def get_money():
    client = pymysql.Connect(host='localhost', user='root', password='rock1204', port=3306, db='HelloPython',
                             charset='utf8')
    cursor = client.cursor()

    try:
        cursor.execute("update Account set money=40 where name='张三';")
        cursor.execute("update Account set money=110 where name='李四';")
        cursor.execute('select * from Account;')
    except Exception as e:
        print(str(e))
        # 出错 打印异常并回滚
        client.rollback()
    else:
        # 成功 提交数据
        client.commit()

    p_moneys = cursor.fetchall()
    for p_money in p_moneys:
        print(p_money)


if __name__ == '__main__':
    get_money()
