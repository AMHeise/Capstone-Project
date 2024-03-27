class AppointmentStaff:
    def __init__(self, primary_provider, appointment_provider, appointment_nurse="", appointment_cna=""):
        self._primary_provider = primary_provider
        self._appointment_provider = appointment_provider
        self._appointment_nurse = appointment_nurse
        self._appointment_cna = appointment_cna

    def get_primary_provider(self):
        return self._primary_provider

    def set_primary_provider(self, primary_provider):
        self._primary_provider = primary_provider

    def get_appointment_provider(self):
        return self._appointment_provider

    def set_appointment_provider(self, appointment_provider):
        self._appointment_provider = appointment_provider

    def get_appointment_nurse(self):
        return self._appointment_nurse

    def set_appointment_nurse(self, appointment_nurse):
        self._appointment_nurse = appointment_nurse

    def get_appointment_cna(self):
        return self._appointment_cna

    def set_appointment_cna(self, appointment_cna):
        self._appointment_cna = appointment_cna
