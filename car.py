class Car:
    __carPlate = ''

    def __init__(self, plate):
        self.__carPlate = plate

    def get_carPlate(self):
        return self.__carPlate

    def set_carPlate(self, plate):
        self.__carPlate = plate
