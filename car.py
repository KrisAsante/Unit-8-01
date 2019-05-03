# Created by: Chris Asante
# Created on: 3-April-2019
# Created for: ICS3U
# Unit 8-01
# This is a class that defines a car

class Car:
    #Class that creates the car
    
    def __init__(self):
        #private fields
        
        self.__license_plate_number = "ABCD1234"
        self.__colour = "black"
        self.__number_of_doors = 4
        self.__speed = 0
        self.__maximum_speed = 200
        self.__minimum_speed = -30
        self.__number_of_wheels = 4
        self.__number_of_tires = 4
    
    #public methods
    def accelerate(self, speed_increase):
        #increases the speed
        
        if self.__speed < self.__maximum_speed:
            self.__speed = self.__speed + speed_increase
            if self.__speed > self.__maximum_speed:
                self.__speed = self.__maximum_speed
        else:
            print('You cannot increase speed past maximum speed.')
    
    def brake(self, speed_decrease):
        #decreases the speed
        
        if self.__speed > self.__minimum_speed:
            self.__speed = self.__speed - speed_decrease
            if self.__speed < self.__minimum_speed:
                self.__speed = self.__minimum_speed
        else:
            print('You cannot decrease speed below maximum reverse speed.')
    
    def current_state(self):
        #returns the current state of the car as a string
        
        return_string = "License plate number = " + str(self.__license_plate_number) + "\nColour = " + str(self.__colour) + "\nNumber of doors = " + str(self.__number_of_doors) + "\nSpeed = " + str(self.__speed) + "\nMaximum speed = " + str(self.__maximum_speed) + "\nMaximum speed in reverse = " + str(self.__minimum_speed) + "\nNumber of wheels = " + str(self.__number_of_wheels) + "\nNumber of tires = " + str(self.__number_of_tires) + "\n"
        
        return return_string