class MedicalRecordAuditLog:
    def __init__(self, field_changed, employee_id, first_name, last_name, date_changed):
        self._field_changed = field_changed
        self._employee_id = employee_id
        self._first_name = first_name
        self._last_name = last_name
        self._date_changed = date_changed

    def get_field_changed(self):
        return self._field_changed

    def set_field_changed(self, field_changed):
        self._field_changed = field_changed

    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_date_changed(self):
        return self._date_changed

    def set_date_changed(self, date_changed):
        self._date_changed = date_changed
