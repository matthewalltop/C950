# Author: Brian Matthew Alltop
# StudentID: 000820333
# WGU C950 - Data Structures & Algorithms 2

import csv
from hash_table import HashTable
from location import Location


class DistanceLookup:
    def __init__(self):
        self._distances = []
        self._locations = []
        self.__load_locations()
        self.__load_distances()

    def __load_locations(self):
        """Loads location data into hash table
            Runs at O(n)"""
        with open('../data/locations.csv') as csvfile:
            location_data = csv.reader(csvfile)
            for row in location_data:
                row_id = int(row[0])
                location = row[1]
                address = row[2]

                # Add the location to the internal hash table.
                self._locations.insert(row_id, Location(row_id, location, address))

    def __load_distances(self):
        """Loads distance data into list
            Runs at O(1)"""
        if not self._distances:
            with open('../data/distances.csv') as csvfile:
                distance_data = csv.reader(csvfile, delimiter=',')
                self._distances = list(distance_data)
        return self._distances

    def get_distance_between_addresses(self, from_address: str, to_address: str) -> float:
        """ Get the distance between two addresses
            :returns float
            Runs at O(n)"""
        from_location: Location = [l for l in self._locations if l.address == from_address][0]
        to_location: Location = [l for l in self._locations if l.address == to_address][0]
        return self.__get_distance(from_location.id, to_location.id)

    def __get_distance(self, from_address_index: int, to_address_index: int) -> float:
        """ Gets the numeric distance from the distance matrix using the address lookup.
            Runs at O(1)"""
        distance = self._distances[from_address_index][to_address_index]
        if distance == '':
            distance = self._distances[to_address_index][from_address_index]

        return float(distance)
