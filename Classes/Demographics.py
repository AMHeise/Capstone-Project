#from Classes import Patient

class Demographics():
    def __init__(self, medical_record_num, first_name, last_name, gender, date_of_birth, social_security_num,
                 phone_num, ethnicity, marital_status, age="", middle_name="", suffix="", email="", deceased="", date_of_death=""):
        #super().__init__(first_name, last_name, gender, medical_record_num, middle_name, suffix, date_of_birth, social_security_num)
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        self._medical_record_num = medical_record_num
        self._date_of_birth = date_of_birth
        self._social_security_num = social_security_num
        self._suffix = suffix
        self._middle_name = middle_name
        self._phone_num = phone_num
        self._age = age
        self._ethnicity = ethnicity
        self._marital_status = marital_status
        self._email = email
        self._deceased = deceased
        self._date_of_death = date_of_death

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
        return str(self._medical_record_num)

    def set_medical_record_num(self, medical_record_num):
        self._medical_record_num = medical_record_num

    def get_middle_name(self):
        return str(self._middle_name)

    def set_middle_name(self, middle_name):
        self._middle_name = middle_name

    def get_suffix(self):
        return self._suffix

    def set_suffix(self, suffix):
        self._suffix = suffix

    def get_date_of_birth(self):
        return str(self._date_of_birth)

    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def get_social_security_num(self):
        return self._social_security_num

    def set_social_security_num(self, social_security_num):
        self._social_security_num = social_security_num

    def get_phone_num(self):
        return self._phone_num

    def set_phone_num(self, phone_num):
        self._phone_num = phone_num

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_ethnicity(self):
        return self._ethnicity

    def set_ethnicity(self, ethnicity):
        self._ethnicity = ethnicity

    def get_marital_status(self):
        return self._marital_status

    def set_marital_status(self, marital_status):
        self._marital_status = marital_status

    def get_deceased(self):
        return self._deceased

    def set_deceased(self, deceased):
        self._deceased = deceased

    def get_date_of_death(self):
        return self._date_of_death

    def set_date_of_death(self, date_of_death):
        self._date_of_death = date_of_death
