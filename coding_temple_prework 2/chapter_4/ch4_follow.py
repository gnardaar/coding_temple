foods = ['tacos', 'pizza', 'dim sum', 'susi']
print(foods[-1]) # this returns the value of the last item of the index in array.

# this is the first for loop
for food in foods:
   print(f"I like to eat", food) # " f'' is important to print string for every index in foods!!!!"
#    print(f"I like to eat {food}") this is the same thing as the function above ^^^
   print(food)
   print(type(food))
    
for food in foods:
   print(f"I like to eat {food} because it\'s yummy!")
   if food == "pizza":
       break
        # print(food)
for food in foods:
   print(f"I like to eat {food} because it\'s yummy!")
   if food == "pizza":
       continue # continue really just skips the value of the index and just moves on with its life... life is short for a for loop... :'(
           
           
# Looping with the index

for index in range(len(foods)):
    print(index)
    print(foods[index])
    print(list(enumerate(foods))) #dang okay thats pretty cool syntatical sugar... Pretty sweet!!! TUPLE : multiple items each!
# for index, food in enumerate(foods):
for index, food in enumerate(foods):
    print(f"my number {index+1} favorite food is {food.title()}")
#my number 1 favorite food is Tacos ^^^
# my number 2 favorite food is Pizza
# my number 3 favorite food is Dim Sum
# my number 4 favorite food is Susi

print(list(range(4))) # this creates a list/ initilize a list
print(len(foods)) 
my_tup = 1, 2
print(type(my_tup))
print(my_tup)
my_tup = type((1,2))
print(my_tup)

# slicing()
my_string = "hey there guys lets learn python"
my_foods = ['tacos', 'pizza', 'dim sum', 'susi']
new_foods = my_foods[:]
print(my_string[1:5]) # returns ey t
print(my_string[::2]) #  get every other letter in the string starting with index 0
print(my_string[::-1]) #this is going to make the string completely backwards!
print(my_string[8:4:-1]) #this is a slice() while the string is backwards!!!! buet!
foods = ['tacos', 'pizza', 'dim sum', 'susi']

print(foods[0:5]) # this counts the index in the array

my_tup = 2, 5
print(my_tup)
my_tup = my_tup + (3,4)
print(my_tup)