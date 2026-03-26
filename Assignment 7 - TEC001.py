#Task 1
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

new_car = Car("ABC-123", 142)

print(f"Registration Number: {new_car.registration_number}")
print(f"Maximum Speed: {new_car.max_speed} km/h")
print(f"Current Speed: {new_car.current_speed} km/h")
print(f"Travelled Distance: {new_car.travelled_distance} km")

#Task 2
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change_of_speed):
        new_speed = self.current_speed + change_of_speed

        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

new_car = Car("ABC-123", 142)
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

print(f"Current speed after acceleration: {new_car.current_speed} km/h")

new_car.accelerate(-200)

print(f"Final speed after emergency brake: {new_car.current_speed} km/h")

#Task 3
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change_of_speed):
        new_speed = self.current_speed + change_of_speed
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed
    def drive(self, hours):
        distance_covered = self.current_speed * hours
        self.travelled_distance += distance_covered

new_car = Car("ABC-123", 142)
new_car.accelerate(60)
new_car.drive(1.5)

print(f"Current Speed: {new_car.current_speed} km/h")
print(f"Travelled Distance: {new_car.travelled_distance} km")

#Task 4
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change_of_speed):
        self.current_speed = max(0, min(self.max_speed, self.current_speed + change_of_speed))
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

cars = []
for i in range(1, 11):
    random_max_speed = random.randint(150, 200)
    cars.append(Car(f"ABC-{i}", random_max_speed))

race_finished = False
while not race_finished:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True

print(f"{'Reg. Number':<12} | {'Max Speed':<10} | {'Current Speed':<15} | {'Distance':<10}")
print("-" * 55)
for car in cars:
    print(
        f"{car.registration_number:<12} | {car.max_speed:<6} km/h | {car.current_speed:<9} km/h | {car.travelled_distance:<10.1f} km")