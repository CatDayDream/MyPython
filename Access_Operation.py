import pyodbc

# file_path是access文件的绝对路径。
file_path = r"J:\SharePool\PD\11_ProductProduction\02_DailyPlan\Production_Material_Defect\FY2024 production order\SPA_ProductionDatabase.accdb"
# 链接数据库
conn = pyodbc.connect(u'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + file_path)
# 创建游标
cursor = conn.cursor()

# tb_name是access数据库中的表名
tb_name = "ProductionData"
cursor.execute('select ID from %s' % tb_name)
# 获取数据库中表的全部数据
data = cursor.fetchall()
print(data)
# 查看数据的字段名
field_list = []
for field in cursor.description:
    field_list.append(field[0])
print(field_list)

# 关闭游标和链接
cursor.close()
conn.close()
