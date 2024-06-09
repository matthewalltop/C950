# Author: Brian Matthew Alltop
# StudentID: 000820333
# WGU C950 - Data Structures & Algorithms 2
from datetime import datetime, time
from enum import Enum


class PackageStatus(str, Enum):
    AtHub = 'At Hub',
    EnRoute = 'En Route',
    Delivered = 'Delivered'


class Package:
    def __init__(self, id: int, address: str, city: str, state: str,
                 postal_code: int, deadline: str, kilos: float, notes: str):
        self._id = id
        self._address = address
        self._city = city
        self._state = state
        self._postal_code = postal_code
        self._deadline = deadline
        self._kilos = kilos
        self._notes = notes
        self._departure_time = ''
        self._delivery_time = ''

    def __str__(self):
        return (f'Package ID: {self.id}\n'
                f'Address: {self.address}\n'
                f'City: {self.city}\n'
                f'State: {self.state}\n'
                f'Postal Code: {self.postal_code}\n'
                f'Deadline: {self.deadline}\n'
                f'Kilos: {self.kilos}\n'
                f'Notes: {self.notes}\n'
                f'Departure Time: {self.departure_time.strftime("%H:%M:%S")}\n'
                f'Delivery Time: {self.delivery_time.strftime("%H:%M:%S")}\n')

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        self._address = value

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, value: str) -> None:
        self._city = value

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, value: str) -> None:
        self._state = value

    @property
    def postal_code(self) -> int:
        return self._postal_code

    @postal_code.setter
    def postal_code(self, value: int) -> None:
        self._postal_code = value

    @property
    def deadline(self) -> str:
        return self._deadline

    @deadline.setter
    def deadline(self, value: str) -> None:
        self._deadline = value

    @property
    def kilos(self) -> int:
        return self._kilos

    @kilos.setter
    def kilos(self, value: int) -> None:
        self._kilos = value

    @property
    def notes(self) -> str:
        return self._notes

    @notes.setter
    def notes(self, value: str) -> None:
        self._notes = value

    @property
    def departure_time(self) -> str:
        return self._departure_time

    @departure_time.setter
    def departure_time(self, value: str) -> None:
        self._departure_time = value

    @property
    def delivery_time(self) -> time:
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, value: str) -> None:
        self._delivery_time = value

    def get_package_status_at_time(self, time_diff: datetime) -> str:
        current_location = self.get_current_location(time_diff)
        return str(self) + f'Current Location: {current_location}\n'

    def get_current_location(self, time_diff: datetime) -> str:
        match time_diff:
            case time_diff if self.delivery_time <= time_diff:
                return "Delivered"
            case time_diff if self.departure_time < time_diff:
                return "En Route"
            case _:
                return "At Hub"
