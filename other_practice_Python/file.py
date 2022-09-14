num1 = 42 #this line is showing integer values
num2 = 2.3 #this line is shwoing decimal values 
boolean = True #boolean will show both values to be true
string = 'Hello World' # Hello World is a string value 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #this is a list 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #this is a dictioinary 
fruit = ('blueberry', 'strawberry', 'banana') #What are these? 
print(type(fruit)) #print function
print(pizza_toppings[1]) #print funciton
pizza_toppings.append('Mushrooms') #Print function
print(person['name']) #print array variable 
person['name'] = 'George' #name is george
person['eye_color'] = 'blue' #person eye color
print(fruit[2]) 

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)



# - variable declaration
# - log statement
# - type check
# - length check
# - comment
#     - single line
#     - multiline
# - Data Types
#     - Primitive
#         - Boolean
#         - Numbers
#         - Strings
#     - Composite
#         - List 
#             - initialize
#             - access value
#             - change value
#             - add value
#             - delete value
#         - Tuples
#             - initialize
#             - access value
#             - change value
#             - add value
#             - delete value
#         - Dictionary
#             - initialize
#             - access value
#             - change value
#             - add value
#             - delete value
# - conditional
#     - if
#     - else if
#     - else
# - for loop
#     - start
#     - stop
#     - increment
#     - break
#     - continue
#     - sequence
# - while loop
#     - start
#     - stop
#     - increment
# - function
#     - parameter
#     - argument
#     - return

# * Bonus: Errors

# - NameError: name <variable name> is not defined
# - TypeError: 'tuple' object does not support item assignment
# - KeyError: 'favorite_team'
# - IndexError: list index out of range
# - IndentationError: unexpected indent
# - AttributeError: 'tuple' object has no attribute 'pop'
# - AttributeError: 'tuple' object has no attribute 'append'
# - Tuples
#     - change value
#     - add value
#     - delete value