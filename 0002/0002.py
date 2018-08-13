"""第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。"""

import MySQLdb

list_id = []

with open("../0001/file_id.txt", "r") as file:
    files = file.readlines()
    for content in files:
        list_id.append(str(content).replace("\n", ""))

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306)
    cur = conn.cursor()
    conn.select_db('test')
    cur.execute('create table if not exists activation_code(id int,uuid varchar(50))')
    for i in range(len(list_id)):
        cur.execute('insert into activation_code values(%s,%s)', (i, list_id[i]))
    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error as e:
    print("MySQLdb Error %d: %s" % (e.args[0], e.args[1]))
