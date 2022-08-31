#user input using while loops

# this is difficult in the earlier progression, might want to re visit ch.7 

# height = 67 this is changing the while loop to false. false will run the loop until the next parent code block!!!!!!!!!!!!!!!!!!!
height = 55
height = int(input("please state your height?\n")) # you must wrap the input() to int(); int(input())...
# height = int(input("please state your height?\n")) # you must wrap the input() to int(); int(input())...

while height < 60:
    height += 1
    # print("this will print infinite amout of times")
    if height < 58: # if the hight is less than 58 inches then you continue
        continue
    print(f"you are {height} inches tall \n and you are too short to ride!")
    print("drink my magic potion")
    if height == 55:
        break
    elif height == 60:
        break
    else:
        print("you are already tall enough to ride this ride!!!!!!")
print(f"{height} in. is the right height!\n C'mon and ride the ride you {height} in. tall person!")
print("thanks for riding...") # this 

while True:
    response = input('say high [h], say goodbye[g], say quit[q]')
    if response.lower() == 'h':
        print("hello there")
    elif response.lower() == "q":
        print("thats a good quitter!")
        break
    else:
        print("invallid option...")
        
        #imagine a video game open world and you just got done talking to the merchant and you used an escape sentace...
       
