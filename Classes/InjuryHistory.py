class InjuryHistory:
    def __init__(self, description, date_occurred):
        self._description = description
        self._date_occurred = date_occurred

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_date_occurred(self):
        return self._date_occurred

    def set_date_occurred(self, date_occurred):
        self._date_occurred = date_occurred
