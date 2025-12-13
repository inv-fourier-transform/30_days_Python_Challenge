class Car:
    def __init__(self, make:str, fuel_type:str, seating_capacity:int) -> None:
        self.make = make
        self.fuel_type = fuel_type
        self.seating_capacity = seating_capacity
        self.engine_state: bool = False

    def __str__(self) -> str:
        return f"Car is {self.make} with fuel type {self.fuel_type} having seating capacity of {self.seating_capacity}"

    def __repr__(self) -> str:
        return f"Car(make={self.make},fuel_type={self.fuel_type},seating_capacity={self.seating_capacity})"

    def car_moves(self):
        if not self.engine_state:
            self.engine_state = True
            return f"Car {self.make} is made to start"
        else:
            return f"Car {self.make} is already running"


if __name__ == "__main__":
    car = Car("Toyota Wellfire", "Petrol", 8)
    print(car)
    print(car.car_moves())
    print(car.car_moves())

    car = Car(make="Kia Carnival",fuel_type="Diesel", seating_capacity=8)
    print(car)
    car.engine_state = True
    print(car.car_moves())

