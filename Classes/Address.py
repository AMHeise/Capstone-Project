class Address:
    def __init__(self, street_address, city, state, zip_code, apt_num="", billing_same_as_res="", guarantor_same_as_res=""):
        self._street_address = street_address
        self._city = city
        self._state = state
        self._zip_code = zip_code
        self._apt_num = apt_num
        self._billing_same_as_res = billing_same_as_res
        self._guarantor_same_as_res = guarantor_same_as_res

    def get_street_address(self):
        return self._street_address

    def set_street_address(self, street_address):
        self._street_address = street_address

    def get_apt_num(self):
        return self._apt_num

    def set_apt_num(self, apt_num):
        self._apt_num = apt_num

    def get_city(self):
        return self._city

    def set_city(self, city):
        self._city = city

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def get_zip_code(self):
        return self._zip_code

    def set_zip_code(self, zip_code):
        self._zip_code = zip_code

    def get_billing_same_as_res(self):
        return self._billing_same_as_res

    def set_billing_same_as_res(self, billing_same_as_res):
        self._billing_same_as_res

    def get_guarantor_same_as_res(self):
        return self._guarantor_same_as_res

    def set_guarantor_same_as_res(self, guarantor_same_as_res):
        self._guarantor_same_as_res
