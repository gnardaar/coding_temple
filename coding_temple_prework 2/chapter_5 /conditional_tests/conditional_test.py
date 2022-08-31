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
    
user_names = ["andy","admin","jack","ryan"]
admin_name = "admin"
for user in user_names:
    if user == admin_name:
      print("hello admin I hope your having a wonderful day!")
    elif user != admin_name:
      print("hello ",user)
    else:
        print('there are no users in the array. try adding one')
        
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, I hope that your having a good day!")
        else:
            print("Hello " + username + ", thank you for logging in again!")
else:
    print("We need to find some users!")
    
    
current_users = ["gnardar","Joshbess","cluckers123","jonny Gash","jessica","brad"]
new_users = ["cluckers123","gnardar","mr.madhouse","Brad"]    
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry there, " + new_user + ", that name is not availible.")
    else:
        print( new_user + " is still available.")
    

list_of_numbers = [1,2,3,4,5,6,7,8,9]
for number in list_of_numbers:
    if number == 1:
        print(" \n"+str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + 'th')
        
        
        #there is many different programs/apps that I would like to develope. one would be a video journaling app,
        # working with video and using the users phone or laptop would be non the less interesting.
        #using the skills inside of this course will alow me to do that on my own!
        
x = 5
print('a spoon ')
if x == 4:
    print('full of ')
else:
    print('make the medicine')
elif x>=4:
    print('sugar')
        