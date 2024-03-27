class PhysicianNotes:
    def __init__(self, notes, date_added):
        self._notes = notes
        self._date_added = date_added

    def get_notes(self):
        return self._notes

    def set_notes(self, notes):
        self._notes = notes

    def get_date_added(self):
        return self._date_added

    def set_date_added(self, date_added):
        self._date_added = date_added
