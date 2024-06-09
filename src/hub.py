# Author: Brian Matthew Alltop
# StudentID: 000820333
# WGU C950 - Data Structures & Algorithms 2

import csv
from datetime import datetime

from hash_table import HashTable
from package import Package
from truck import Truck


class Hub:

    def __init__(self):
        self._trucks = []

        self._shipments = HashTable()
        self.__load_shipments()

    @property
    def trucks(self) -> list:
        return self._trucks

    @property
    def shipments(self) -> HashTable:
        return self._shipments

    def deliver_packages(self):
        truck_one: Truck = Truck(1)
        truck_two: Truck = Truck(2)
        truck_three: Truck = Truck(3)

        self._trucks.append(truck_one)
        self._trucks.append(truck_two)
        self._trucks.append(truck_three)

        # Truck one leaves at 8:00am
        truck_one.departure_time = datetime.strptime('08:00:00', '%H:%M:%S')

        # Truck two will leave at 9:05am
        truck_two.departure_time = datetime.strptime('09:05:00', '%H:%M:%S')

        # Pre-sorted package IDs for each truck
        # I organized these in Excel to make it easier to sort by zip code and create groupings.
        truck_one_packages = [1, 13, 14, 15, 16, 19, 20, 21, 26, 27, 29, 34, 35, 39, 40]
        truck_two_packages = [3, 6, 8, 12, 17, 18, 30, 31, 36, 37, 38]
        truck_three_packages = [2, 4, 5, 7, 9, 10, 11, 22, 23, 24, 25, 28, 32, 33]

        # Sort the packages into the trucks
        # Runs at O(n) time complexity, O(n) space complexity
        for kvp in self.shipments:
            package: Package = kvp[1]
            if package.id in truck_one_packages:
                truck_one.load_package(package)
            elif package.id in truck_two_packages:
                truck_two.load_package(package)
            elif package.id in truck_three_packages:
                truck_three.load_package(package)

        # Deliver the packages
        # Truck one and two must deliver their packages before truck three
        truck_one.deliver_packages()
        truck_two.deliver_packages()

        # Whenever truck one or two returns, truck three can depart.
        truck_three_can_depart = datetime.strptime('10:20:00', '%H:%M:%S')

        # Truck three cannot depart until 10:20 when package #9's address is corrected.
        # If one of the trucks returns before 10:20, this ensures truck three can leave as soon as possible.
        if min(truck_one.current_time, truck_two.current_time) < truck_three_can_depart:
            truck_three.departure_time = truck_three_can_depart
        else:
            truck_three.departure_time = min(truck_one.current_time, truck_two.current_time)

        truck_three.deliver_packages()

        # Update package statuses at the Hub.
        for p in truck_one.delivered_packages:
            self.__update_package_status(p)

        for p in truck_two.delivered_packages:
            self.__update_package_status(p)

        for p in truck_three.delivered_packages:
            self.__update_package_status(p)

    def get_truck_total_mileage(self):
        """Returns the total mileage for all trucks
            Runs at O(n) time complexity, O(1) space complexity"""
        total_mileage = 0
        for truck in self._trucks:
            total_mileage += truck.get_total_mileage()
        return total_mileage

    def get_package_by_id(self, package_id: int) -> Package:
        """Returns a package by ID
            Runs at O(1) time complexity, O(1) space complexity"""
        package = self.shipments[package_id]
        return package

    def print_shipments(self):
        """Prints all shipments
            Runs at O(n) time complexity, O(1) space complexity"""
        for kvp in self.shipments:
            print(kvp[1])

    def __load_shipments(self):
        with open('../data/shipments.csv') as csvfile:
            shipment_data = csv.reader(csvfile)
            for row in shipment_data:
                id = int(row[0])
                address = row[1]
                city = row[2]
                state = row[3]
                postal_code = row[4]
                deadline = row[5]
                kilos = row[6]
                notes = row[7]

                package = Package(id, address, city, state, postal_code, deadline, kilos, notes)
                self._shipments[id] = package

    def __update_package_status(self, updated_package: Package):
        package = self.shipments[updated_package.id]
        package.departure_time = updated_package.departure_time
        package.delivery_time = updated_package.delivery_time
