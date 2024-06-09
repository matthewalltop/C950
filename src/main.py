# Author: Brian Matthew Alltop
# StudentID: 000820333
# WGU C950 - Data Structures & Algorithms 2
from datetime import datetime

from hub import Hub


def main():
    print('\n')
    print('----- WGUPS Package Delivery -----')
    print('\n')

    hub: Hub = Hub()
    hub.deliver_packages()

    running: bool = True

    # Begin the main program loop
    while running:
        selection = input("""Please select an option below:\n
                          1. Display all package information\n
                          2. Display information for a single package\n
                          3. Display mileage traveled by trucks\n
                          q. Exits the program\n""")

        if selection.lower() not in ['1', '2', '3', 'q']:
            print('\n----- Invalid input. Please selection a valid option below: -----\n')
            continue
        elif selection.lower() == 'q':
            break
        elif selection.lower() == '1':
            print('\nYou selected 1\n')
            time_str = input('Enter a time to display package information.(Use format HH:MM:SS)\n')
            time = datetime.strptime(time_str, '%H:%M:%S')
            for kvp in hub.shipments:
                package = kvp[1]
                print(package.get_package_status_at_time(time))
            continue
        elif selection.lower() == '2':
            print('\nYou selected 2\n')
            package_id = input("""Enter the package ID to display information for""")
            print(f'Package ID: {package_id}\n')
            id = int(package_id)
            package = hub.get_package_by_id(id)
            if package is not None:
                time_str = input(f'Enter a time to display information for package {package.id}.(Use format '
                                 f'HH:MM:SS)')
                time = datetime.strptime(time_str, '%H:%M:%S')
                print(package.get_package_status_at_time(time))
            else:
                print(f'Package ID {package_id} not found.')
            continue
        elif selection.lower() == '3':
            print('\nYou selected 3\n')
            print('Mileage traveled by trucks:')
            for truck in hub.trucks:
                print(f'Truck {truck.id}: {'{0:.3g}'.format(truck.mileage)} miles')
            print('\n')
            print(f'Truck total mileage: {'{0:.3g}'.format(sum([truck.mileage for truck in hub.trucks]))} miles\n')
            print('\n')
        else:
            running = False

    input('Goodbye!\n')


if __name__ == "__main__":
    # execute only if run as a script
    main()
