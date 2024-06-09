import unittest

from hub import Hub


class TestHub(unittest.TestCase):
    def setUp(self):
        self.hub = Hub()

    def test_loads_trucks(self):
        self.assertEqual(len(self.hub.trucks), 3)

    def test_loads_shipments(self):
        self.assertEqual(len(self.hub.shipments), 40)

    def test_delivers_packages(self):
        self.hub.deliver_packages()
        self.assertEqual(len(self.hub.trucks[0].packages), 16)


if __name__ == '__main__':
    unittest.main()
