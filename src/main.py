# Author: Brian Matthew Alltop
# StudentID: 000820333
# WGU C950 - Data Structures & Algorithms 2

from hub import Hub


def main():
    print('\n')
    print('----- WGU C950 - Routing Algorithm Program -----')
    print('\n')

    hub: Hub = Hub()
    running: bool = True

    # Begin the main program loop
    while running:
        selection = input("""Select an option or enter 'q' to exit the program
                          1. Display all package information
                          2. Display information for a single package\nInput> """)

        if selection.lower() not in ['1', '2', 'q']:
            print('\n----- Invalid input. Please selection a valid option below: -----\n')
        elif selection.lower() == 'q':
            break
        elif selection.lower() == '1':
            print('\nYou selected 1\n')
            packages = hub.get_shipments()
            for package in packages:
                package.print()
        elif selection.lower() == '2':
            print('\nYou selected 2\n')
            package_id = input("""Enter the package ID to display information for\nInput>""")
            print(f'Package ID: {package_id}\n')
            package = hub.get_shipment(package_id)
            if package is not None:
                package.print()
            else:
                print(f'Package ID {package_id} not found.')
        else:
            running = False

    input('Goodbye!\n')


if __name__ == "__main__":
    # execute only if run as a script
    main()
