class AppointmentTimeAndDate:
    def __init__(self, appointment_time_and_date, status="", appointment_id=""):
        self._appointment_time_and_date = appointment_time_and_date
        self._status = status
        self._appointment_id = appointment_id

    def get_appointment_time_and_date(self):
        return self._appointment_time_and_date

    def set_appointment_time_and_date(self, appointment_time_and_date):
        self._appointment_time_and_date = appointment_time_and_date

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_appointment_id(self):
        return self._appointment_id

    def set_appointment_id(self, appointment_id):
        self._appointment_id = appointment_id
