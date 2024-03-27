# from Person import Person
class Sibling():
    def __init__(self, medical_record_num, first_name, last_name, gender):
        ##super().__init__(first_name, last_name, gender)
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._medical_record_num = medical_record_num

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

    def get_medical_record_num(self):
        return self._medical_record_num

    def set_medical_record_num(self, medical_record_num):
        self._medical_record_num = medical_record_num
