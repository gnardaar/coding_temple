
my_list = []
print(type(my_list))
my_list = list()
print(type(my_list))
#  index   0 1  2   3    4
numbers = [2,6,10, 12.5, 0]
print(numbers)
print(type(numbers))

print(type(numbers[0]))  #this checks the type of the first number in the array wich is 2
print(type(numbers[0]*15.6)) #taking the num from the array and * it with a float to get a class of float

print(numbers[3])
print(type(numbers[3]))

foods = ['tacos', 'pizza', 'dim sum', 'susi']
print(foods[1])
print(type(foods[1]))
print(foods[0].upper())

x=5
y=2
z='hello'

random_list = [x,y,z]
print(random_list[0])
print(type(random_list[0]))
print(random_list[1])
print(type(random_list[1]))
print(random_list[2])
print(type(random_list[2]))

my_fav_num = str(random_list[1])
print(my_fav_num)

foods = ['tacos', 'pizza', 'dim sum', 'susi']
foods.append("cheeseburger")
print(foods)

foods = ['tacos', 'pizza', 'dim sum', 'susi']
foods.insert(0, "boogers") #0 is the 2nd arguement other that what you want to add
print(foods)


foods = ['tacos', 'pizza', 'dim sum', 'susi']
foods.insert(0, "boogers") #0 is the 2nd arguement other that what you want to add
print(foods)
foods.remove("boogers")
print(foods)


foods = ['tacos', 'pizza', 'dim sum', 'susi']
del foods[2]
print(foods)

foods = ['tacos', 'pizza', 'dim sum', 'susi']
print(foods.pop())

# sort method these are all sorted in place
foods = ['tacos', 'pizza', 'dim sum', 'susi']
print(foods.sort())
print(foods)
print(foods.sort(reverse=True))
print(foods)

# sorted is going to be sorted out of place
foods = ['tacos', 'pizza', 'dim sum', 'susi']
print(sorted(foods ,reverse = True))
print(foods)

