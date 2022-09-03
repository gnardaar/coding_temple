def greet_user():
    print("hello")
greet_user()

def say_goodbye():
    print("goodbye")
say_goodbye()    

def greetings():
    return "hello"
print(greetings())
greetings()

def hello(name, age):
    
    print(f"hello {name}, you are {age} years old!")
hello("andy",222)

def hello_2(name, age):     # swap the variable names and the pooter gets messed up!
    
    print(f"hello {name}, you are {age} years old!")
hello_2(222,"andy")

def hello_3(name, age):     #assign the variables to the correct position
    
    print(f"hello {name}, you are {age} years old!")
hello_3(age = 222, name = "andy")


# def hello_der():
# hello_der()


# def ok_bye_now():
# ok_bye_now(

def greet_back(feeling):
    if feeling == "good?":
        print("awsome I feel great too")
    elif feeling == "eh":
        print("yeah momma told us there be days like this... hang in der kittin!")
    elif feeling == "bad":
        print("dude im sorry that must suck")
    else:
        print("that\'s too bad")
        
        #driver code
while True :
    response = input('what do you want to do??? say hello [H] say "eh" [g] say "bad" say [bad] press q to q[q]')
    if response.lower() =='q':
        say_goodbye()
        break
    elif response.lower()== "h":    
        name = input("what is your name?")
        age = input("what is you age?")
        hello(name, age)
    elif response.lower() == 'g':
        input('well that\'s too bad, bye now!')
        say_goodbye(name)
    elif response.lower():
        print("thats okay in this day and age!")
    elif response.lower() == "t" :
        feeling = input("how are you feeling today? ")
        greet_back(feeling)
    else:
        print("invalid input!")
    greet_back()




    