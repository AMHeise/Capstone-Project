from PySide6.QtWidgets import QApplication

from Forms import Login

if __name__ == "__main__":
    app = QApplication([])
    login_page = Login.Login()
    login_page.initialize_login()
    app.exec()
