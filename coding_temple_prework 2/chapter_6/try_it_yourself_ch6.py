alien_0 = {
    "color" : "green",
    "points" : 5
}
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

alien_0 = {
    "color" : "green",
    "points" : 5,
    "original x_position": 0,
    "y_position":25,
    "speed": "medium"
}

person = {
    "first_name":"Andy",
    "last_name":"Kraus",
    "age":28,
    "city":"denver",
}
for key, value in person.items():
    print(key,end=":\n")
    print(value,end="\n")
    
friends_fav_numbers = {
    "jessica":"blue",
    "matt":"green",
    "goerge":"red",
}
for key , value in friends_fav_numbers.items():
    print(key, value)
    
programming_words = {
    "\nattribute:\n" : "Function objects that define corresponding methods of its instances. They are used to implement access controls of\n the classes.\n",
    "tuple:\n" : "Used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of\n data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and\n unchangeable.\n",
    "return:\n" : "A special statement that you can use inside a function or method to send the function's result back to the caller.\n A return statement consists of the return keyword followed by an optional return value.\n",
    "class:\n" : "a code template for creating objects. Objects have member variables and have behaviour associated with them.\n In python a class is created by the keyword class . An object is created using the constructor of the class.\n",
    "elif:\n" : "For short for else if. It allows us to check for multiple expressions. If the condition for if is False,\n it checks the condition of the next elif block and so on. If all the conditions are False , the body of else is executed.\n",
    "else:\n" : "The else keyword is used in conditional statements (if statements), and decides what to do if the condition is False.\n"
}

for key, value in programming_words.items():
    print(key.upper(),end=" \t")
    print(value)


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

print("\n")

new_pollers = ['susie', 'greg', 'bill', 'sarah', 'jose', 'phil', ]
for poller in new_pollers:
    if poller in favorite_languages.keys():
        print("Thank you for taking the poll, " + poller.title() + "!")
    else:
        print(poller.title() + ", what's your favorite programming language?")
aliens = []
for number_of_aliens in range(12):
    new_alien = {
        "color" : "green",
        "life" : 15,
        "points" : 12
    }
    aliens.append(new_alien["color"])
    print(aliens)
    for alien in aliens[:5]:
        print(alien)
    print(str(len(alien)))

programming_words.update({
    "string:\n" : "\ta string is a sequence of Unicode characters. Unicode was introduced to include every character in all languages and bring uniformity in encoding. You can learn about Unicode from Python Unicode.\n",
    "length:\n" : "\tDescription. Python dictionary method len() gives the total length of the dictionary. This would be equal to the number of items in the dictionary.\n",
    "lambda:\n" : "\tIn Python, a lambda function is a single-line function declared with no name, which can have any number of arguments, but it can only have one expression.\n Such a function is capable of behaving similarly to a regular function declared using the Python's def keyword.\n",
    "break:\n" : "\t'Break' in Python is a loop control statement. It is used to control the sequence of the loop. Suppose you want to terminate a loop and skip to the next code after the loop; break will help you do that.\n A typical scenario of using the Break in Python is when an external condition triggers the loop's termination.\n",
    "or:\n" : "\t The Python or operator evaluates both operands and returns the object on the right, which may evaluate to either true or false.\n"
})
print(programming_words)
for words, definition in programming_words.items():
    print(words.upper(), definition)

country_rivers ={
    "Tigris" : "Iran, Iraq, Turkey, and Syria",
    "Mississippi" : "United Sates Of America",
    "Amazon river" : "Brazil"
}
for key in country_rivers:
    if key in country_rivers:
        print(" The " + key.title() +", is in " + country_rivers[key], end=".\n"+"\n")
