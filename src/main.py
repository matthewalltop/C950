# Author: Brian Matthew Alltop
# StudentID: 000820333
# WGU C950 - Data Structures & Algorithms 2

from shipments import Shipments
from distances import Distances

def main():
    shipments = Shipments()
    distances = Distances()

    print('\n')
    print('----- WGU C950 - Routing Algorithm Program -----')
    print('\n')
    # TODO print(f'Route was completed in {total_distance():.2f} miles.\n')

    option_list = ['1', '2', 'q']

    running = True

    # Begin the main program loop
    while running:
        selection = input("""Select an option or enter 'q' to exit the program
                          1. Display all package information
                          2. Display information for a single package\nInput> """)

        if selection.lower() not in option_list:
            print('\n----- Invalid input. Please selection a valid option below: -----\n')
        elif selection.lower() == 'q':
            break
        elif selection.lower() == '1':
            print('\nYou selected 1\n')
            #TODO: Show all package data

            print(f'Truck One: {len(shipments.get_first_shipment())} packages\n')
            for p in shipments.get_first_shipment():
                print(p)
            print('\n')
            print(f'Truck Two: {len(shipments.get_second_shipment())} packages\n')
            for p in shipments.get_second_shipment():
                print(p)
            print('\n')
            print(f'Truck Three: {len(shipments.get_third_shipment())} packages\n')
            for p in shipments.get_third_shipment():
                print(p)
            print('\n')

            # matr = distances.get_distance_matrix()
            # for m in matr:
            #     if len(m) > 0:
            #         print(m)

        elif selection.lower() == '2':
            print('\nYou selected 2\n')
            #TODO: Show single package data.
        else:
            running = False

    input('Goodbye!\n')






if __name__ == "__main__":
    # execute only if run as a script
    main()