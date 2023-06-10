QUESTION:-1. What is Abstraction in oops? Explain with an example.
Abstraction is the process of hiding the internal details of an application from the outer world.
import abc
class pwskills: 

    @abc.abstractmethod
    def students_detials(self): 
        pass

    @abc.abstractmethod
    def student_asssignment(self): 
        pass

    @abc.abstractmethod
    def students_marks(self): 
        pass

class student_detils(pwskills): 
    def students_detials(self): 
        return "This is a method for takimg students details"

    def student_assignment(self): 
        return "This is a method for assing details for a perticular student"

class data_science_maters(pwskills): 
    def students_detials(self): 
        return "This will return a student details for data science masters"

    def student_assignment(self): 
        return "This will give you a student assignment detailed for data science masters"

dsm = data_science_maters()
print(dsm.students_detials())

sd = student_detils()
print(sd.students_detials())       



QUESTION:-2. Differentiate between Abstraction and Encapsulation. Explain with an example.
Abstraction is a design level process and it is used to reduce the complexity at the designing stage of a project.
import abc
class pwskills: 

    @abc.abstractmethod
    def students_detials(self): 
        pass

    @abc.abstractmethod
    def student_asssignment(self): 
        pass

    @abc.abstractmethod
    def students_marks(self): 
        pass

class student_detils(pwskills): 
    def students_detials(self): 
        return "this is a meth for takimg students details"

    def student_assignment(self): 
        return "this is a meth for assing details for a perticualt student"

class data_science_maters(pwskills): 
    def students_detials(self): 
        return "this will return a student details for data science masters"

    def student_assignment(self): 
        return "this will give you a student assignment detaild for data science masters"

dsm = data_science_maters()
print(dsm.students_detials())

sd = student_detils()
print(sd.students_detials())       

Encapsulation is an implementation level process, and it is used to provide privacy and maintain control over the transparency of data at the implementation stage of a project.
class car : 
    def __init__(self , year , make , model, speed): 
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = 0

    def set_speed(self,speed) : 
        self.__speed = 0 if speed < 0 else speed

    def get_speed(self) : 
        return self.__speed        
c = car(2021 , "toyata" , "innova" , 12)
print(c._car__year)
c.set_speed(100)
print(c.get_speed()) 
print(c._car__model)
print(c._car__make) 



QUESTION:-3. What is abc module in python? Why is it used?
This module provides the infrastructure for defining abstract base classes (ABCs) in python, as outlined in PEP 3119; see the PEP for why this was added to python.



QUESTION:-4. How can we achieve data abstraction?
Data Abstraction in python can be achieved through creating abstract classes and inheriting them later.



QUESTION:-5. Can We create an instance of an abstract class? Explain your answer.
Abstract classes cannot be instantiated, but they can be subclassed. When an abstract class is subclassed, the subclass usually provides implementations for all of the abstract methods in its parent class.
