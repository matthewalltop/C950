class Location:
    def __init__(self, id: int, location: str, address: str):
        self._id = id
        self._location = location
        self._address = address

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    def location(self, value: str) -> None:
        self._location = value

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        self._address = value
