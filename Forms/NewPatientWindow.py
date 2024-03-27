from PySide6.QtWidgets import QMainWindow, QPushButton, QLineEdit, QComboBox, QGroupBox, QButtonGroup, QRadioButton, \
    QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QAction
from Classes import Address
from Classes import Demographics
from MedicalRecords.Source import db_access

import traceback

from Forms import MedicalRecordWindow, HomePage, PatientLookup, Login


class NewPatient(QMainWindow):

    def __init__(self, current_user, selected_location):
        super().__init__()
        self.loader = QUiLoader()

        self.current_user = current_user
        self.selected_location = selected_location

        # Initialize Form
        self.new_patient_window = self.loader.load("Forms/newPatientWindow.ui")

        # Initialize Sub-Forms
        self.medical_records_window = MedicalRecordWindow.MedicalRecord
        self.homepage = HomePage.HomePage
        self.patient_lookup = PatientLookup.PatientLookup
        self.login = Login.Login

        # Initialize Buttons
        self.submit_button = self.new_patient_window.findChild(QPushButton, "submit_pushButton")
        self.submit_button.clicked.connect(self.on_submit_button_clicked)

        # ------ Remove if database is active ----- #
        # self.mrn = "202301"
        # self.current_user = "Test"

        # Set Actions
        self.actionhome = self.new_patient_window.findChild(QAction, "actionhome")
        self.actionhome.triggered.connect(self.on_actionhome_clicked)
        icon9 = QIcon("Images/home.png")
        self.actionhome.setIcon(icon9)
        self.actionnewPatient = self.new_patient_window.findChild(QAction, "actionnewPatient")
        self.actionnewPatient.triggered.connect(self.on_actionnewPatient_clicked)
        icon10 = QIcon("Images/plus-button.png")
        self.actionnewPatient.setIcon(icon10)
        self.actionpatientSearch = self.new_patient_window.findChild(QAction, "actionpatientSearch")
        self.actionpatientSearch.triggered.connect(self.on_actionpatientSearch_clicked)
        icon11 = QIcon("Images/magnifier.png")
        self.actionpatientSearch.setIcon(icon11)
        self.actionlogout = self.new_patient_window.findChild(QAction, "actionlogout")
        self.actionlogout.triggered.connect(self.on_actionlogout_clicked)
        icon12 = QIcon("Images/door-arrow.png")
        self.actionlogout.setIcon(icon12)

        # Initialize Text Fields
        self.mrn_lineEdit = self.new_patient_window.findChild(QLineEdit, "mrn_lineEdit")
        self.mrn_lineEdit.setReadOnly(True)
        self.first_name_lineEdit = self.new_patient_window.findChild(QLineEdit, "first_name_lineEdit")
        self.middle_name_lineEdit = self.new_patient_window.findChild(QLineEdit, "middle_name_lineEdit")
        self.last_name_lineEdit = self.new_patient_window.findChild(QLineEdit, "last_name_lineEdit")
        self.jr_radioButton = self.new_patient_window.findChild(QRadioButton, "jr_radioButton")
        self.sr_radioButton = self.new_patient_window.findChild(QRadioButton, "sr_radioButton")
        self.I_radioButton = self.new_patient_window.findChild(QRadioButton, "I_radioButton")
        self.II_radioButton = self.new_patient_window.findChild(QRadioButton, "II_radioButton")
        self.III_radioButton = self.new_patient_window.findChild(QRadioButton, "III_radioButton")
        self.na_radioButton = self.new_patient_window.findChild(QRadioButton, "radioButton_6")
        self.date_of_birth_lineEdit = self.new_patient_window.findChild(QLineEdit, "date_of_birth_lineEdit")
        self.ssn_lineEdit = self.new_patient_window.findChild(QLineEdit, "ssn_lineEdit")
        self.street_address_lineEdit = self.new_patient_window.findChild(QLineEdit, "street_address_lineEdit")
        self.new_patient_apt_lineEdit = self.new_patient_window.findChild(QLineEdit, "new_patient_apt_lineEdit")
        self.city_lineEdit = self.new_patient_window.findChild(QLineEdit, "city_lineEdit")
        self.new_patient_state_comboBox = self.new_patient_window.findChild(QComboBox, "new_patient_state_comboBox")
        self.zip_code_lineEdit = self.new_patient_window.findChild(QLineEdit, "zip_code_lineEdit")
        self.phone_number_lineEdit = self.new_patient_window.findChild(QLineEdit, "phone_number_lineEdit")
        self.email_lineEdit = self.new_patient_window.findChild(QLineEdit, "email_lineEdit")
        self.male_radioButton = self.new_patient_window.findChild(QRadioButton, "radioButton")
        self.female_radioButton = self.new_patient_window.findChild(QRadioButton, "radioButton_2")
        self.other_radioButton = self.new_patient_window.findChild(QRadioButton, "radioButton_3")

    def on_actionlogout_clicked(self):
        self.login = self.login()
        self.login.initialize_login()
        self.new_patient_window.close()

    def on_actionpatientSearch_clicked(self):
        self.patient_lookup = self.patient_lookup(self.current_user, self.selected_location)
        self.patient_lookup.initialize_patient_lookup()
        self.new_patient_window.close()

    def on_actionnewPatient_clicked(self):
        pass
        # clear all fields

    def on_actionhome_clicked(self):
        self.homepage = self.homepage(self.current_user, self.selected_location)
        self.homepage.initialize_homepage()
        self.new_patient_window.close()

    def initialize_new_patient_window(self):
        mrn = db_access.get_mrn()
        updated_mrn = mrn + 1
        self.mrn_lineEdit.setText(str(updated_mrn))
        self.new_patient_window.show()

    # Button On-Click
    def on_submit_button_clicked(self):
        self.errors = self.verify_info()
        if self.errors:
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, One of the entries is not valid.")
            # show the message box
            msg_box.exec_()
        """    
        else:
            self.medical_records_window = self.medical_records_window(self.current_user, self.selected_location)
            self.medical_records_window.initialize_medical_record_window()
            self.new_patient_window.close()
        """

    def get_selected_suffix(self):
        if self.jr_radioButton.isChecked():
            suffix = "Jr."
        elif self.sr_radioButton.isChecked():
            suffix = "Sr."
        elif self.I_radioButton.isChecked():
            suffix = "I"
        elif self.II_radioButton.isChecked():
            suffix = "II"
        elif self.III_radioButton.isChecked():
            suffix = "III"
        elif self.na_radioButton.isChecked():
            suffix = "na"
        else:
            print("Error, choose a suffix field")

        return suffix

    def get_selected_sex(self):
        if self.male_radioButton.isChecked():
            sex = "Male"
        elif self.female_radioButton.isChecked():
            sex = "Female"
        elif self.other_radioButton.isChecked:
            sex = "Other"
        else:
            pass

        return sex

    def initialize_variables(self):
        self.medical_record_number = self.mrn_lineEdit.text()

        self.first_name = self.first_name_lineEdit.text()
        self.middle_name = self.middle_name_lineEdit.text()
        self.last_name = self.last_name_lineEdit.text()

        # Figure out selected Suffix
        self.suffix = self.get_selected_suffix()

        # Figure out the selected sex group box option
        self.sex = self.get_selected_sex()

        self.date_of_birth = self.date_of_birth_lineEdit.text()
        self.ssn = self.ssn_lineEdit.text()
        self.street_address = self.street_address_lineEdit.text()
        self.apt_number = self.new_patient_apt_lineEdit.text()
        self.city = self.city_lineEdit.text()


        # Figure out the selected state combo box option
        self.state = self.new_patient_window.findChild(QComboBox, "new_patient_state_comboBox")


        self.zip_code = self.zip_code_lineEdit.text()
        self.phone_number = self.phone_number_lineEdit.text()
        self.email = self.email_lineEdit.text()

    def verify_info(self):

        self.failure_message = QMessageBox()
        self.failure_message.setWindowTitle("Error")

        try:
            self.initialize_variables()

            if isinstance(int(self.medical_record_number), (int, float)):
                #self.medical_record_number = int(self.medical_record_number)
                print("MRN: Good")

                if self.first_name != "":
                    print("First Name: Good")

                    if self.middle_name != "":
                        print("Middle Name: Good")

                        if self.last_name != "":
                            print("Last Name: Good")

                            if isinstance(int(self.date_of_birth), int):
                                self.date_of_birth_month = self.date_of_birth[:2]
                                self.date_of_birth_day = self.date_of_birth[2:4]
                                self.date_of_birth_year = self.date_of_birth[4:]
                                # self.date_of_birth_string = f"{self.date_of_birth_month}-" \
                                 #                           f"{self.date_of_birth_day}-" \
                                  #                          f"{self.date_of_birth_year}"
                                self.date_of_birth_string = f"{self.date_of_birth_year}-" \
                                                            f"{self.date_of_birth_month}-" \
                                                            f"{self.date_of_birth_day}"
                                # print(self.date_of_birth_string)
                                print("DoB: Good")

                                if isinstance(int(self.ssn), int):

                                    print("SSN: Good")

                                    if self.street_address != "":
                                        print("Street Address: Good")

                                        if self.apt_number != "":
                                            print("Apt#: Good")

                                            if self.city != "":
                                                print("City: Good")

                                                if self.zip_code != "":
                                                    print("Zip: Good")

                                                    if self.phone_number != "" and isinstance(int(self.phone_number),
                                                                                              int):
                                                        print("Phone Num: Good")

                                                        if self.email != "":
                                                            print("Email: Good")

                                                            print("Verify Success")
                                                            self.mrn = str(self.medical_record_number)
                                                            self.create_patient()

                                                        else:
                                                            print("Email: Bad")
                                                            self.failure_message.setText(f"Email Not Valid.")
                                                            self.failure_message.exec()

                                                    else:
                                                        print("Phone Num: Bad")
                                                        self.failure_message.setText(f"Phone Number Not Valid.")
                                                        self.failure_message.exec()

                                                else:
                                                    print("Zip: Bad")
                                                    self.failure_message.setText(f"Zip Not Valid.")
                                                    self.failure_message.exec()

                                            else:
                                                print("City: Bad")
                                                self.failure_message.setText(f"City Not Valid.")
                                                self.failure_message.exec()

                                        else:
                                            print("Apt#: Bad")
                                            self.failure_message.setText(f"Apt# Not Valid.")
                                            self.failure_message.exec()

                                    else:
                                        print("Street Address: Bad")
                                        self.failure_message.setText(f"Street Address Not Valid.")
                                        self.failure_message.exec()

                                else:
                                    print("SSN: Bad")
                                    self.failure_message.setText(f"SSN Not Valid.")
                                    self.failure_message.exec()

                            else:
                                print("DOB: Bad")
                                self.failure_message.setText(f"First Name Not Valid.")
                                self.failure_message.exec()

                        else:
                            print("Last Name: Bad")
                            self.failure_message.setText(f"Last Name Not Valid.")
                            self.failure_message.exec()

                    else:
                        print("Middle Name: Bad")
                        self.failure_message.setText(f"Middle Name Not Valid.")
                        self.failure_message.exec()

                else:
                    print("First Name: Bad")
                    self.failure_message.setText(f"First Name Not Valid.")
                    self.failure_message.exec()
            else:
                print("MRN: Bad")
                self.failure_message.setText(f"Medical Record Number Not Valid.")
                self.failure_message.exec()
        except Exception as bad_input:
            print("Bad input: ", bad_input)
            self.failure_message.setText(f"One of the entries is not valid.")
            self.failure_message.exec()
            traceback.print_exc()

    def create_patient(self):
        print("In create patient")
        self.ethnicity = "Other"
        self.marital_status = "Single"
        self.age = "10"
        selectedIndex = self.state.currentIndex()
        state_option = state_options.get(selectedIndex)

        if self.medical_record_number == "":
            self.bad_mrn = QMessageBox()
            self.bad_mrn.setWindowTitle("Error - Patient not added")
            self.bad_mrn.setText("Medical Record Number was left empty")
            self.bad_mrn.exec()
        else:
            try:
                print("In try catch")
                patient_info = Demographics.Demographics(self.medical_record_number,
                                            self.first_name,
                                            self.last_name,
                                            self.sex,
                                            self.date_of_birth_string,
                                            self.ssn,
                                            self.phone_number,
                                            self.ethnicity,
                                            self.marital_status,
                                            self.age,
                                            self.middle_name,
                                            self.suffix,
                                            self.email)

                patient_address_info = Address.Address(self.street_address,
                                               self.city,
                                               state_option,
                                               self.zip_code,
                                               self.apt_number)

                self.save_patient_to_database(patient_info, patient_address_info)

            except Exception as error:
                print(f"Try/Except: Error")
                self.failure_message = QMessageBox()
                self.failure_message.setWindowTitle("Error")
                self.failure_message.setText(f"Patient was not added.")
                self.failure_message.exec()
                print(f"Error\n{error}")
                traceback.print_exc()

    def open_medical_record_window(self, patient_info, patient_address_info):
        print("END OF NewPatientWindow.py")
        self.medical_records_window = self.medical_records_window(self.current_user, self.selected_location)
        self.medical_records_window.initialize_medical_record_window()

        self.medical_records_window.set_patient_info_to_display(patient_info)

        # Setting the fields on Demographics Tab
        self.medical_records_window.first_name_lineEdit.setText(patient_info.get_first_name())
        self.medical_records_window.middle_name_lineEdit.setText(patient_info.get_middle_name())
        self.medical_records_window.last_name_lineEdit.setText(patient_info.get_last_name())
        self.medical_records_window.set_suffix_radio_buttons(patient_info)
        self.medical_records_window.dob_lineEdit.setText(patient_info.get_date_of_birth())
        self.medical_records_window.set_gender_radio_buttons(patient_info)
        self.medical_records_window.ethnicity_comboBox.setCurrentText(patient_info.get_ethnicity())
        self.medical_records_window.ssn_lineEdit.setText(patient_info.get_social_security_num())
        self.medical_records_window.phone_number_lineEdit.setText(patient_info.get_phone_num())
        self.medical_records_window.email_address_lineEdit.setText(patient_info.get_email())
        self.medical_records_window.marital_status_comboBox.setCurrentText(patient_info.get_marital_status())
        if patient_info.get_deceased():
            self.medical_records_window.deceased_checkBox.select()
            self.medical_records_window.date_of_death_lineEdit.get_date_of_death()
        self.medical_records_window.res_street_address_lineEdit.setText(patient_address_info.get_street_address())
        self.medical_records_window.res_apt_lineEdit.setText(patient_address_info.get_apt_num())
        self.medical_records_window.res_city_lineEdit.setText(patient_address_info.get_city())
        self.medical_records_window.res_state_comboBox.setCurrentText(patient_address_info.get_state())
        self.medical_records_window.res_zipcode_lineEdit.setText(patient_address_info.get_zip_code())

        self.new_patient_window.close()

    def save_patient_to_database(self, patient_info, patient_address_info):

        # Get a valid AddressID
        address_id = 1
        conn = db_access.connect()
        query = f"SELECT MAX(AddressID) FROM MRAddress"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            highest_address_id = c.fetchone()[0]
            conn.commit()

        print("Highest AddressID: ", highest_address_id)
        address_id = highest_address_id + 1

        # Check to see if there is a record with the mrn already in the MRPatient Table
        conn = db_access.connect()
        query = f"SELECT COUNT(*) FROM MRPatient WHERE MRN = {patient_info.get_medical_record_num()}"

        with db_access.closing(conn.cursor()) as c:
            c.execute(query)
            result = c.fetchone()[0]
            conn.commit()

        if result != 0:
            print(f"The MRN is in the MRPatient Table {result} times.")
            print("Patient MRN was already in the database")
            print("Patient not added")

            # Message Box
            self.used_mrn_message = QMessageBox()
            self.used_mrn_message.setWindowTitle("Error - MRN already used.")
            self.used_mrn_message.setText(f"The MRN '{patient_info.get_medical_record_num()}' is already assigned to a patient.")
            self.used_mrn_message.exec()
        else:

            db_access.create_new_patient(patient_info.get_medical_record_num(),
                                         patient_info.get_first_name(),
                                         patient_info.get_last_name(),
                                         patient_info.get_gender(),
                                         patient_info.get_date_of_birth(),
                                         patient_info.get_social_security_num(),
                                         patient_info.get_middle_name(),
                                         patient_info.get_suffix())

            # Save the additional columns
            conn = db_access.connect()
            query = f"UPDATE MRPatient " \
                    f"SET PhoneNum = '{patient_info.get_phone_num()}', " \
                    f"     Email = '{patient_info.get_email()}'" \
                    f"WHERE MRN = {patient_info.get_medical_record_num()}"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()

            print("Patient Added")

            conn = db_access.connect()
            query = f"INSERT INTO MRAddress (MRN, StreetAddress, City, State, ZipCode, AptNum, AddressID)" \
                    f"VALUES ({patient_info.get_medical_record_num()}, '{patient_address_info.get_street_address()}'," \
                    f" '{patient_address_info.get_city()}', '{patient_address_info.get_state()}'," \
                    f" '{patient_address_info.get_zip_code()}', '{patient_address_info.get_apt_num()}', '{address_id}')"

            with db_access.closing(conn.cursor()) as c:
                c.execute(query)
                conn.commit()
            print("Address Added")

            # Message Box
            self.confirm_creation_message = QMessageBox()
            self.confirm_creation_message.setWindowTitle("Patient has been added")
            self.confirm_creation_message.setText(f"{self.first_name} {self.last_name} has been added.")
            self.confirm_creation_message.exec()

            print(f"About to open MedicalRecordWindow")
            self.open_medical_record_window(patient_info, patient_address_info)

state_options = {
    0: 'Alabama',
    1: 'Alaska',
    2: 'Arizona',
    3: 'Arkansas',
    4: 'California',
    5: 'Colorado',
    6: 'Connecticut',
    7: 'Delaware',
    8: 'Florida',
    9: 'Georgia',
    10: 'Hawaii',
    11: 'Idaho',
    12: 'Illinois',
    13: 'Indiana',
    14: 'Iowa',
    15: 'Kansas',
    16: 'Kentucky',
    17: 'Louisiana',
    18: 'Maine',
    19: 'Maryland',
    20: 'Massachusetts',
    21: 'Michigan',
    22: 'Minnesota',
    23: 'Mississippi',
    24: 'Missouri',
    25: 'Montana',
    26: 'Nebraska',
    27: 'Nevada',
    28: 'New Hampshire',
    29: 'New Jersey',
    30: 'New Mexico',
    31: 'New York',
    32: 'North Carolina',
    33: 'North Dakota',
    34: 'Ohio',
    35: 'Oklahoma',
    36: 'Oregon',
    37: 'Pennsylvania',
    38: 'Rhode Island',
    39: 'South Carolina',
    40: 'South Dakota',
    41: 'Tennessee',
    42: 'Texas',
    43: 'Utah',
    44: 'Vermont',
    45: 'Virginia',
    46: 'Washington',
    47: 'West Virginia',
    48: 'Wisconsin',
    49: 'Wyoming'
}
