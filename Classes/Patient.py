class Patient():
    def __init__(self, first_name, last_name, gender, medical_record_num, date_of_birth,
                 social_security_num, middle_name="", suffix="", ethnicity=""):
        # super().__init__(first_name, last_name, gender)
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self._medical_record_num = medical_record_num
        self._date_of_birth = date_of_birth
        self._social_security_num = social_security_num
        self._suffix = suffix
        self._middle_name = middle_name
        self._ethnicity = ethnicity

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

    def get_middle_name(self):
        return self._middle_name

    def set_middle_name(self, middle_name):
        self._middle_name = middle_name

    def get_suffix(self):
        return self._suffix

    def set_suffix(self, suffix):
        self._suffix = suffix

    def get_date_of_birth(self):
        return self._date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def get_social_security_num(self):
        return self._social_security_num

    def set_social_security_num(self, social_security_num):
        self._social_security_num = social_security_num

    def get_ethnicity(self):
        return self._ethnicity

    def set_ethnicity(self, ethnicity):
        self._ethnicity = ethnicity

