# Author: Brian Matthew Alltop
# StudentID: 000820333
# WGU C950 - Data Structures & Algorithms 2

from enum import Enum


class DeliveryStatus(str, Enum):
    AtHub = 'At Hub',
    EnRoute = 'En Route',
    Delivered = 'Delivered'


class Delivery:
    def __init__(self, delivery_id: int, address: str, city: str, state: str, zip: int, deadline: str, kilos: int,
                 notes: str):
        self.id = delivery_id
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = zip
        self.deadline = deadline
        self.kilos = kilos
        self.notes = notes
        self.delivery_time = ''
        self.current_location = DeliveryStatus.AtHub
        self.status = DeliveryStatus.AtHub

    def set_delivery_time(self, delivery_time: str) -> None:
        self.delivery_time = delivery_time

    def set_current_location(self, current_location: str) -> None:
        self.current_location = current_location

    def get_delivery_time(self) -> str:
        return self.delivery_time

    def get_address(self) -> str:
        return self.address

    def get_city(self) -> str:
        return self.city

    def get_state(self) -> str:
        return self.state

    def get_postal_code(self) -> int:
        return self.postal_code

    def get_deadline(self) -> str:
        return self.deadline

    def get_kilos(self) -> int:
        return self.kilos

    def get_notes(self) -> str:
        return self.notes

    def get_status(self) -> str:
        return self.status

    def get_current_location(self) -> str:
        return self.current_location
    
    def print(self):
        print(f'Package ID: {self.id}')
        print(f'Address: {self.address}')
        print(f'City: {self.city}')
        print(f'State: {self.state}')
        print(f'Postal Code: {self.postal_code}')
        print(f'Deadline: {self.deadline}')
        print(f'Kilos: {self.kilos}')
        print(f'Notes: {self.notes}')
        print(f'Delivery Time: {self.delivery_time}')
        print(f'Current Location: {self.current_location}')
        print(f'Status: {self.status}')
        print('\n')
