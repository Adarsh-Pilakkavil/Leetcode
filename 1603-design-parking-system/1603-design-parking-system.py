class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.avail=[big,medium,small]
    def addCar(self, carType: int) -> bool:
        i=carType-1
        if self.avail[i]>0:
            self.avail[i]-=1
            return True
        return False
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)