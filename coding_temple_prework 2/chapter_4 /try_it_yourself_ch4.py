#DO IT YOURSELF
pizza_type = ["pepperoni", "sausage", "pinapple"]
for pizza in enumerate(pizza_type):
    print(pizza)
    print(f"I really enjoy {pizza_type[0]} pizza is my very favorite pizza")
    print(f"I really enjoy {pizza_type[1]} pizza is my 2nd favorite")
    print(f"I really enjoy {pizza_type[2]} pizza is my least favorite! Yuck!")
    break
simular_animals = ["tiger", "house-cat", "lion","lyger","a ware-lion"]
for animal in simular_animals:
    
    if animal != "house-cat":
        print(f"a {animal} would not be a great pet.") 
    if animal == "house-cat":
        print(f"a {animal} would be a great pet.") 
        

        continue
print("\nalot of these animals are dangerous kittys and the should not be house pets, unless your a pro boxer, or a shape shifter!\n")

squares = [value**2 for value in range(1,11)]
print(squares)
squares[1:10] = []
squares[1:10] = squares + [4,5.6,]
print(squares)


numerals = [value+1 for value in range(0,20)]
print(numerals)
copied_numbers = numerals[:]
print(copied_numbers)
copied_numbers.append("21")
print(copied_numbers)

#TRY IT YOURSELF
print("the first three items from the beginning of the list are:")
cities = ["london", "munich", "cancun", "paris", "tokyo"]
print(cities[1])
print(cities[2])
print(cities[3])

pizza_type = ["pepperoni", "sausage", "pinapple"]
friend_pizza_type = ["less cheese", "pineapple", "no pepperroni"]

pizza_type.append("barbecue")
friend_pizza_type.append("Crust")

print("and you pizza is:\n")

for pizza in pizza_type:
    print(pizza)
    
print("and the friends pizza is:\n")

for friend_pizza in friend_pizza_type:
    print(friend_pizza)