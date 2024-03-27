class Medication:
    def __init__(self, medication_name, dose_amount, dose_type, frequency, frequency_type, medication_type):
        self._medication_name = medication_name
        self._dose_amount = dose_amount
        self._dose_type = dose_type
        self._frequency = frequency
        self._frequency_type = frequency_type
        self._medication_type = medication_type

    def get_medication_name(self):
        return self._medication_name

    def set_medication_name(self, medication_name):
        self._medication_name = medication_name

    def get_dose_amount(self):
        return self._dose_amount

    def set_dose_amount(self, dose_amount):
        self._dose_amount = dose_amount

    def get_dose_type(self):
        return self._dose_type

    def set_dose_type(self, dose_type):
        self._dose_type = dose_type

    def get_frequency(self):
        return self._frequency

    def set_frequency(self, frequency):
        self._frequency = frequency

    def get_frequency_type(self):
        return self._frequency_type

    def set_frequency_type(self, frequency_type):
        self._frequency_type = frequency_type

    def get_medication_type(self):
        return self._medication_type

    def set_medication_type(self, medication_type):
        self._medication_type = medication_type
