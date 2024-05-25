print("hello world")
# creating a variable in python
#JS let or const, boolean or all other ones
#python variable below
# You need to use str for numbered variables str(age)
# shift enter or right click to run single or multiple lines of codes
name = "Blake"
last_name = "Turner"
age = 100
found = True
total = 12.99
country = "USA"
print(name + " " + last_name + " " + "is" + " " + str(age))

#if/else statement
#JS if(age<100){ console.log("no worries youre not that old")}
#Py
if age < 99:
    print("no worries youre not that old")
    print("inside of the if")
elif age > 101:
    print("Congrats youre a century")
else:
    "I dont know how you got here"
    
print("Im outside of the if statement")

#functions
#function name_of_the_function() ---> this is JS
#python function
def say_hello():
    print("Hello there!")

def say_good_bye(name):
    print("Good bye" + " " + name)

#try to print "hello my name is" age "and im from" + country
def user_input(name,country,age):
    print("hello my name is " + name +" and" + " I am " + str(age) +" years old and i am from " + country)

#Call the function
say_hello()
say_good_bye(name)
user_input(name,country,age)





