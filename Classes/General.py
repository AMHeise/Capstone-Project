class General:
    def __init__(self, weight, height_ft, height_in, smoking, drinking, exercise, drugs,
                 appointment_type, chief_complaint):
        self._weight = weight
        self._height_ft = height_ft
        self._height_in = height_in
        self._smoking = smoking
        self._drinking = drinking
        self._exercise = exercise
        self._drugs = drugs
        self._appointment_type = appointment_type
        self._chief_complaint = chief_complaint

    def get_weight(self):
        return self._weight

    def set_weight(self, weight):
        self._weight = weight

    def get_height_ft(self):
        return self._height_ft

    def set_height_ft(self, height_ft):
        self._height_ft = height_ft

    def get_height_in(self):
        return self._height_in

    def set_height_in(self, height_in):
        self._height_in = height_in

    def get_smoking(self):
        return self._smoking

    def set_smoking(self, smoking):
        self._smoking = smoking

    def get_drinking(self):
        return self._drinking

    def set_drinking(self, drinking):
        self._drinking = drinking

    def get_exercise(self):
        return self._exercise

    def set_exercise(self, exercise):
        self._exercise = exercise

    def get_drugs(self):
        return self._drugs

    def set_drugs(self, drugs):
        self._drugs = drugs

    def get_appointment_type(self):
        return self._appointment_type

    def set_appointment_type(self, appointment_type):
        self._appointment_type = appointment_type

    def get_chief_complaint(self):
        return self._chief_complaint

    def set_chief_complaint(self, chief_complaint):
        self._chief_complaint = chief_complaint
