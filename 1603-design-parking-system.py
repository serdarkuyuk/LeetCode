#Naive solution
class ParkingSystem:

    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small


    def addCar(self, carType):
        if carType == 1:
            self.big -= 1
            return False if self.big < 0 else True
        elif carType == 2:
            self.medium -= 1
            return False if self.medium < 0 else True
        elif carType == 3:
            self.small -= 1
            return False if self.small < 0 else True

#Hashmap solution
class ParkingSystem:

    def __init__(self, big, medium, small):
        self.table = {1:big,
                    2:medium,
                    3:small}

    def addCar(self, carType):
        if self.table[carType] > 0:
            self.table[carType] -= 1
            return True
        return False

parkingSystem = ParkingSystem(1, 1, 0)


#for parkingSystem.addCar(1)
print(parkingSystem.addCar(1))
print(parkingSystem.addCar(2))
print(parkingSystem.addCar(3))
print(parkingSystem.addCar(1))
