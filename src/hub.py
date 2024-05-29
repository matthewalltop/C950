# Author: Brian Matthew Alltop
# StudentID: 000820333
# WGU C950 - Data Structures & Algorithms 2

import csv
from hash_table import HashTable
from delivery import Delivery
from distances import Distances
from truck import Truck


class Hub:
    def __init__(self):
        self.__trucks = []
        self.__shipments = HashTable()
        self.__load_trucks()
        self.__load_packages()

    def __load_trucks(self) -> None:
        """Loads trucks with packages"""
        truck_one = Truck('8:00')
        truck_two = Truck('9:00')
        truck_three = Truck('10:00')

        self.__trucks.append(truck_one)
        self.__trucks.append(truck_two)
        self.__trucks.append(truck_three)

    def __load_packages(self) -> None:
        """Reads shipment data into hash table
            Runs at O(n)"""
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

                package = Delivery(id, address, city, state, postal_code, deadline, kilos, notes)

                self.__shipments[id] = package

    # def __sort_packages(self) -> None:
    #     # Load anything
    #     if postal_code == '84014' and deadline != '10:30':
    #         self.__shipment_three.append(delivery)
    # 
    #     # Package Number #9 needs address corrected at 10:20am
    #     if 'Wrong address listed' in notes:
    #         delivery[1] = '410 S State St'
    #         delivery[3] = '84111'
    #         self.__shipment_three.append(delivery)
    # 
    #     # Load anything on the first truck that has to be delivered together
    #     # or that has no special constraints; This will be the first truck
    #     # to leave so we can wait for EOD packages
    #     if deadline != 'EOD':
    #         if 'Must' in notes or notes == '':
    #             self.__shipment_one.append(delivery)
    # 
    #     # Add the second truck specific values to the second truck
    #     if 'Can only be' in notes or 'Delayed' in notes:
    #         self.__shipment_two.append(delivery)
    # 
    #     # If not in any other deliveries add here.
    #     if delivery not in self.__shipment_one and \
    #             delivery not in self.__shipment_two and \
    #             delivery not in self.__shipment_three:
    #         if len(self.__shipment_two) > len(self.__shipment_three):  # Add to shipment three if it has less.
    #             self.__shipment_three.append(delivery)
    #         else:
    #             self.__shipment_two.append(delivery)

    def get_truck_total_mileage(self):
        """Returns the total mileage for all trucks"""
        total_mileage = 0
        for truck in self.__trucks:
            total_mileage += truck.get_total_mileage()
        return total_mileage

    def get_shipment(self, package_id: int) -> Delivery:
        """Returns a package by ID"""
        return self.__shipments[package_id]

    def get_shipments(self) -> HashTable:
        """Returns all shipments"""
        return self.__shipments

    def get_trucks(self) -> list:
        """Returns all trucks"""
        return self.__trucks
