Programming Lang - Procedural Programming, Object-Oreiented Programming

ex: C, Pascal

unit - functions

concentrates on creating functions
data and operations on the data are separated.
methodology requires sending data to procedure/functions.

#travel
Global Data
travel{
    openApp()
    bookCab()
    waitForTheCab()
    sitInCab()
    reachDestination()
    PayCabFare()
}

Object-Oriented Programming
ex: C++, Java, Python
unit - class
centered on creating objects
Objects: A single software unit that combines data and methods
Data in an object are known as attributes.
Procedure/functions in an object are known as methods.


class Cab{
    cabService, make.location, numberPlate;   #data
    book(), arrival(), start(); #methods
}

class CabDriver{
    name, employeeID  #data
    openDoor(), drive()   #methods
}

class passenger{
    name, address  #data
    openApp(), bookCab(), walk()    #methods
}
