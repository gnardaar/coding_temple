#TRY IT YOURSELF
friends = ["Micheal", "Zach", "Josh", "Sabine"]

message_1 = " Thank you Micheal for beleiving in me with every step!"
message_2 = " Thank you Zach for being a goofball!"
message_3 = " Thank you Josh for teaching me how to skateboard!"
message_4 = " Thank you Sabine for being the cutest doggy!"


good_girl_str = " (THAT IS A GOOD GURL!)\n" 

print(friends[0]+',\n\t' + message_1)
print(friends[1]+',\n\t' + message_2)
print(friends[2]+',\n\t' + message_3)
print(friends[3]+',\n\t' + message_4 + good_girl_str)


# my own list
bonus_statment = "\tWhere do I get one?\n"


fav_transports = ['skateboard','Rollercoasters','waterslides','Bamboo train','Coco Taxi ']
transport_statment_1 = "was the first thing that I ever fell in love with!\n"
print("A "+fav_transports[0] + " " + transport_statment_1 )
transport_statment_2 = " are extremly fun and I would like to own one...\n"
print(fav_transports[1] + transport_statment_2)
transport_statment_3 = "are extremly fun and I would like to own one...\n"
print(fav_transports[2] + transport_statment_3)
transport_statment_4 = " are extremly fun and i would like to own...two?\n"
print(fav_transports[3] + transport_statment_4 + bonus_statment)


#TRY IT YOURSELF
dinner_guests = [' Fank Zappa\n', ' Nikola Tesla\n', ' Elvis Presly\n']
last_resort_guest = " Weird kid from across the street,\n "
guest_invitations_1 = "\tHello would you like to come over for dinner later this week?  \n"
print("dear," + dinner_guests[0] + guest_invitations_1)
print("from: Mr. zappa,\n" + "\tdude duh!\n")
guest_invitations_2 = "\tHello would you like to come over for dinner later this week?  \n"
print("dear," + dinner_guests[1] + guest_invitations_2)
print("to YOUR PARTY!\n NO!!!!!!\n -Nikola Tesla")
print('You should just invite that kid that that nobody understands why he says all the time, "I am the president of the United States Of \'Merica!\n')
print("okay! fine\n")
print("dear," + last_resort_guest + guest_invitations_1 + "Or whatever...\n")
print(' The blue Cryon has good flavor of razzberries! I\'ll bring some over, I baked a pie...\n')
print("hmmmmmmmmmmmm?")
print("fine.")

last_resort_guest = " Weird kid from across the street,\n "
# dinner_guests = [' Fank Zappa\n', ' Nikola Tesla\n', ' Elvis Presly\n']
del dinner_guests[1]
dinner_guests.insert(1,last_resort_guest)
print(dinner_guests)
print('there will be more dinner guest arriving!')
dinner_guests.insert(0,"Dale")
dinner_guests.insert(1, "Hank\n")
dinner_guests.append("Boomhauer\n")
print(dinner_guests)

print("Dang it " + dinner_guests[0] + "!\n"  )
print("Hello " + dinner_guests[1])
print("Hello " + dinner_guests[4])  

print("Well,\n  it looks as though I only have 2 guests over, that means , Frank and Elvis can stay, it seems as if my table shrank!!! \n Also I only have three tv dinners to spare... so the rest of you kick rocks!\n")
dinner_guests = [' Fank Zappa\n', ' Nikola Tesla\n', ' Elvis Presly\n']
del dinner_guests[1]
print(dinner_guests)

print("do we have really just TV dinners?? - " + dinner_guests[0])
print("Man you see here I\'m the king and what I say goes...\n Let\'s ditch this sucker, and how about me and you just get loaded up at the bar! sound good there Amigo? - " + dinner_guests[1])
print("yeah sure man! - " + dinner_guests[0])
del dinner_guests[0]
del dinner_guests[0]

dinner_guests.append("THE END")

print (dinner_guests)
del dinner_guests[0]
print(dinner_guests)

print('I apologize for all the errors in my writing proof reading gets a little harder when your in the terminal, and for making you read all that. \n')

#DO IT YOURSELF

placees_to_visit = ["Japan","Ireland","Switzerland","Guam", "Chile"]
print(sorted(placees_to_visit))
print(placees_to_visit)
placees_to_visit
print(placees_to_visit.sort(reverse=True))
print(placees_to_visit) #you have to print it cause the sort method returns "none" otherwise
placees_to_visit = ["Japan","Ireland","Switzerland","Guam", "Chile"]
print(placees_to_visit.reverse())
print(placees_to_visit)
print(placees_to_visit.reverse())
print(placees_to_visit.sort())
print(placees_to_visit)
print(placees_to_visit.sort(reverse=True))
print(placees_to_visit)

numb_of_guests = len(dinner_guests)
print(numb_of_guests)
# dinner_guests.append("me",",myself"," and I")
# print(dinner_guests)


random_list = ["Andes Mountains", "France", "Mississippi River", "Burn-side skatepark"]
random_list.append("Disney World")
print(random_list)
random_list.pop()
print(random_list)
random_list.sort()
print(random_list)
random_list.pop()
print(random_list)
random_list.reverse()
print(random_list)
random_list.remove("France")
print(sorted(random_list))
numb_of_things = len(random_list)
print(numb_of_things)
del random_list[0]
print(random_list)


#I have def recieved an index error on my program no need to replicate it hahahhahaha