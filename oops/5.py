# Encapsulation

class car:
    def __init__(self):
        self.__updatesoftware()

    def drive(self):
        print("driving")
        # self.__updatesoftware()

    def __updatesoftware(self):
        print("updating software")


blackcar = car()
blackcar.drive()
# blackcar.__updatesoftware()