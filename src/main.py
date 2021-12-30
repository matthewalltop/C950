# Author: Brian Matthew Alltop
# StudentID: 000820333
# WGU C950 - Data Structures & Algorithms 2

from shipments import Shipments
from distances import Distances



def main():
    shipments = Shipments()

    print(f'First Shipment: {len(shipments.get_first_shipment())} packages')
    print(shipments.get_first_shipment())
    print(f'Second Shipment: {len(shipments.get_second_shipment())} packages')
    print(shipments.get_second_shipment())
    print(f'Third Shipment: {len(shipments.get_third_shipment())} packages')
    print(shipments.get_third_shipment())

    distances = Distances()



if __name__ == "__main__":
    # execute only if run as a script
    main()