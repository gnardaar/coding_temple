my_dict = {}
my_dict = dict()
my_dict = {
    "key" : "value"
}

my_dict = dict(key="value")

person = {
    "name":"steve",
    "weight" : 155.5,
    "height" : 70,
    "foods" : ["apples","hamburger","cookies"],
    "ice_cream" : {
        "vinilla" : "yummy",
        "mint" : False,
        "chocolate" : True
    },
    10 : "this is an integer key"
        }
#name of dict[key]
person.append('name','andy')
print(person['name'])
print(type(person['name'].upper()))
print(type(person["name"]))
print(type(person["weight"]))
print(person["weight"])
print(type(person["foods"]))
print(person["foods"][1])
print(type(person["name"].upper()))
print(type(person))
print(person["ice_cream"]["vinilla"])
print(type(person["ice_cream"]["vinilla"]))
print(person.get("candies","no candy was found")) #the .get()is a the way to check if there is a value in your program without crashing it
#changing the key 
person["name"] = "Andy"
print(person["name"])
person.update({
    "candies": ["gum", "caremel apple", "sour patch kids"]
})
print(person["candies"][1]) 
print(person)   
del person["candies"]
print(person)
for key in person:               #this loops through the keys in a dict
    print(key)
    print(type(key))
    print(person[key])
print(person.values())
for value in person.values():    #this loops through the values of a dict
    print(value)
    print(type(value))
for tup in person.items():  #this loops through the values of a dict
    print(tup)
print(person.items()) 

for key, value in person.items():  #this loops through the values and keys to add the data right next to eachother  of a dict
    print(key, end=": ")
    print(value)


for key, value in person.items():  # this loops through the person dict and checks if there is a key value of a list data type. then 
                                    #it returns whatever the list started with, in this case foods!
    if isinstance(value, list):
        print(f"the list is at {key}")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
       print(alien)
       
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
if 'erin' not in favorite_languages.keys(): #you dont have to specify keys() the default is keys
    print("Erin, please take our poll!")
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()):
       print(name.title() + ", thank you for taking the poll.")
        