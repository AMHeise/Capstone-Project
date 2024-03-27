from PySide6.QtWidgets import QMainWindow, QPushButton, QLineEdit, QListWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QAction
import os
import pyodbc
import sys
from contextlib import closing

from Forms import OpenPatientMenu, Login, HomePage, NewPatientWindow


class PatientLookup(QMainWindow):

    def __init__(self, current_user, selected_location):
        super().__init__()
        self.loader = QUiLoader()

        self.current_user = current_user
        self.selected_location = selected_location

        # Initialize Form
        self.patient_lookup = self.loader.load("Forms/patientLookup.ui")

        # Initialize Sub-Forms
        self.open_patient_menu = OpenPatientMenu.OpenPatientMenu
        self.login = Login.Login
        self.homepage = HomePage.HomePage
        self.new_patient = NewPatientWindow.NewPatient

        # Initialize Patient Lookup Button
        self.select_patient_record_pushButton = self.patient_lookup.findChild(QPushButton, "select_patient_record_pushButton")
        self.select_patient_record_pushButton.clicked.connect(self.on_select_patient_record_button_clicked)

        # Initialize Clear Search Results Button
        self.clear_search_results_pushButton = self.patient_lookup.findChild(QPushButton, "clear_search_results_pushButton")
        self.clear_search_results_pushButton.clicked.connect(self.on_clear_search_results_pushButton_clicked)

        # Initialize Patient Lookup Search Button
        self.patient_lookup_search_pushButton = self.patient_lookup.findChild(QPushButton, "patient_lookup_search_pushButton")
        self.patient_lookup_search_pushButton.clicked.connect(self.on_patient_lookup_search_pushButton_clicked)

        # Set Actions
        self.actionhome = self.patient_lookup.findChild(QAction, "actionhome")
        self.actionhome.triggered.connect(self.on_actionhome_clicked)
        icon9 = QIcon("Images/home.png")
        self.actionhome.setIcon(icon9)
        self.actionnewPatient = self.patient_lookup.findChild(QAction, "actionnewPatient")
        self.actionnewPatient.triggered.connect(self.on_actionnewPatient_clicked)
        icon10 = QIcon("Images/plus-button.png")
        self.actionnewPatient.setIcon(icon10)
        self.actionpatientSearch = self.patient_lookup.findChild(QAction, "actionpatientSearch")
        self.actionpatientSearch.triggered.connect(self.on_actionpatientSearch_clicked)
        icon11 = QIcon("Images/magnifier.png")
        self.actionpatientSearch.setIcon(icon11)
        self.actionlogout = self.patient_lookup.findChild(QAction, "actionlogout")
        self.actionlogout.triggered.connect(self.on_actionlogout_clicked)
        icon12 = QIcon("Images/door-arrow.png")
        self.actionlogout.setIcon(icon12)

        # Initialize Text Fields
        self.first_name_lineEdit = self.patient_lookup.findChild(QLineEdit, "first_name_lineEdit")
        self.last_name_lineEdit = self.patient_lookup.findChild(QLineEdit, "last_name_lineEdit")
        self.date_of_birth_lineEdit = self.patient_lookup.findChild(QLineEdit, "date_of_birth_lineEdit")
        self.ssn_lineEdit = self.patient_lookup.findChild(QLineEdit, "ssn_lineEdit")
        self.mrn_lineEdit = self.patient_lookup.findChild(QLineEdit, "mrn_lineEdit")
        self.patient_search_list_tableView = self.patient_lookup.findChild(QListWidget, "patient_search_list_tableView")

    def on_actionlogout_clicked(self):
        self.login = self.login()
        self.login.initialize_login()
        self.patient_lookup.close()

    def on_actionpatientSearch_clicked(self):
        pass
        # clear all fields

    def on_actionnewPatient_clicked(self):
        pass
        self.new_patient = self.new_patient(self.current_user, self.selected_location)
        self.new_patient.initialize_new_patient_window()
        self.patient_lookup.close()

    def on_actionhome_clicked(self):
        self.homepage = self.homepage(self.current_user, self.selected_location)
        self.homepage.initialize_homepage()
        self.patient_lookup.close()

    def initialize_patient_lookup(self):
        self.patient_lookup.show()

    # Button On-Click
    def on_select_patient_record_button_clicked(self):
        """
        # comment out if database is active
        patient_info = {'first_name': "John", 'last_name': "Doe", 'gender': "Male", 'MRN': "111111", 'DOB': "1997-09-01", "ssn": "123-45-6789"}
        app_info = {'app_time_and_date': "4/3/2023, 10:30 AM", 'status': False}
        general_info = {'weight': 190, 'height_ft': 5, 'height_in': 10, 'smoking': False, 'drinking': False, 'exercise': True, 'drugs': False, 'app_type': "Wellness Check", 'chief_complaint': "Upset Stomach"}

        self.OpenPatientMenu.get_patient_app_info();
        """
        selected_item = self.patient_search_list_tableView.currentItem()
        if selected_item:
            mrn_str = selected_item.text().split(", ")[0].split(": ")[1]
            self.open_patient_menu = self.open_patient_menu(self.current_user, self.selected_location, mrn_str)
            self.open_patient_menu.initialize_open_patient_menu_window()
            self.patient_lookup.close()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, please make a selection.")
            msg_box.exec_()

    def on_clear_search_results_pushButton_clicked(self):
        self.first_name_lineEdit.setText("")
        self.last_name_lineEdit.setText("")
        self.date_of_birth_lineEdit.setText("")
        self.ssn_lineEdit.setText("")
        self.mrn_lineEdit.setText("")
        self.patient_search_list_tableView.clear()

    def on_patient_lookup_search_pushButton_clicked(self):
        self.first_name = self.first_name_lineEdit.text()
        self.last_name = self.last_name_lineEdit.text()
        self.date_of_birth = self.date_of_birth_lineEdit.text()
        self.ssn = self.ssn_lineEdit.text()
        self.mrn = self.mrn_lineEdit.text()

        if self.first_name != "" and self.last_name == "" and self.date_of_birth == "" and self.ssn == "" and self.mrn == "":
            # call the db to get all patient with matching first name
            results = self.get_patients_by_first_name(self.first_name)
        elif self.first_name == "" and self.last_name != "" and self.date_of_birth == "" and self.ssn == "" and self.mrn == "":
            # call the db to get all patient with matching last name
            results = self.get_patients_by_last_name(self.last_name)
        elif self.first_name == "" and self.last_name == "" and self.date_of_birth != "" and self.ssn == "" and self.mrn == "":
            # call the db to get all patient with matching date of birth
            results = self.get_patients_by_date_of_birth(self.date_of_birth)
        elif self.first_name == "" and self.last_name == "" and self.date_of_birth == "" and self.ssn != "" and self.mrn == "":
            # call the db to get all patient with matching ssn
            results = self.get_patients_by_ssn(self.ssn)
        elif self.first_name == "" and self.last_name == "" and self.date_of_birth == "" and self.ssn == "" and self.mrn != "":
            # call the db to get all patient with matching mrn
            results = self.get_patients_by_mrn(self.mrn)
        elif self.first_name != "" and self.last_name != "" and self.date_of_birth == "" and self.ssn == "" and self.mrn == "":
            # call the db to get all patient with matching first name and last name
            results = self.get_patients_by_first_last_name(self.first_name, self.last_name)
        elif self.first_name != "" and self.last_name == "" and self.date_of_birth != "" and self.ssn == "" and self.mrn == "":
            # call the db to get all patient with matching first name and date of birth
            results = self.get_patients_by_first_name_and_dob(self.first_name, self.date_of_birth)
        elif self.first_name != "" and self.last_name == "" and self.date_of_birth == "" and self.ssn != "" and self.mrn == "":
            # call the db to get all patient with matching first name and ssn
            results = self.get_patients_by_first_name_and_ssn(self.first_name, self.ssn)
        elif self.first_name != "" and self.last_name == "" and self.date_of_birth == "" and self.ssn == "" and self.mrn != "":
            # call the db to get all patient with matching first name and mrn
            results = self.get_patients_by_first_name_and_mrn(self.first_name, self.mrn)
        elif self.first_name == "" and self.last_name != "" and self.date_of_birth != "" and self.ssn == "" and self.mrn == "":
            # call the db to get all patient with matching last name and date of birth
            results = self.get_patients_by_last_name_and_dob(self.last_name, self.date_of_birth)
        elif self.first_name == "" and self.last_name != "" and self.date_of_birth == "" and self.ssn != "" and self.mrn == "":
            # call the db to get all patient with matching last name and ssn
            results = self.get_patients_by_last_name_and_ssn(self.last_name, self.ssn)
        elif self.first_name == "" and self.last_name != "" and self.date_of_birth == "" and self.ssn == "" and self.mrn != "":
            # call the db to get all patient with matching last name and mrn
            results = self.get_patients_by_last_name_and_mrn(self.last_name, self.mrn)
        elif self.first_name == "" and self.last_name == "" and self.date_of_birth != "" and self.ssn != "" and self.mrn == "":
            # call the db to get all patient with matching date of birth and ssn
            results = self.get_patients_by_dob_and_ssn(self.date_of_birth, self.ssn)
        elif self.first_name == "" and self.last_name == "" and self.date_of_birth != "" and self.ssn == "" and self.mrn != "":
            # call the db to get all patient with matching date of birth and mrn
            results = self.get_patients_by_dob_and_mrn(self.date_of_birth, self.mrn)
        elif self.first_name == "" and self.last_name == "" and self.date_of_birth == "" and self.ssn != "" and self.mrn != "":
            # call the db to get all patient with matching ssn and mrn
            results = self.get_patients_by_ssn_and_mrn(self.ssn, self.mrn)
        elif self.first_name != "" and self.last_name != "" and self.date_of_birth != "" and self.ssn == "" and self.mrn == "":
            # call the db to get all patient with matching first name, last name, and date of birth
            results = self.get_patients_by_name_dob(self.first_name, self.last_name, self.date_of_birth)
        elif self.first_name != "" and self.last_name != "" and self.date_of_birth == "" and self.ssn != "" and self.mrn == "":
            # call the db to get all patient with matching first name, last name, and ssn
            results = self.get_patients_by_name_ssn(self.first_name, self.last_name, self.ssn)
        elif self.first_name != "" and self.last_name != "" and self.date_of_birth == "" and self.ssn == "" and self.mrn != "":
            # call the db to get all patient with matching first name, last name, and mrn
            results = self.get_patients_by_name_mrn(self.first_name, self.last_name, self.mrn)
        elif self.first_name != "" and self.last_name == "" and self.date_of_birth != "" and self.ssn != "" and self.mrn == "":
            # call the db to get all patient with matching first name, date of birth, and ssn
            results = self.get_patients_by_fname_dob_ssn(self.first_name, self.date_of_birth, self.ssn)
        elif self.first_name != "" and self.last_name == "" and self.date_of_birth != "" and self.ssn == "" and self.mrn != "":
            # call the db to get all patient with matching first name, date of birth, and mrn
            results = self.get_patients_by_name_dob_mrn(self.first_name, self.date_of_birth, self.mrn)
        elif self.first_name != "" and self.last_name == "" and self.date_of_birth == "" and self.ssn != "" and self.mrn != "":
            # call the db to get all patient with matching first name, ssn, and mrn
            results = self.get_patients_by_name_ssn_mrn(self.first_name, self.ssn, self.mrn)
        elif self.first_name == "" and self.last_name != "" and self.date_of_birth != "" and self.ssn != "" and self.mrn == "":
            # call the db to get all patient with matching last name, date of birth, and ssn
            results = self.get_patients_by_name_dob_ssn(self.last_name, self.date_of_birth, self.ssn)
        elif self.first_name == "" and self.last_name != "" and self.date_of_birth != "" and self.ssn == "" and self.mrn != "":
            # call the db to get all patient with matching last name, date of birth, and mrn
            results = self.get_patients_by_last_name_dob_mrn(self.last_name, self.date_of_birth, self.mrn)
        elif self.first_name == "" and self.last_name != "" and self.date_of_birth == "" and self.ssn != "" and self.mrn != "":
            # call the db to get all patient with matching last name, ssn, and mrn
            results = self.get_patients_by_last_name_ssn_mrn(self.last_name, self.ssn, self.mrn)
        elif self.first_name == "" and self.last_name == "" and self.date_of_birth != "" and self.ssn != "" and self.mrn != "":
            # call the db to get all patient with matching date of birth, ssn, and mrn
            results = self.get_patients_by_dob_ssn_mrn(self.date_of_birth, self.ssn, self.mrn)
        elif self.first_name != "" and self.last_name != "" and self.date_of_birth != "" and self.ssn != "" and self.mrn == "":
            # call the db to get all patient with matching first name, last name, date of birth, and ssn
            results = self.get_patients_by_full_name_dob_ssn(self.first_name, self.last_name, self.date_of_birth, self.ssn)
        elif self.first_name != "" and self.last_name != "" and self.date_of_birth != "" and self.ssn == "" and self.mrn != "":
            # call the db to get all patient with matching first name, last name, date of birth, and mrn
            results = self.get_patients_by_full_name_dob_mrn(self.first_name, self.last_name, self.date_of_birth, self.mrn)
        elif self.first_name == "" and self.last_name != "" and self.date_of_birth != "" and self.ssn != "" and self.mrn != "":
            # call the db to get all patient with matching last name, date of birth, ssn, and mrn
            results = self.get_patients_by_name_dob_ssn_mrn(self.last_name, self.date_of_birth, self.ssn, self.mrn)
        elif self.first_name != "" and self.last_name == "" and self.date_of_birth != "" and self.ssn != "" and self.mrn != "":
            # call the db to get all patient with matching first name, date of birth, ssn, and mrn
            results = self.get_patients_by_first_name_dob_ssn_mrn(self.first_name, self.date_of_birth, self.ssn, self.mrn)
        elif self.first_name != "" and self.last_name != "" and self.date_of_birth != "" and self.ssn != "" and self.mrn != "":
            # call the db to get all patient with matching first name, last name, date of birth, ssn, and mrn
            results = self.get_patients_by_full_name_dob_ssn_mrn(self.first_name, self.last_name, self.date_of_birth, self.ssn, self.mrn)
        elif self.first_name == "" and self.last_name == "" and self.date_of_birth == "" and self.ssn == "" and self.mrn == "":
            # show message box that input cannot be empty
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, Input cannot be empty.")
            msg_box.exec_()

        else:
            # show message box that input is invalid
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, Input is invalid.")
            msg_box.exec_()

        for result in results:
            mrn_str = str(result[0])
            item = f"MRN: {mrn_str}, {result[1]} {result[2]}, DOB: {result[4]}, SSN: {result[5]}"
            self.patient_search_list_tableView.addItem(item)

    # -------------------------------------------------------------------------------------------------------------

    # Call connection
    @staticmethod
    def connect():
        try:
            if sys.platform == "win32":
                db = "Driver={ODBC Driver 18 for SQL Server};" \
                     "Server=tcp:capstone2023.database.windows.net,1433;" \
                     "Database=capstone2023;" \
                     "Uid=medRecordsUser;" \
                     "Pwd=Password01!;" \
                     "Encrypt=yes;" \
                     "TrustServerCertificate=no;" \
                     "Connection Timeout=30;"
            else:
                home = os.environ["HOME"]
                db = home + "Driver={ODBC Driver 18 for SQL Server};" \
                            "Server=tcp:capstone2023.database.windows.net,1433;" \
                            "Database=capstone2023;" \
                            "Uid=medRecordsUser;" \
                            "Pwd=Password01!;" \
                            "Encrypt=yes;" \
                            "TrustServerCertificate=no;" \
                            "Connection Timeout=30;"

            conn = pyodbc.connect(db)
            return conn
        except IOError as e:
            print(e)
            conn = False
            return conn
    def get_patients_by_first_name(self, first_name):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE FirstName = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (first_name,))
            results = c.fetchall()
        return results

    def get_patients_by_last_name(self, last_name):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE LastName = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (last_name,))
            results = c.fetchall()
        return results

    def get_patients_by_date_of_birth(self, date_of_birth):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE DateOfBirth = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (date_of_birth,))
            results = c.fetchall()
        return results

    def get_patients_by_ssn(self, ssn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (ssn,))
            results = c.fetchall()
        return results

    def get_patients_by_mrn(self, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (mrn,))
            results = c.fetchall()
        return results

    def get_patients_by_first_last_name(self, first_name, last_name):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE FirstName = ? AND LastName = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (first_name, last_name))
            results = c.fetchall()
        return results

    def get_patients_by_first_name_and_dob(self, first_name, dob):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE FirstName = ? AND DateOfBirth = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (first_name, dob))
            results = c.fetchall()
        return results

    def get_patients_by_first_name_and_ssn(self, first_name, ssn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE FirstName = ? AND SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (first_name, ssn))
            results = c.fetchall()
        return results

    def get_patients_by_first_name_and_mrn(self, first_name, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ? AND FirstName = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (mrn, first_name))
            results = c.fetchall()
        return results

    def get_patients_by_last_name_and_dob(self, last_name, dob):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE LastName = ? AND DateOfBirth = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (last_name, dob))
            results = c.fetchall()
        return results

    def get_patients_by_last_name_and_ssn(self, last_name, ssn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE LastName = ? AND SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (last_name, ssn))
            results = c.fetchall()
        return results

    def get_patients_by_last_name_and_mrn(self, last_name, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ? AND LastName = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (mrn, last_name))
            results = c.fetchall()
        return results

    def get_patients_by_dob_and_ssn(self, date_of_birth, ssn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE DateOfBirth = ? AND SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (date_of_birth, ssn,))
            results = c.fetchall()
        return results

    def get_patients_by_dob_and_mrn(self, date_of_birth, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ? AND DateOfBirth = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (mrn, date_of_birth))
            results = c.fetchall()
        return results

    def get_patients_by_ssn_and_mrn(self, ssn, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ? AND SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (mrn, ssn))
            results = c.fetchall()
        return results

    def get_patients_by_name_dob(self, first_name, last_name, date_of_birth):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE FirstName = ? AND LastName = ? AND DateOfBirth = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (first_name, last_name, date_of_birth))
            results = c.fetchall()
        return results

    def get_patients_by_name_ssn(self, first_name, last_name, ssn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE FirstName = ? AND LastName = ? AND SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (first_name, last_name, ssn))
            results = c.fetchall()
        return results

    def get_patients_by_name_mrn(self, first_name, last_name, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ? AND FirstName = ? AND LastName = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (mrn, first_name, last_name))
            results = c.fetchall()
        return results

    def get_patients_by_fname_dob_ssn(self, first_name, date_of_birth, ssn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE FirstName = ? AND DateOfBirth = ? AND SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (first_name, date_of_birth, ssn))
            results = c.fetchall()
        return results

    def get_patients_by_name_dob_mrn(self, first_name, date_of_birth, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ? AND FirstName = ? AND DateOfBirth = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (mrn, first_name, date_of_birth))
            results = c.fetchall()
        return results

    def get_patients_by_name_ssn_mrn(self, first_name, ssn, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ? AND FirstName = ? AND SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (mrn, first_name, ssn))
            results = c.fetchall()
        return results

    def get_patients_by_name_dob_ssn(self, last_name, date_of_birth, ssn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE LastName = ? AND DateOfBirth = ? AND SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (last_name, date_of_birth, ssn))
            results = c.fetchall()
        return results

    def get_patients_by_last_name_dob_mrn(self, last_name, date_of_birth, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ? AND LastName = ? AND DateOfBirth = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (mrn, last_name, date_of_birth))
            results = c.fetchall()
        return results

    def get_patients_by_last_name_ssn_mrn(self, last_name, ssn, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ? AND LastName = ? AND SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (mrn, last_name, ssn))
            results = c.fetchall()
        return results

    def get_patients_by_dob_ssn_mrn(self, date_of_birth, ssn, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ? AND DateOfBirth = ? AND SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (mrn, date_of_birth, ssn))
            results = c.fetchall()
        return results

    def get_patients_by_full_name_dob_ssn(self, first_name, last_name, date_of_birth, ssn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE FirstName = ? AND LastName = ? AND DateOfBirth = ? AND SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (first_name, last_name, date_of_birth, ssn))
            results = c.fetchall()
        return results

    def get_patients_by_full_name_dob_mrn(self, first_name, last_name, date_of_birth, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ? AND FirstName = ? AND LastName = ? AND DateOfBirth = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (mrn, first_name, last_name, date_of_birth))
            results = c.fetchall()
        return results

    def get_patients_by_name_dob_ssn_mrn(self, last_name, date_of_birth, ssn, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ? AND LastName = ? AND DateOfBirth = ? AND SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (mrn, last_name, date_of_birth, ssn))
            results = c.fetchall()
        return results

    def get_patients_by_first_name_dob_ssn_mrn(self, first_name, date_of_birth, ssn, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ? AND FirstName = ? AND DateOfBirth = ? AND SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (mrn, first_name, date_of_birth, ssn))
            results = c.fetchall()
        return results

    def get_patients_by_full_name_dob_ssn_mrn(self, first_name, last_name, date_of_birth, ssn, mrn):
        conn = self.connect()
        query = "SELECT * FROM MRPatient WHERE MRN = ? AND FirstName = ? AND LastName = ? AND DateOfBirth = ? AND SSN = ?"
        with closing(conn.cursor()) as c:
            c.execute(query, (first_name, last_name, date_of_birth, ssn, mrn))
            results = c.fetchall()
        return results
