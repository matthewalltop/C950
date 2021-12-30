import csv
from hash_table import HashTable


class Shipments:
    def __init__(self):
        self.__shipment_one = []
        self.__shipment_two = []
        self.__shipment_three = []
        self.__load_packages()
        self.__shipments = None

    def __load_packages(self):
        """Reads shipment data into hash table
            Runs at O(n)"""
        self.__shipments = HashTable()
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
                status = 'At Hub'  # All packages start at the hub

                delivery = [id, address, city, state, postal_code, deadline, kilos, notes, status]

                # Load anything
                if postal_code == '84014' and deadline != '10:30':
                    self.__shipment_three.append(delivery)

                # Package Number #9 needs address corrected at 10:20am
                if 'Wrong address listed' in notes:
                    delivery[1] = '410 S State St'
                    delivery[3] = '84111'
                    self.__shipment_three.append(delivery)

                # Load anything on the first truck that has to be delivered together
                # or that has no special constraints; This will be the first truck
                # to leave so we can wait for EOD packages
                if deadline != 'EOD':
                    if 'Must' in notes or notes == '':
                        self.__shipment_one.append(delivery)

                # Add the second truck specific values to the second truck
                if 'Can Only be' in notes or 'Delayed' in notes:
                    self.__shipment_two.append(delivery)

                # If not in any other deliveries add here.
                if delivery not in self.__shipment_one and \
                   delivery not in self.__shipment_two and \
                   delivery not in self.__shipment_three:
                    if len(self.__shipment_two) > len(self.__shipment_three):  # Add to shipment three if it has less.
                        self.__shipment_three.append(delivery)
                    else:
                        self.__shipment_two.append(delivery)

                self.__shipments.insert_item(id, delivery)

    def get_hash_table(self):
        """Returns hash table containing shipment data
           Runs At: O(1)"""
        return self.__shipments

    def get_first_shipment(self):
        """ Returns the first shipment
            Runs At: O(1)"""
        return self.__shipment_one

    def get_second_shipment(self):
        """ Returns the second shipment
            Runs At: O(1)"""
        return self.__shipment_two

    def get_third_shipment(self):
        """ Returns the third shipment
            Runs At: O(1)"""
        return self.__shipment_three

