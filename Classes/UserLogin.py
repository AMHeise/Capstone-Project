class UserLogin():
    def __init__(self, username, password="", employee_id="", first_name="", last_name="", access_level=""):
        self._username = username
        self._password = password

        if employee_id != -1:
            self._employee_id = employee_id
            self._first_name = first_name
            self._last_name = last_name
            self._access_level = access_level
        else:
            # Enter in code for creating a new account. We need to know everything that would be going into this
            pass

    def get_username(self):
        return self._username

    def set_username(self, username):
        self._username = username

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_access_level(self):
        return self._access_level

    def set_access_level(self, access_level):
        self._access_level = access_level
