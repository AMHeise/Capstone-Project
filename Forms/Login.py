from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap

from Forms import ChooseLocationWindow
from Classes import UserLogin


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.loader = QUiLoader()

        # Initialize Form
        self.login = self.loader.load("Forms/login.ui")

        # Initialize Sub-Forms
        self.choose_location_window = ChooseLocationWindow.ChooseLocation

        # Initialize Buttons
        self.login_button = self.login.findChild(QPushButton, "login_pushButton")
        self.login_button.clicked.connect(self.on_login_button_clicked)

        # Set image
        logo_image_label = self.login.findChild(QLabel, "logo_image_label")
        pixmap = QPixmap("Images/steth.png")
        logo_image_label.setPixmap(pixmap)

        # Initialize Text Fields
        self.username_lineEdit = self.login.findChild(QLineEdit, "username_lineEdit")
        self.Password_lineEdit = self.login.findChild(QLineEdit, "Password_lineEdit")

    def initialize_login(self):
        self.login.show()

    def on_login_button_clicked(self):
        username = self.username_lineEdit.text()
        password = self.Password_lineEdit.text()
        # self.verify_user_credentials(username, password)
        if username in self.users and self.users[username] == password:
            # If the entered username exists in the users dictionary and its associated
            # password matches the one entered by the user, allow access
            current_user = UserLogin.UserLogin(username)
            current_user_str = current_user.get_username()
            self.choose_location_window = self.choose_location_window(current_user_str)
            self.choose_location_window.initialize_choose_location_window()
            self.login.close()
        else:
            # If the entered username or password is incorrect, show an error message
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, Invalid Login Credentials.")
            # show the message box
            msg_box.exec_()

    # Use Below Method if there is a database connection
    """
    def verify_user_credentials(self, username, password):
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        # Execute query to retrieve user information
        cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
        user = cursor.fetchone()

        if user:
            # If the query returned a user, allow access
            self.choose_location_window = self.choose_location_window()
            self.choose_location_window.initialize_choose_location_window()
            self.login.close()
        else:
            # If the query did not return a user, show an error message
            # create a QMessageBox object
            msg_box = QMessageBox()
            # set the message box icon, title, and message text
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error, Invalid Login Credentials.")
            # show the message box
            msg_box.exec_()
        cursor.close()
        conn.close()
    """

    users = {
        "Ally": "1234",
        "Anna": "1234",
        "Drew": "1234",
        "Kameron": "1234",
        "Roberto": "1234"
    }
