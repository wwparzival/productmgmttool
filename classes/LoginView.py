# Standard classes / libraries
import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton

class LoginView(QWidget):
    """
    A class used to represent the Login View.

    Methods
    -------
    validate_login()
        Calls the callback function to validate the login.
    """

    def __init__(self, cb_validate_login) -> None:
        """ Initiats the Add customer view.

        Parameters
        ----------
        cb_validate_login : function
            The callback function of the Controller class.
        """

        self.cb_validate_login = cb_validate_login
        
        QWidget.__init__(self)
        self.setWindowTitle("Login")
        layout = QGridLayout()

        # Label Widget for usernname
        lbl_user = QLabel("Bitte Username eingeben:")
        layout.addWidget(lbl_user)

        # Entry Widget for usernname
        self.ent_user = QLineEdit(self)
        layout.addWidget(self.ent_user) 

        # Label Widget for password
        lbl_pwd = QLabel("Bitte Password eingeben:")
        layout.addWidget(lbl_pwd)

        # Entry Widget for password
        self.ent_pwd = QLineEdit(self)
        self.ent_pwd.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.ent_pwd) 

        # Button to login
        btn_login = QPushButton("Login")
        btn_login.clicked.connect(self.validate_login)
        layout.addWidget(btn_login)

        # Button to close the application
        btn_quit = QPushButton("Beenden")
        btn_quit.clicked.connect(sys.exit)
        layout.addWidget(btn_quit)

        # Arrange the layout of the widgets
        self.setLayout(layout)

    def validate_login(self) -> None:
        """ Calls the callback function of the Controller, when the Login button is clicked.
        
        Parameters
        ----------
        None

        Return
        ----------
        None
        """

        self.cb_validate_login(self.ent_user.text(), self.ent_pwd.text())