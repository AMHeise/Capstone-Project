class OfficeLocations:
    def __init__(self, office_name, office_address=""):
        self._office_name = office_name
        self._office_address = office_address

    def get_office_name(self):
        return self._office_name

    def set_office_name(self, office_name):
        self._office_name = office_name

    def get_office_address(self):
        return self._office_address

    def set_office_address(self, office_address):
        self._office_address = office_address

