# 有100辆车
cars = 100
# 一个车有4个空位置
space_in_a_car = 4
# 有30名司机
drivers = 30
# 有90名乘客
passengers = 90
# 有多少辆车没有司机
cars_not_driven = cars - drivers
# 车辆的司机
cars_driven = drivers
# 载客容量 
carpool_capacity = cars_driven * space_in_a_car
# 每辆车的平均乘客量
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people tody.")
print("We hava", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


i = 20
x = 30
j = 2

print(i * x / j)