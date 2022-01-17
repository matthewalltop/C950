# Author: Brian Matthew Alltop
# StudentID: 000820333
# WGU C950 - Data Structures & Algorithms 2

import csv
from hash_table import HashTable

class Distances:
    def __init__(self):
        self.__distances = []
        self.__locations = {}
        self.__distance_matrix = HashTable()
        self.__load_distances()
        self.__load_locations()

    def __load_locations(self):
        """Reads shipment data into hash table
            Runs at O(n)"""
        locations = HashTable()
        with open('../data/locations.csv') as csvfile:
            location_data = csv.reader(csvfile)
            for row in location_data:
                row_id = int(row[0])
                location = row[1]
                address = row[2]
                distance_map = self.__get_distances()[row_id]  # Append this locations distances.
                locations[row_id] = [row_id, location, address]
                self.__distance_matrix[address] = distance_map

            self.__locations = locations

    def get_locations(self):
        return self.__locations

    def __load_distances(self):
        """Reads shipment data into hash table
            Runs at O(1)"""
        with open('../data/distances.csv') as csvfile:
            distance_data = csv.reader(csvfile, delimiter=',')
            self.__distances = list(distance_data)

    def __get_distances(self):
        return self.__distances

    def get_distance_matrix(self):
        return self.__distance_matrix

    def get_distance(self, from_address_index, to_address_index):
        """Calculates the distance between two indexes
            Runs at O(1)"""
        distance = self.__distances[from_address_index][to_address_index]
        if distance is '':
            distance = self.__distances[to_address_index][from_address_index]

        return float(distance)



