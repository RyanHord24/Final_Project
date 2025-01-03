class CarManager:
    all_cars = []
    total_cars = 0
    id_counter = 1

    def __init__(self, make, model, year, mileage, services,):
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services
        self._id = CarManager.id_counter

        print(f'New car included. It is a {self._year} {self._make} {self._model}')

        CarManager.all_cars.append(self)
        CarManager.total_cars += 1
        CarManager.id_counter += 1

    def __str__(self):
        return(f'This is a {self._year} {self._make} {self._model}')


car_1 = CarManager('Jeep', 'Compass', '2020', '50000', 'CarPlay')

car_2 = CarManager('Toyota', 'Prius', '2015', '75000', 'Good Mileage')

print(car_1._id)

print(car_2._id)

print(CarManager.total_cars)

print(car_1)
