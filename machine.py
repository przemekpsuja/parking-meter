import datetime
import sys

from car import Car
from ticket import Ticket


class Machine:
    tempPlate = ''
    logout = False
    prices = {
        '1': '0,10$',
        '2': '0,20$',
        '3': '0,50$',
        '4': '1,00$',
        '5': '2,00$',
        '6': '5,00$',
    }

    def __init__(self):
        self.tickets = {}

    def choose_option(self):
        while True:
            print('1. Print free 2h ticket')
            print('2. Buy long term ticket')
            print('3. Log in as controller')
            print('4. Exit')
            x = int(input('Your choice is: '))
            if x == 1:
                self.tempPlate = input('Please type your car\'s plate: ').upper()
                self.print_free_ticket(self.tempPlate)
            elif x == 2:
                self.tempPlate = input('Please type your car\'s plate: ').upper()
                self.buy_ticket(self.tempPlate)
            elif x == 3:
                self.logout = False
                pin = int(input('Type your pin (TIP: it\'s = 1234): '))
                while not self.logout:
                    self.login(pin)
            else:
                sys.exit()

#This function couting how many coins does we put into park-machine and return how long car can parking
    def how_long(self):
        time = 0
        stop = False

        while not stop:
            print('Insert coin: \n')
            for k, v in self.prices.items():
                print(f'{k}. {v}')
            x = input('Choose coin: \n')
            print(x)
            if int(x) <= len(self.prices):
                if self.prices[x] == '0,10$':
                    time += 1
                elif self.prices[x] == '0,20$':
                    time += 2
                elif self.prices[x] == '0,50$':
                    time += 5
                elif self.prices[x] == '1,00$':
                    time += 10
                elif self.prices[x] == '2,00$':
                    time += 20
                elif self.prices[x] == '5,00$':
                    time += 50
            else:
                print('Incorect value. Please type coin value by keys 1-6')
            print(f'\nYou can park by {time} minutes.\n')
            print('1. Insert next coin')
            print('2. Confirm time')
            y = int(input('What do you want to do next: \n'))
            if y == 2:
                stop = True
        return time

# Function creating free 2 hours ticket for a specific car
    def print_free_ticket(self, plate):
        car = Car(plate)
        ticket = Ticket(car.get_carPlate(), 120)
        ticket.set_datetime(2)
        self.tickets[car.get_carPlate()] = ticket.get_expirydatetime()
        print(f'Take your free ticket! It expire: {ticket.get_expirydatetime().strftime("%x %X")}\n')

# Function creating new ticket on specified parking time
    def buy_ticket(self, plate):
        car = Car(plate)
        time = self.how_long()
        ticket = Ticket(car.get_carPlate(), time)
        self.tickets[car.get_carPlate()] = ticket.get_expirydatetime()
        print(f'Your ticket expire in: {ticket.get_expirydatetime().strftime("%x %X")}\n')

# Function which removing from dictionary expired tickets durig every loggin
    def remove_expire_ticets(self):
        for k in list(self.tickets.keys()):
            if self.tickets[k] < datetime.datetime.now():
                del self.tickets[k]

# Simple logging function which checking PIN number correctness and servicing logged user
    def login(self, pin):
        if pin == 1234:
            self.remove_expire_ticets()
            self.check_plate()
            x = input('Logout? y - yes, n - no \n')
            if x == 'y':
                self.logout = True
            else:
                pass
        else:
            print('PIN number is incorrect!\n')

# This one searching thru the ticket dict for specified plate
    def check_plate(self):
        x = input('What plate would you check? \n').upper()
        if x in self.tickets:
            if self.tickets[x] >= datetime.datetime.now():
                print('Everythink is OK!\n')
            else:
                print('His time has gone!\n')
        else:
            print('This car not exist!\n')
