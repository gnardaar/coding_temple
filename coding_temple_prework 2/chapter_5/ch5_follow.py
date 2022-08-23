#booleans are either on or off true or false "0","1"
from pickle import TRUE


my_bool = True
my_bool = False #use capital T and F
print(my_bool)
print(bool(10))
print("dog" == "cat")
print("dog" == "Dog".lower())
print("dog" == "Dog".upper())
print(4>6)
print(4<=45)
print(5<20==20)
letter="b"
print(letter>"a")#true
print(letter>"b")#false
print(ord("a"))
print()
x= 8
y=9
print(x==y)
print(x!=y)
print(not x==y)
# if BOOLEAN OR BOOLEAN EXP:
#     CODE BLOCK FOR IF TRUE
#   ELSE:
#       CODE BLOCK FOR IF FALSE    

height = 73
if height < 60:
    print("you are too short!")
    print("but get off my ride")
elif height > 72:
    print("you are too tall get off!")
else:
    print("you are a good hieght for this ride... unlike those other than that shorty mcShortens over there!!!!")
    
diff_heights = [5.7,5.5,6,6.5,7,8]
for height in diff_heights:
    print(height)
    if height > 6:
        print("nice going!")
    elif height == 6:
        print("cool dude whatever!")
    else:
        print("kick rocks!")
