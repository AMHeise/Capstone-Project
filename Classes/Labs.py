class Labs:
    def __init__(self, lab_type, date_requested, status):
        self._lab_type = lab_type
        self._date_requested = date_requested
        self._status = status

    def get_lab_type(self):
        return self._lab_type

    def set_lab_type(self, lab_type):
        self._lab_type = lab_type

    def get_date_requested(self):
        return self._date_requested

    def set_date_requested(self, date_requested):
        self._date_requested = date_requested

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status
