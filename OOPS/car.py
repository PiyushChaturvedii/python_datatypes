class Car:
    pass

ford = Car()
honda = Car()
audi = Car()

ford.speed = 200
honda.speed = 220
audi.speed = 250

ford.color = 'red'
honda.color = 'blue'
audi.color = 'black'



print(ford.speed)
print(ford.color)

ford.speed = 300
ford.color = 'white'

print(ford.speed)
print(ford.color)
