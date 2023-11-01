class CarParkingSystem:
    def __init__(self, total_spaces):
        self.total_spaces = total_spaces
        self.available_spaces = total_spaces

    def park_car(self):
        if self.available_spaces > 0:
            self.available_spaces -= 1
            return "Car parked successfully."
        else:
            return "Sorry, the car park is full."

    def free_up_space(self):
        if self.available_spaces < self.total_spaces:
            self.available_spaces += 1
            return "Space has been freed up successfully."
        else:
            return "No space to free up."

    def get_parking_availability(self):
        return f"Real-time parking availability: {self.available_spaces} out of {self.total_spaces} spaces available."

def main():
    parking_system = CarParkingSystem(total_spaces=100)

    print(parking_system.get_parking_availability())

    # Park cars
    print(parking_system.park_car())
    print(parking_system.get_parking_availability())

    # Free up spaces
    print(parking_system.free_up_space())
    print(parking_system.get_parking_availability())

if __name__ == "__main__":
    main()
