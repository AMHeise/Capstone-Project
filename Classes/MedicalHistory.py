class MedicalHistory:
    def __init__(self, diagnosis, history_type):
        self._diagnosis = diagnosis
        self._history_type = history_type

    def get_diagnosis(self):
        return self._diagnosis

    def set_diagnosis(self, diagnosis):
        self._diagnosis = diagnosis

    def get_history_type(self):
        return self._history_type

    def set_history_type(self, history_type):
        self._history_type = history_type
