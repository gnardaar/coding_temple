# #try it yourself
# what_car = "subaru"

# what_car = input("what kind of car would you like?")
# print(f"I would like a {what_car} please")
# print(f"hold on lemme see if we gots dat {what_car}!")



max_num_of_guest = "8"
num_of_guests = (input(f"would there be more than 8 joining all of you?"))
while num_of_guests !=max_num_of_guest:
    print(num_of_guests)
    print("table for " + num_of_guests + " please come this way!")
    break
if num_of_guests == max_num_of_guest:
    print("you will have to wait people!!!!! ")
    
