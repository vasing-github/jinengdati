import xlrd

# 打开 .xls 文件
workbook = xlrd.open_workbook('userid.xls')

# 获取第一个工作表
sheet = workbook.sheet_by_index(0)

# 创建一个空字典
my_dict = {}

# 遍历工作表中的每一行
for row in range(1, sheet.nrows):
    # 获取姓名和 userid
    name = sheet.cell_value(row, 0)
    userid = sheet.cell_value(row, 1)

    # 将姓名和 userid 添加到字典中
    my_dict[userid] = name

# 打印字典
print(my_dict)
