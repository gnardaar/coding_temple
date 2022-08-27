#TRY IT YOURSELF
alien_color = "yellow"
if alien_color == "yellow":
    print("congrats you just earned 5 points")
else:
    print("")
    
alien_color = "blue"
if alien_color == "yellow":
    print("congrats you just earned 5 points")
elif alien_color == "blue":
    print("congrats you just got 10 points!")
    
alien_color = "red"
if alien_color == "yellow":
    print("congrats you just earned 5 points")
elif alien_color == "blue":
    print("congrats you just got 10 points!")
else:
    print(alien_color.upper() + "!" + " that is correct!")
    print("very good you just recieved 15 points!")
    
age = 66
if age < 2:
    print("your just a baby!")
elif age >=2 and age <4:
    print("you are a toddler.")
elif age>=4 and age < 13:
    print("you are a kid")
elif age >=13 and age < 20:
    print("your an teen... don't get use to it!")
elif age >= 20 and age < 65:
    print("you are an adult... get use to that!")
else:
    print("you're old dude! jk you know I love you!")
    
fav_fruits = ["apples", "bannanas", "grapes", "mangos","peaches"]
fav_fruit = fav_fruits[0]
print(fav_fruit)
if fav_fruit == "bannanas":
    print("you guessed wrong boy!")
elif fav_fruit == "grapes":
    print("still wrong!")
elif fav_fruit == "mangos":
    print("man thats not it either!")
elif fav_fruit == "peaches":
    print("man thats not it either you are not that good at guessing! \nthink more red")
else:
    print("you got it its apples")
    print("I really like apples!!")
    
car = "subaru"
#true
print('my prediction is true')
print(car == "subaru")
print('my prediction is true')
print(car >= "subaru")
print('my prediction is true')
print(car != "audi")
print('my prediction is true')
print(car == "Subaru".lower())
print('my prediction is true')
print(car == "subaru" and car == "Subaru".lower())

#false
print('my prediction is false')
print(car <= "Subaru" )
print('my prediction is false')
print(car == "audi")
print('my prediction is false')
print(car != "subaru")
print('my prediction is false')
print(car > "subaru")
print('my prediction is false')
print(car == "subaru" and car =="audi")