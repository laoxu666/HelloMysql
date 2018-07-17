import pymysql

"""
(self, host=None, user=None, password="",
                 database=None, port=0, unix_socket=None,
                 charset='', sql_mode=None,
"""

def get_data():
    # 链接数据库
    client = pymysql.Connect('localhost', 'root', 'rock1204', 'HelloPython', 3306, charset='utf8')

    cursor = client.cursor()

    result = cursor.execute("show tables")

    # print(result)
    # for i in range(result):
    #     print(cursor.fetchone())
    # print(cursor.fetchall())

    tables = cursor.fetchall()
    for table in tables:
        print(table)


def get_home():
    client = pymysql.Connect(host='localhost', user='root',
                             password='rock1204', port=3306, db='HelloPython',
                             charset='utf8')
    cursor = client.cursor()
    cursor.execute("select * from Home;")
    homes = cursor.fetchall()
    for home in homes:
        print(home)


def get_persons():
    client = pymysql.Connect(host='localhost', user='root',
                             password='rock1204', port=3306, db='HelloPython', charset='utf8')
    cursor = client.cursor()
    try:

        cursor.execute("update Person set age=50 "
                       "where p_name ='uu';")
        cursor.execute("select * from Person")
        persons = cursor.fetchall()
        for person in persons:
            print(person)
    except Exception as e:
        print(str(e))
        client.rollback()
    else:
        client.commit()


if __name__ == '__main__':
    # get_data()
    get_home()
    # get_persons()
