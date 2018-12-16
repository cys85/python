from sys import argv

script, input_file = argv

# 打印文件
def print_all(f): 
  print(f.read())

# 回滚至第一行
def rewind(f):
  f.seek(0)

def print_a_line(line_count, f):
  print(line_count, f.readline(), end = "")

# 打开文件
current_file = open(input_file, 'r', encoding='UTF-8')

print("First let's print the whole file:\n")

# 打印当前文件
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# 执行回滚
rewind(current_file)

print("Let's print three lines:")
# 当前行 + 1
current_line = 1
# 执行print_a_line函数
print_a_line(current_line, current_file)

# 当前行 + 1
current_line += 1
# 执行print_a_line 函数
print_a_line(current_line, current_file)

# 当前行 + 1
current_line += 1
# 执行pprint_a_line 函数
print_a_line(current_file, current_file)
