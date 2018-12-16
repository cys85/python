
def callMe(name): 
  print(f'You will called: {name}')


#1 
callMe('cys')

#2
name = 'cys'
callMe(name)

#3
name = 'cys'
callMe(name + 'jyn')

#4 
name = input("name> ")
callMe(name)

#5

name1 = 'cys'
name2 = 'jyn'

callMe(f"{name1} && {name2}")

#6
file = open('ex16_sample.txt')
data = file.read()

callMe(data)

#7 
callMe("cys && {}".format('jyn'))

#8
