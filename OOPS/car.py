class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self,value):
        self.__speed = value

    def get_speed(self):
        return self.__speed
        # print(speed)
        # print(color)
        # print('the __init__ is called')

ford = Car(200, 'red')
honda = Car(220, 'blue')
audi = Car(250, 'black')

# print(ford.speed)
# print(ford.color)

# ford.speed = 'jdskds'
ford.set_speed(300)

print(ford.get_speed())
# print(ford.color)

ford.set_speed(400)
print(ford.get_speed())

# audi1 = Car()

# ford.speed = 200
# honda.speed = 220
# audi.speed = 250

# ford.color = 'red'
# honda.color = 'blue'
# audi.color = 'black'



# print(ford.speed)
# print(ford.color)

# ford.speed = 300
# ford.color = 'white'

# print(ford.speed)
# print(ford.color)
