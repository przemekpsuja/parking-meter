import datetime

import car


class Ticket:
    min = 0

    def __init__(self, plate, minute):
        self.__datetime = datetime.datetime.now()
        self.__car = car.Car(plate)
        self.__expirydatetime = self.__datetime + datetime.timedelta(minutes=minute)

    def get_datetime(self):
        return self.__datetime

    def set_datetime(self, min):
        temp = datetime.timedelta(minutes=min)
        self.__datetime = self.__datetime + temp

    def get_expirydatetime(self):
        return self.__expirydatetime
