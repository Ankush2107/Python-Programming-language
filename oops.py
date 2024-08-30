class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def get_number_of_wheels(self):
        return self.number_of_wheels
    
    def set_number_of_wheels(self, number):
        self.number_of_wheels = number
        
    def make_noise(self):
        print('VRUUUUUUUUU')
        
        
mercedes = Vehicle(4, 'electric', 4, 350)
print(mercedes.get_number_of_wheels())

mercedes.set_number_of_wheels(8)
print(mercedes.get_number_of_wheels())

mercedes.make_noise()