from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap

from Forms import Login, NewPatientWindow, PatientLookup, ChooseLocationWindow


class HomePage(QMainWindow):

    def __init__(self, current_user, selected_location):
        super().__init__()
        self.loader = QUiLoader()

        self.current_user = current_user
        self.selected_location = selected_location

        # Initialize Super-Form
        self.choose_location_window = ChooseLocationWindow.ChooseLocation

        # Initialize Form
        self.homepage = self.loader.load("Forms/homePage.ui")

        # Initialize Sub-Forms
        self.patient_lookup = PatientLookup.PatientLookup
        self.new_patient_window = NewPatientWindow.NewPatient
        self.login = Login.Login

        # Initialize Buttons
        self.logout_button = self.homepage.findChild(QPushButton, "logout_pushButton")
        self.logout_button.clicked.connect(self.on_logout_button_clicked)
        self.patient_lookup_button = self.homepage.findChild(QPushButton, "search_for_patient_pushButton")
        self.patient_lookup_button.clicked.connect(self.on_patient_lookup_button_clicked)
        self.choose_location_button = self.homepage.findChild(QPushButton, "choose_office_location_pushButton")
        self.choose_location_button.clicked.connect(self.on_choose_location_button_clicked)
        self.new_patient_button = self.homepage.findChild(QPushButton, "add_new_patient_pushButton")
        self.new_patient_button.clicked.connect(self.on_new_patient_button_clicked)

        # Set images
        search_for_patient_image_label = self.homepage.findChild(QLabel, "search_for_patient_image_label")
        pixmap = QPixmap("Images/magnifying-glass.png")
        search_for_patient_image_label.setPixmap(pixmap)
        choose_office_location_image_label = self.homepage.findChild(QLabel, "choose_office_location_image_label")
        pixmap2 = QPixmap("Images/office.png")
        choose_office_location_image_label.setPixmap(pixmap2)
        add_new_patient_image_label = self.homepage.findChild(QLabel, "add_new_patient_image_label")
        pixmap3 = QPixmap("Images/plus-symbol.png")
        add_new_patient_image_label.setPixmap(pixmap3)
        logout_image_label = self.homepage.findChild(QLabel, "logout_image_label")
        pixmap4 = QPixmap("Images/logout.png")
        logout_image_label.setPixmap(pixmap4)

    def initialize_homepage(self):
        self.homepage.show()

    # Button On-Click
    def on_logout_button_clicked(self):
        self.login = self.login()
        self.login.initialize_login()
        self.homepage.close()

    def on_patient_lookup_button_clicked(self):
        self.patient_lookup = self.patient_lookup(self.current_user, self.selected_location)
        self.patient_lookup.initialize_patient_lookup()
        self.homepage.close()

    def on_choose_location_button_clicked(self):
        self.choose_location_window = self.choose_location_window(self.current_user)
        self.choose_location_window.initialize_choose_location_window()
        self.homepage.close()

    def on_new_patient_button_clicked(self):
        self.new_patient_window = self.new_patient_window(self.current_user, self.selected_location)
        self.new_patient_window.initialize_new_patient_window()
        self.homepage.close()
