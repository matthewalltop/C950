import unittest

from package import Package


class TestPackage(unittest.TestCase):
    def test_package_init(self):
        package = Package(1, '123 Main St', 'Salt Lake City', 'UT', '84101', '10:30', '5', 'Fragile')
        self.assertEqual(package.id, 1)
        self.assertEqual(package.address, '123 Main St')
        self.assertEqual(package.city, 'Salt Lake City')
        self.assertEqual(package.state, 'UT')
        self.assertEqual(package.postal_code, '84101')
        self.assertEqual(package.deadline, '10:30')
        self.assertEqual(package.kilos, '5')
        self.assertEqual(package.notes, 'Fragile')

    def test_package_str(self):
        package = Package(1, '123 Main St', 'Salt Lake City', 'UT', '84101', '10:30', '5', 'Fragile')
        self.assertEqual(str(package), 'Package ID: 1, Address: 123 Main St, City: Salt Lake City, State: UT, Postal Code: 84101, Deadline: 10:30, Kilos: 5, Notes: Fragile, Delivery Time: , Current Location: PackageStatus.AtHub')


if __name__ == '__main__':
    unittest.main()
