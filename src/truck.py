import datetime
from sys import float_info
from typing import List

from distancelookup import DistanceLookup
from package import Package, PackageStatus


class Truck:

    def __init__(self, id: int):
        self._id = id
        self._average_speed = 18.0
        self._max_packages = 16
        self._departure_time = None
        self._current_time = self._departure_time
        self._current_location = '4001 South 700 East'
        self._mileage = 0.0
        self._packages = []
        self._delivered_packages = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def departure_time(self) -> datetime:
        return self._departure_time

    @departure_time.setter
    def departure_time(self, value: datetime):
        self._departure_time = value

    @property
    def current_time(self) -> datetime:
        return self._current_time

    @current_time.setter
    def current_time(self, value: datetime):
        self._current_time = value

    @property
    def mileage(self) -> int:
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        self._mileage = value

    @property
    def packages(self) -> list[Package]:
        return self._packages

    @property
    def delivered_packages(self) -> List[Package]:
        return self._delivered_packages

    def load_package(self, package) -> None:
        self._packages.append(package)

    def deliver_packages(self) -> None:
        """
        Deliver the packages on the truck's route.
        Nearest neighbor implementation to determine the truck's route.
        Runs at O(n^2) time complexity, O(1) space complexity
        """
        # Iterate over the packages and calculate their delivery time.
        # The truck will deliver the packages according to the optimal route.
        distance_lookup = DistanceLookup()
        self._current_time = self._departure_time
        while len(self._packages) > 0:
            # Initialize a max float to store the initial distance
            distance = float(float_info.max)
            # Set the current package to None
            current_package = None
            for package in self._packages:
                # Calculate the distance from the current location to the package's address
                calculated_distance = distance_lookup.get_distance_between_addresses(self._current_location,
                                                                                           package.address)
                # If the calculated distance is less than or equal to the current distance, update the distance and 
                # current package.
                if calculated_distance <= distance:
                    distance = calculated_distance
                    current_package = package

            # Calculate the time to deliver the package based on the truck's average speed
            time_to_deliver = self.calculate_time_to_deliver(distance)

            # The delivery time will be the next departure time plus the time to deliver the package
            delivery_time = self._current_time + datetime.timedelta(hours=time_to_deliver)

            # Update the package's delivery time and status
            current_package.departure_time = self._departure_time
            current_package.delivery_time = delivery_time

            # Remove the package from the packages list and add it to the delivered packages list
            self._delivered_packages.append(current_package)
            self._packages.remove(current_package)

            # Update the truck's current mileage based on the distance traveled.
            self._mileage += distance

            # Update the truck's current time to the last delivery time
            self._current_time = delivery_time

            # Update the current location to the package's address
            self._current_location = current_package.address

    def calculate_time_to_deliver(self, distance: float) -> float:
        """
        Calculate the time to deliver a package based on the truck's average speed.
        :param distance: The distance, in miles.
        :return: The time to deliver the package, in hours.
        Runs at O(1)
        """
        return distance / self._average_speed
