my_string = "hello there!"
my_string_2 = "hellothere"
print(my_string == my_string_2)
print(my_string != my_string_2)

print(my_string == my_string_2.lower())
print(my_string <= my_string_2)




print(my_string >= my_string_2)
print(my_string <= my_string_2)


print(my_string > my_string_2)
print(my_string < my_string_2)

print(my_string > my_string_2 and my_string == my_string_2)
print(my_string < my_string_2 or my_string != my_string_2)
    
    
listOfStrings = ['clank' , 'hit', 'smash', 'bang', 'boom', 'boop']
    
if listOfStrings.count("hit") > 0 :
    print("Yes, 'hit' found in List : " , listOfStrings)
    
if listOfStrings.count("zoom") < 1:
    print("no, 'zoom' found in List : " , listOfStrings)
    

    