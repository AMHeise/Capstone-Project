from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QComboBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap

from Forms import HomePage


class ChooseLocation(QMainWindow):

    def __init__(self, current_user):
        super().__init__()
        self.loader = QUiLoader()

        self.current_user = current_user

        # Initialize Form
        self.choose_location_window = self.loader.load("Forms/chooseLocationWindow.ui")

        # Initialize Sub-Forms
        self.homepage = HomePage.HomePage

        # Initialize Buttons
        self.select_location_button = self.choose_location_window.findChild(QPushButton, "select_location_pushButton")
        self.select_location_button.clicked.connect(self.on_select_location_button_clicked)

        # Set image
        choose_office_location_image_label = self.choose_location_window.findChild(QLabel, "label")
        pixmap = QPixmap("Images/office.png")
        choose_office_location_image_label.setPixmap(pixmap)

        # Initialize Text Fields
        self.welcome_message_label = self.choose_location_window.findChild(QLabel, "label_2")
        self.office_location_comboBox = self.choose_location_window.findChild(QComboBox, "office_location_comboBox")

    def initialize_choose_location_window(self):
        self.choose_location_window.show()

    # Button On-Click
    def on_select_location_button_clicked(self):
        self.selected_location = self.get_selected_location()
        self.homepage = self.homepage(self.current_user, self.selected_location)
        self.homepage.initialize_homepage()
        self.choose_location_window.close()

    def get_selected_location(self):
        selectedIndex = self.office_location_comboBox.currentIndex()
        location_option = location_options.get(selectedIndex)
        return location_option

location_options = {0: "Kernersville", 1: "Winston-Salem", 2: "Mount Airy"}
