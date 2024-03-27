class Allergy:
    def __init__(self, allergy_name, allergy_type, date_added):
        self._allergy_name = allergy_name
        self._allergy_type = allergy_type
        self._date_added = date_added

    def get_allergy_name(self):
        return self._allergy_name

    def set_allergy_name(self, allergy_name):
        self._allergy_name = allergy_name

    def get_allergy_type(self):
        return self._allergy_type

    def set_allergy_type(self, allergy_type):
        self._allergy_type = allergy_type

    def get_date_added(self):
        return self._date_added

    def set_date_added(self, date_added):
        self._date_added = date_added
