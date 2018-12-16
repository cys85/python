# 人的类型
types_of_people = 10
# 这有{types_of_people}种人
x = f"There are {types_of_people} types of people." # 1

# 变量 binary
binary = "binary"
do_not = "don't"
y = f"Those who know (binary) and those who {do_not}." # 2

# 打印 x
print(x)
# 打印 Y
print(y)
print(f"I said: {x}") 
print(f"I also said: '{y}'")

hilarious = "False"
joke_evaluation = "Isn't that joke so funny?! {}" # 3

# 格式化替换
print(joke_evaluation.format(hilarious))

w = "This is the left side of"
e = "a string with a right side."

# 字符串拼接打印
print(w + e) # 4