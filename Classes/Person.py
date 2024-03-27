class Person:
    def __init__(self, first_name, last_name, gender):
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender
