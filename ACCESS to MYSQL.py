import pyodbc
import pymysql


# 写的一个类 password需要输入自己MySQL的密码
class mysql(object):
    def __init__(self, host='localhost', user='root', port=3306, charset='utf8', passwd='xxx'):
        self.host = host
        self.user = user
        self.port = port
        self.charset = charset
        self.passwd = passwd

    def create_database(self, dbname):  # 库的创建传入库名
        conn = pymysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            port=self.port,
            charset=self.charset
        )
        # 获取游标
        cursor = conn.cursor()
        sql = f'create database if not exists {dbname} default character set utf8'
        cursor.execute(sql)  # 提及语句
        conn.commit()  # 提及更改
        # 关闭
        cursor.close()
        conn.close()

    def create_T(self, dbname, sql_table):  # 表的创建传入库名和，建表语句
        conn = pymysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            port=self.port,
            charset=self.charset,
            db=dbname
        )
        # 获取游标
        cursor = conn.cursor()
        cursor.execute(sql_table)
        conn.commit()  # 提及更改
        # 关闭
        cursor.close()
        conn.close()


if __name__ == '__main__':
    base = mysql()  # 创建对象
    base.create_database('work2009')  # 建立一个叫work2009的数库
    # 创建access数库连接
    DBfile = r"C:/Users/22248/Desktop/原始数据库/AdventureWorks2008.mdb"  # 数据库文件
    conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;")
    cursor = conn.cursor()
    # 准备3个列表容器
    tables = []  # 表名容器
    fields = []  # 字段容器
    field_str = []  # 字段封装成sql语句容器
    # 获取所以表名
    for table_info in cursor.tables(tableType='TABLE'):
        tables.append(table_info.table_name)
    # 遍历所有表
    for table in tables:
        for row in cursor.columns(table):
            fields.append(row.column_name)  # row.column_name得到表的字段
        for field_r in fields:  # 将一个表的字段封装成字符串
            s = f'{field_r} char(120)'  # 做成sql语句形式
            field_str.append(s)
        fields.clear()  # 清理字段容器，准备装下一个表的字段
        m = ','.join(field_str)  # m为字符串格式str
        base.create_T('work2009', f'create table {table}({m})')  # 在work2009建立表，这是sql,语句f'create table {table}({m})'
        field_str.clear()  # 清理字段sql语句容器，准备装下一个表

# 以上工作主要完成在mysql中表的创建，并给出了列名和数据类型，剩下的就是往里面填充数据

# 数据写入
# 创建access数据库库连接
DBfile = r"C:/Users/22248/Desktop/原始数据库/AdventureWorks2008.mdb"  # 数据库文件
conn_A = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;")
cursor_A = conn_A.cursor()
# 创建mysql数据库连接
conn_M = pymysql.connect(
    host='localhost',
    user='root',
    passwd='xxx',  # 输入自己的mysql密码
    port=3306,
    db='work2009',
    charset='utf8'
)
cursor_M = conn_M.cursor(pymysql.cursors.DictCursor)
# 准备3个容器
tables = []
fields = []
field_str = []
# 获取所有表名
for table_info in cursor_A.tables(tableType='TABLE'):
    tables.append(table_info.table_name)
# 遍历所有表名
for table in tables:
    for row in cursor_A.columns(table):
        fields.append(row.column_name)
    # 进行sql语句拼接
    f = ','.join(fields)
    s = ','.join(['%s' for i in range(len(fields))])
    sql = f'insert into {table}({f}) values({s})'  # 相比于上面，这里给出了values的值，也就是将数据输入进去
    SQL = f"SELECT * from {table};"
    # print(sql)
    # print(SQL)
    # 获取到表的数据
    for row in cursor_A.execute(SQL):  # 选中access表中的每一行数据
        field_str.append(row)   # 将该行数据存入容器中
    cursor_M.executemany(sql, field_str)  # 传入多条数据 用到executemany函数
    conn_M.commit()  # 提交更改

    fields.clear()
    field_str.clear()
cursor_A.close() # access游标关闭
conn_A.close()   # access数据库关闭
cursor_M.close()  # mysql游标关闭
conn_M.close()    # mysql数据库关闭