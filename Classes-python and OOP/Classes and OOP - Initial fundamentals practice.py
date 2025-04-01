#!/usr/bin/env python
# coding: utf-8

# 
# <div class="alert" style="background-color:#fff; color:white; padding:0px 10px; border-radius:5px;"><h1 style='margin:15px 15px; color:#008B8B; font-size:40px'> Classes and OOP </h1>
# </div>
# 
# 

# In[ ]:





# 
# - Class and Object creation
# - Instance variables and Methods, and Class level attributes
# - Model systems with class inheritance i.e., inherit From Other Classes
# - Parent Classes and Child Classes
# - Extend the functionality of Parent Classes using Child class
# - Object checking
# 
# 

# In[ ]:





# ## Create a Class with instance attributes: 

# In[2]:



## Create a Class with instance attributes: 
class Vehicle: 
    # Constructor:
    #-------------
    def __init__(self, max_speed, mileage):
        # body of the constructor:
        # Instance variable:
        self.max_speed = max_speed
        self.mileage = mileage
        
        

# Create object of the class: 
rav = Vehicle(160, 25)
print(rav.max_speed, rav.mileage)


# In[ ]:





# ## Create a Vehicle class without any variables and methods
# 

# In[3]:



## Create a Vehicle class without any variables and methods
class Vehicle:
    pass
  


# In[ ]:





# ## Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# 

# In[11]:



## Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
        
class Bus(Vehicle): 
    pass


        
# Object for testing: 
school_bus = Bus("school volvo", 180, 20)
print(school_bus.name, school_bus.max_speed, school_bus.mileage)
    


# In[ ]:





# ## Class Inheritance: 
# 

# In[29]:



## Class Inheritance: 
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
# 'Polymorphism' 
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    

class Bus(Vehicle): 
    # assign default value to capacity:
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
    

        
# Object for testing: 
school_bus = Bus("school volvo", 180, 20)
print(school_bus.seating_capacity())
    



# In[ ]:





# ## Define a property that must have the same value for every class instance (object) 
# 

# In[22]:



## Define a property that must have the same value for every class instance (object) 
# Define a class attribute "color” with a default value white. I.e., Every Vehicle should be white.


##** Variables created in .__init__() are called INSTANCE VARIABLEs. An instance variable’s value
    # is specific to a particular instance of the class
##**  CLASS VARIABLE is shared between all class instances. You can define a class attribute by
    # assigning a value to a variable name outside of .__init__()
    #  a variable that is declared inside of class, but outside of any instance method or __init__() method.
    
class Vehicle:
    
    #* Class attribute:
    color = "white"

    def __init__(self, name, max_speed, mileage):
        self.name = name 
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass




# Object for testing: 
School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, school_bus.name, school_bus.max_speed, school_bus.mileage)
car = Car("car lux", 120, 6)
print(car.color, car.name, car.max_speed, car.mileage)
    


# In[ ]:





# ## Class Inheritance
# 

# In[37]:



## Class Inheritance
# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any
    # vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% 
    # on full fare as a maintenance charge. So total fare for bus instance will become the final 
    # amount = total fare + 10% of the total fare.


class Vehicle: 
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
        
    def fare(self):
        return self.capacity * 100
    

class Bus(Vehicle):
    
    def fare(self):
        amount = super().fare()   # this gets you the return val from same name super fun? 
        return amount*1.1
    
    

    
# TEST
School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


# In[ ]:





# ## Check type of an object
# 

# In[42]:



## Check type of an object
# Write a program to determine which class a given Bus object belongs to.


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass




# TEST:
School_bus = Bus("School Volvo", 12, 50)
school_bus2 = Vehicle("genric", 20, 43)
print(type(School_bus), school_bus.name, school_bus.max_speed, school_bus.mileage)
print(type(School_bus2), school_bus2.name, school_bus2.mileage)


# In[ ]:





# ## Determine if School_bus is also an instance of the Vehicle class
# 

# In[49]:



## Determine if School_bus is also an instance of the Vehicle class


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass




#TEST: 
school_bus = Bus("School Volvo", 12, 50)

# Python's built-in isinstance() function:
#* isinstance(name, str) checks if name is an instance of a class str.
print(isinstance(school_bus, Bus))
print(isinstance(school_bus, Vehicle))


# In[ ]:





# In[56]:



# Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3
    # as arguments. Make sure to set these appropriately in the body of the __init__()method.

class Triangle:
    
    number_of_sides = 3 

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3    
    
    def check_angles(self): 
        if self.angle1+self.angle2+self.angle3 == 180:
            return True
        else:
            return False
        

        
# TEST: 
my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides, my_triangle.check_angles())


# In[ ]:





# In[57]:



# Define a class called Songs, it will show the lyrics of a song

class Songs:
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for item in self.lyrics:
            print(item)
    

    
# TEST:     
happy_bday = Songs(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])

print(happy_bday.sing_me_a_song())


# In[ ]:





# In[ ]:





# In[ ]:





# In[61]:



# Define a class called Lunch.Its __init__() method should have two arguments
# if "menu 1" print "Your choice:", menu, "Price 12.00", if "menu 2" print "Your choice:", menu, "Price 13.40", else print "Error in menu".
class Lunch:
    
    def __init__(self, menu):
        self.menu = menu
    
    def menu_price(self):
        if self.menu == "menu 1":
            print("Your choice:", self.menu, "Price 12.00")
        elif self.menu == "menu 2":
            print("Your choice:", self.menu, "Price 13.40")
        else:
            print("Error in menu")
            

# TEST: 
Paul = Lunch("menu 1") 
print(Paul.menu_price())
            
        


# In[ ]:





# In[2]:



# Object Oriented:
#-------------------


class Student(object):
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    def setGrade(self, course, grade):
        self.grades[course] = grade

    def getGrade(self, course):
        return self.grades[course]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)

# Define some students
john = Student("John", 12, "male", 6, {"math":3.3})
jane = Student("Jane", 12, "female", 6, {"math":3.5})

# Now we can get to the grades easily
print(john.getGPA())
print(jane.getGPA())







# Standard Dict:
#-----------------


def calculateGPA(gradeDict):
    return sum(gradeDict.values())/len(gradeDict)

students = {}
# We can set the keys to variables so we might minimize typos
name, age, gender, level, grades = "name", "age", "gender", "level", "grades"
john, jane = "john", "jane"
math = "math"
students[john] = {}
students[john][age] = 12
students[john][gender] = "male"
students[john][level] = 6
students[john][grades] = {math:3.3}

students[jane] = {}
students[jane][age] = 12
students[jane][gender] = "female"
students[jane][level] = 6
students[jane][grades] = {math:3.5}

# At this point, we need to remember who the students are and where the grades are stored. Not a huge deal, but avoided by OOP.
print(calculateGPA(students[john][grades]))
print(calculateGPA(students[jane][grades]))




## REF: https://stackoverflow.com/questions/33072570/when-should-i-be-using-classes-in-python  




# In[ ]:





# In[ ]:





# In[5]:



## Constructors:
class Student:

    # constructor
    # initialize instance variable
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('All variables initialized')

    # instance Method
    def show(self):
        print('Hello, my name is', self.name)


# create object using constructor
s1 = Student('Emma')
s1.show()


# In[ ]:





# In[3]:


## Static Methods: 

class Employee(object):

    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        for task in requirement:
            print('Completed', task)

emp = Employee('Kelly', 12000, 'ABC Project')
emp.work()



# In[ ]:





# In[7]:



##  Polymorphism: 
# Polymorphism with Inheritance

class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


        
# inherit from vehicle class
#---------------------------
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')




# Car Object
car = Car('Car x1', 'Red', 20000)
car.show()
# calls methods from Car class
car.max_speed()
car.change_gear()

# Vehicle Object
vehicle = Vehicle('Truck x1', 'white', 75000)
vehicle.show()
# calls method from a Vehicle class
vehicle.max_speed()
vehicle.change_gear()




# In[8]:



## Polymorphism: Overrride Built-in Functions - "len()"

class Shopping:
    def __init__(self, basket, buyer):
        self.basket = list(basket)
        self.buyer = buyer

    def __len__(self):
        print('Redefine length')
        count = len(self.basket)
        # count total items in a different way
        # pair of shoes and shir+pant
        return count * 2

shopping = Shopping(['Shoes', 'dress'], 'Jessa')
print(len(shopping))


# In[10]:



# Polymorphism In Class methods

class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("Max speed 350")

class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("Max speed is 240")

ferrari = Ferrari()
bmw = BMW()

# iterate objects of same type
for car in (ferrari, bmw):
    # call methods without checking class of object
    car.fuel_type()
    car.max_speed()
    

##** They have the same instance method names fuel_type() and max_speed(). However, we have not
    # linked both the classes nor have we used inheritance.
    


# In[11]:



# Polymorphism with Function and Objects

class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("Max speed 350")

class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("Max speed is 240")

# normal function
def car_details(obj):
    obj.fuel_type()
    obj.max_speed()

ferrari = Ferrari()
bmw = BMW()

car_details(ferrari)
car_details(bmw)




# In[12]:



# pyhton way of method Overloading  (standard overloading not suported in python) 
# User-defined polymorphic method

class Shape:
    # function with two default parameters
    def area(self, a, b=0):
        if b > 0:
            print('Area of Rectangle is:', a * b)
        else:
            print('Area of Square is:', a ** 2)

square = Shape()
square.area(5)

rectangle = Shape()
rectangle.area(5, 3)


# In[15]:



# Operator Overloading in Python

# add 2 numbers
print(100 + 200)

# concatenate two strings
print('Jess' + 'Roy')

# merger two list
print([10, 20, 30] + ['jessa', 'emma', 'kelly'])



## Overloading + operator for custom objects
#---------------------------------------------

class Book:
    def __init__(self, pages):
        self.pages = pages

    # Overloading + operator with magic method
    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(400)
b2 = Book(300)
print("Total number of pages: ", b1 + b2)




##* Overloading the * Operator
#---------------------------------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, timesheet):
        print('Worked for', timesheet.days, 'days')
        # calculate salary
        return self.salary * timesheet.days


class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days


emp = Employee("Jessa", 800)
timesheet = TimeSheet("Jessa", 50)
print("salary is: ", emp * timesheet)




# In[ ]:





# # Python Class Exercises
# 

# In[25]:



class Nobel():
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner
    

    

#* __str__ function can be used to return a string representation for the class when needed.

class Nobel():
    
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner
        
    def __str__(self):
        return "{} was the winner of nobel {} prize in year {}".format(self.winner, self.category, self.year)
        

        
#------------------------
        
class Myfunc():
    
    def fifth(num):
        return "the 5th power of {} is {}.".format(num, num**5)
    

ans = Myfunc.fifth(5)
print(ans)

#----------------------------



        
class Myfunc():
    
    def power(n1, n2):
        return "the {} power of {} is {}.".format(n2, n1, n1**n2)
    
    def __str__(self):
        return "mMyfunc is a class which is capable of mathematical operations like raising a number to a power with power function."

    

ans1 = Myfunc.power(5, 6)
ans2 = Myfunc.power(2, 8)

print(ans1)
print(ans2)




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 
# <div class="notebook-title" style="background-color:#008B8B; color:white; padding:5px 5px; border-radius:5px;"><h2 style='margin:7px 5px; font-size:22px'> Indexing Calls Workflow Fun   </h2>
# </div>
# 
# 

# 
# 
# <div style="border-color: #008B8B; border-style:solid; background-color:#D3D3D3"><h2 style='margin:10px 5px; font-size:35px, color:#008B8B'>MAIN()  CALL: </h2></div>
# 
# 

# In[ ]:





# In[ ]:





# In[23]:


## REF: 

# https://pynative.com/python-object-oriented-programming-oop-exercise/
# 


# In[ ]:





# In[ ]:




