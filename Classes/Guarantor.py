#from Person import Person

class Guarantor():
    def __init__(self, first_name, middle_name, last_name, gender, relationship, phone_num):
        #super().__init__(first_name, last_name, gender)
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._gender = gender
        self._relationship = relationship
        self._phone_num = phone_num

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_middle_name(self):
        return self._middle_name

    def set_middle_name(self, middle_name):
        self._middle_name = middle_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender

    def get_relationship(self):
        return self._relationship

    def set_relationship(self, relationship):
        self._relationship = relationship

    def get_phone_num(self):
        return self._phone_num

    def set_phone_num(self, phone_num):
        self._phone_num = phone_num
