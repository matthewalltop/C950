import csv
from hash_table import HashTable

class Distances:
    def __init__(self):
        self.__distances = []
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
                address = row[1]
                city = row[2]
                distance_map = self.get_distances()[row_id]  # Append this locations distances.
                locations.insert_item(row_id, [row_id, address, city, distance_map])
                item = locations.get_item(row_id)
                print(item)

    def __load_distances(self):
        """Reads shipment data into hash table
            Runs at O(1)"""
        with open('../data/distances.csv') as csvfile:
            distance_data = csv.reader(csvfile, delimiter=',')
            self.__distances = list(distance_data)

    # def calculate_distance(self, currentIndex, targetIndex, running_total):

    def get_distance(self, from_address_index, to_address_index):
        """Calculates the distance between two indexes
            Runs at O(1)"""
        distance = self.__distances[from_address_index][to_address_index]
        if distance is '':
            distance = self.__distances[to_address_index][from_address_index]

        return float(distance)


