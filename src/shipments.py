import csv
from hash_table import HashTable


def run():
    shipments = HashTable()
    with open('./data/shipments.csv') as csvfile:
        distances = csv.reader(csvfile)
        for row in distances:
            id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            deadline = row[5]
            kilos = row[6]
            notes = row[7]
            shipments.add_or_update(id, [address,city,state,zip,deadline,kilos,notes])
            item = shipments.get_item(id)
            print(item)



        