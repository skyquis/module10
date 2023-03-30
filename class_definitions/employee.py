#Importing date time as it is needed
import datetime

"""
Encapsulation Assignment
Write your first class! Look at the Employee class above, copy and paste to employee.py in your IDE after you create your Module10 project, class_definitions package and test package.
In designing code, we often use UML diagrams, below is the UML diagram for Employee class. In Python, it is less obvious the type of data members. The - minus sign means private and the + plus sign means public. Use the convention to consider private in naming your class variables in your constructor, do not use name mangling. Note the examples above did not consider class data members private!
UML of Employee Class
The class attributes are the following:
last_name: string
first_name: string
address: string
phone_number: string
salaried: boolean
start_date: datetime
salary: float (sorry, had listed double as the type before, that is in C or Java; or Jython/CPython).

Methods:
display() returns a string that when printed will follow the below format:
Sasha Patel
123 Main Street
Urban, Iowa
Salaried employee: $40,000/year       # OR Hourly employee: $7.25/hour
Start date: 6-28-2019
Note this will have some logic statements to check for salaried or hourly to construct the return string.
"""

class Employee:
    '''Employee Class '''
    # Constructor
    def __init__(self, lname, fname, addy, phone_num, salary, st_date, sal_amount=40000):
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = phone_num
        self.salaried = salary
        self.start_date = st_date
        self.salary = sal_amount

    # Defining how string of object appears
    def __str__(self):
         return str(self.first_name)+" " + str(self.last_name)

    # Defining representation of object
    def __repr__(self):
         return "Employee(\""+self.last_name+"\",\""+self.first_name+"\",\""+self.address+"\",\""+self.salaried+"\")"

    def display(self):
         if self.salaried==False:
             self.salary=7.25
             return str(self.last_name) + ", " + str(self.first_name) +"\n"+str(self.address)+"\nHourly employee: $"+str(self.salary)+"/hour\nStart date: "+str(self.start_date)
         else:
             return str(self.last_name) + ", " + str(self.first_name) + "\n" + str(self.address) + "\nHourly employee: $" + str(self.salary) + "/year\nStart date: " + str(self.start_date)

# Driver
emp = Employee('Marquis', 'Skyler','506 Maxwelton Drive\nDes Moines, Iowa','515-441-6249','False',datetime.date(2022,5,9)) # call the construtor, needs to have a first and last name in parameter
print(emp.display())                # display returns a str, so print the information
print(str(emp))                     # str displays the defined string of object
print(repr(emp))                    # repr displays representation of object
del emp                             #clean up step