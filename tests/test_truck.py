import unittest
from unittest.mock import Mock
from faker import Faker

from package import Package
from truck import Truck


class TestTruck(unittest.TestCase):
    def setUp(self):
        self.truck = Truck('8:00:00')

    def test_load_package(self):
        mock = Mock()
        d: Package = Package(mock)
        print(d)
        self.truck.load_package(
            Package(1, '195 W Oakland Ave', 'Salt Lake City', 'UT', 84115, '2:03 PM', 1, 'Delivered'))
        result = self.truck.get_package_by_id(1)
        self.assertEqual(result.get_address(), '195 W Oakland Ave')
        self.assertEqual(result.get_address(), '195 W Oakland Ave')

    def create_package(self, id: int) -> Package:
        fake = Faker()
        return Package(id, fake.street_address(), fake.city(), fake.state_abbr(), fake.zipcode(), fake.time(), 1,
                       fake.text())


if __name__ == '__main__':
    unittest.main()
