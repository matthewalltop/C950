from delivery import Delivery


class Truck:
    mileage: float

    def __init__(self, departure_time):
        self.departure_time = departure_time
        self.mileage = 0.0
        self.packages = []

    def load_package(self, package) -> None:
        self.packages.append(package)

    def get_total_mileage(self) -> int:
        return self.mileage

    def get_shipment(self, package_id: int) -> Delivery:
        return self.packages[package_id]
