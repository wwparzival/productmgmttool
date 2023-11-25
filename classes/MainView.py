# Standard classes / libraries
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QMessageBox

class MainView(QWidget):
    """ A class used to represent the Main View.

    Methods
    -------
    raise_show_customers()
        Displays the "Show all customers" window. 
    raise_add_customer()
        Displays the "Add a customer" window.
    raise_update_customer()
        Displays the "Update a customer" window.
    raise_delete_customer()
        Displays the "Delete customers" window.
    logout()
        Logs the user out of the application, to return to the LoginView.
    """

    switch_show_customers = pyqtSignal()
    switch_add_customer = pyqtSignal()
    switch_update_customer = pyqtSignal()
    switch_delete_customer = pyqtSignal()
    switch_logout = pyqtSignal()

    def __init__(self, privilege):
        """

        Parameters
        ----------
        none

        Return
        ----------
        none
        """

        QWidget.__init__(self)

        self.setWindowTitle("Kundendatenbank")
        self.resize(400, 200)
        layout = QGridLayout()

        # Button to show the show customers view
        btn_show_customers = QPushButton("Alle Kunden anzeigen")
        btn_show_customers.clicked.connect(self.raise_show_customers)
        layout.addWidget(btn_show_customers)

        # Only shows this view elements, if the logged in user has the "write" privileges
        if privilege == "w":
            # Button to show the add customer view
            btn_add_customer = QPushButton("Einen Kunden anlegen")
            btn_add_customer.clicked.connect(self.raise_add_customer)
            layout.addWidget(btn_add_customer)

            # Button to show the update customers view
            btn_update_customer = QPushButton("Kunden bearbeiten")
            btn_update_customer.clicked.connect(self.raise_update_customer)
            layout.addWidget(btn_update_customer)

            # Button to show the delete customers view
            btn_delete_customer = QPushButton("Kunden löschen")
            btn_delete_customer.clicked.connect(self.raise_delete_customer)
            layout.addWidget(btn_delete_customer)

        # Button to logout
        btn_logout = QPushButton("Logout")
        btn_logout.clicked.connect(self.logout)
        layout.addWidget(btn_logout)

        # Button to close the application
        btn_quit = QPushButton("Beenden")
        btn_quit.clicked.connect(sys.exit)
        layout.addWidget(btn_quit)

        # Arrange the layout of the widgets
        self.setLayout(layout)

    def raise_show_customers(self):
        """ Displays the show customers menu window.

        Parameters
        ----------
        none

        Return
        ----------
        none
        """

        self.switch_show_customers.emit()

    def raise_add_customer(self):
        """ Displays the add customer menu window.

        Parameters
        ----------
        none

        Return
        ----------
        none
        """
        
        self.switch_add_customer.emit()

    def raise_update_customer(self):
        """ Displays the update customers menu window.

        Parameters
        ----------
        none

        Return
        ----------
        none
        """
        
        self.switch_update_customer.emit()

    def raise_delete_customer(self):
        """ Displays the delete customers menu window.

        Parameters
        ----------
        none

        Return
        ----------
        none
        """
        
        self.switch_delete_customer.emit()

    def logout(self):
        """ Logs the user out of the application, to return to the LoginView.

        Parameters
        ----------
        none

        Return
        ----------
        none
        """
        
        # Runs and displays the MessageBox, as long as the user acknowledges the popup window
        ack = False
        while not ack:
            choice = QMessageBox.question(
                None,
                " ",
                "Bitte den Logout bestätigen.",
                QMessageBox.Ok,
                QMessageBox.Cancel
            )
            if choice == QMessageBox.Ok:
                ack = True
                self.switch_logout.emit()
            if choice == QMessageBox.Cancel:
                ack = True