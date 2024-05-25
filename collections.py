#list ----> arrays
color = ["white","red","yellow"]

print(color[1]) #it will print red [0,1,2]

#add to list
color.append("pink")

print(color)

#for loop
for current in color:
    print(current)

# for JS
#for(i=o;<color.legnth;i++)
#current = color[i]

#Dictionaries
me = {
    "first_name":"Blake",
    "last_name":"Turner",
    "age":28
}

#add to dictionary
me["color"]="Blue"
#modify
me["color"]="red"
me["age"]=29
#get value
print(me["first_name"]+" "+str(me["age"]))

print(me)


ages = [32, 74, 20, 69, 52, 26, 31, 77, 43, 73, 51, 57, 19, 79, 40, 34, 27, 23, 21, 44, 53, 55, 24, 36, 41, 47, 78, 46, 68, 75, 49, 83, 61, 60, 29, 56, 67, 17, 70, 81, 87, 38]

# print all the numbers 
#print all the numbers greater or equal to 21
#print how many numbers are greater than 21
def printall():
    count = 0
    for age in ages:
        if age >=21:
            print(age)
            count +=1
    print("there was "+str(count)+ "greater than 21")
#call the function
printall()

users = [

   {

       'id': 1,

       'name': 'Alice',

       'gender': 'female',

       'age': 25,

       'preferred_color': 'blue'

   },

   {

       'id': 2,

       'name': 'Bob',

       'gender': 'male',

       'age': 35,

       'preferred_color': 'GREEN'

   },

   {

       'id': 3,

       'name': 'Charlie',

       'gender': 'male',

       'age': 45,

       'preferred_color': 'Red'

   },

   {

       'id': 4,

       'name': 'Danielle',

       'gender': 'female',

       'age': 30,

       'preferred_color': 'YelloW'

   },

   {

       'id': 5,

       'name': 'Evelyn',

       'gender': 'female',

       'age': 20,

       'preferred_color': 'PuRplE'

   },

   {

       'id': 6,

       'name': 'Frank',

       'gender': 'male',

       'age': 28,

       'preferred_color': 'purple'

   },

{

       'id': 7,

       'name': 'Grace',

       'gender': 'female',

       'age': 31,

       'preferred_color': 'GREEN'

   },

   {

       'id': 8,

       'name': 'Henry',

       'gender': 'male',

       'age': 40,

       'preferred_color': 'BLUE'

   },

   {

       'id': 9,

       'name': 'Isabelle',

       'gender': 'female',

       'age': 27,

       'preferred_color': 'red'

   },

   {

       'id': 10,

       'name': 'Jack',

       'gender': 'male',

       'age': 24,

       'preferred_color': 'yellow'

   }

]

def printNames():
    for user in users:
        print(user["name"])

def printHowMany():
    female=0
    male=0
    for user in users:
        gender = user["gender"]
        if gender == "female":
            female +=1
        elif gender == "male":
            male +=1
    print(f"There are {female} females and {male} males")

def findById(id):
    for user in users:
        if user["id"]==id:
            print(user)

findById(2)

printHowMany()


printNames()