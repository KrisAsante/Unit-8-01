# Created by: Chris Asante
# Created on: 3-April-2019
# Created for: ICS3U
# Unit 8-01
# This main program will create a car object

from car import *

#create a vehicle
car1 = Car()
car2 = Car()

print(car1.current_state())
car1.accelerate(100)
print(car1.current_state())
car1.brake(50)
print(car1.current_state())

print(car2.current_state())
car2.accelerate(50)
print(car2.current_state())
car2.accelerate(160)
print(car2.current_state())