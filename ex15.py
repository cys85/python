# 导入模块
from sys import argv

# 接受filename 参数
script, filename = argv

# 打开文件
txt = open(filename)

# print的打印提示
print(f"Here's you file {filename}:")
# 打开文件并且打印文件内容
print(txt.read())

txt.close()
# 提示
print("Type the filename again:")
# 再次输入文件名称
file_again = input("> ")

# 再次打开文琴
text_again = open(file_again)

# 再次读取文件内容
print(text_again.read())
text_again.close() 