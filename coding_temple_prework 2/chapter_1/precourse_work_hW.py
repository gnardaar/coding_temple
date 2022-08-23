def hello_name(user_name):
    user_name = "paul"
    if user_name == "andy".title():
        print("hello, " + user_name)
    else:
        print("kick rocks! your not him!")
hello_name("Andy")

# def first_odds(numbers):
#     # numbers = list(range(1,100))
#     print(numbers)
# first_odds(list(range(1,100)))
# for odd in first_odds:
    
def first_odds():
    a = [5, 3, 2, 8, 1, 4]
    b = sorted([item for item in a if item%2 != 0])
    odd_int = 0
    for i in range(len(a)):
        if a[i] %2 != 0:
            a[i] = b[odd_int]
            odd_int += 1
            print(b)
first_odds()
def max_num_in_list_a():
    list_a = [1,2,3,4,5,6]
    max_number = 7
    
    print(max_number)
max_num_in_list_a()