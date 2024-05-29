import unittest

from hub import Hub


class TestHub(unittest.TestCase):
    def setUp(self):
        self.hub = Hub()

    def test_loads_trucks(self):
        self.assertEqual(len(self.hub.get_trucks()), 3)

    def test_gets_initial_total_milage(self):
        self.assertEqual(self.hub.get_truck_total_mileage(), 0.0)

    def test_loads_shipments(self):
        self.assertEqual(self.hub.get_shipments().length(), 40)

    def test_gets_shipment(self):
        self.assertEqual(self.hub.get_shipment(1).get_address(), '195 W Oakland Ave')
        self.assertEqual(self.hub.get_shipment(2).get_address(), '2530 S 500 E')
        self.assertEqual(self.hub.get_shipment(3).get_address(), '380 W 2880 S')
        self.assertEqual(self.hub.get_shipment(4).get_address(), '410 S State St')
        self.assertEqual(self.hub.get_shipment(5).get_address(), '3060 Lester St')
        self.assertEqual(self.hub.get_shipment(6).get_address(), '1330 E 2100 S')
        self.assertEqual(self.hub.get_shipment(7).get_address(), '300 State St')
        self.assertEqual(self.hub.get_shipment(8).get_address(), '1344 W 200 S')
        self.assertEqual(self.hub.get_shipment(9).get_address(), '300 State St')
        self.assertEqual(self.hub.get_shipment(10).get_address(), '600 E 900 South')
        self.assertEqual(self.hub.get_shipment(11).get_address(), '2600 Taylorsville Blvd')
        self.assertEqual(self.hub.get_shipment(12).get_address(), '3575 W Valley Central Station bus Loop')
        self.assertEqual(self.hub.get_shipment(13).get_address(), '2010 W 500 S')
        self.assertEqual(self.hub.get_shipment(14).get_address(), '4300 S 1300 E')
        self.assertEqual(self.hub.get_shipment(15).get_address(), '4580 S 2300 E')
        self.assertEqual(self.hub.get_shipment(16).get_address(), '4580 S 2300 E')
        self.assertEqual(self.hub.get_shipment(17).get_address(), '1060 Dalton Ave S')
        self.assertEqual(self.hub.get_shipment(18).get_address(), '2835 Main St')
        self.assertEqual(self.hub.get_shipment(19).get_address(), '1330 2100 S')
        self.assertEqual(self.hub.get_shipment(20).get_address(), '4580 S 2300 E')
        self.assertEqual(self.hub.get_shipment(21).get_address(), '1060 Dalton Ave S')


if __name__ == '__main__':
    unittest.main()
