# Standard classes / libraries
import sys
import pandas as pd
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QMessageBox

# Custom classes / libraries
from classes.Table import *
from classes.helper import replace_nan

class ShowCustomersView(QWidget):
    """
    A class used to represent the Show Customers View.

    Methods
    -------
    raise_main()
        Switches back to the main menu.
    logout()
        Logs the user out of the application, to return to the LoginView.
    """

    switch_main = pyqtSignal()
    switch_logout = pyqtSignal()

    def __init__(self, customer_data: pd.DataFrame) -> None:
        """ Initiats the Add customer view.

        Parameters
        ----------
        customer_data : pandas.DataFrame
            Contains all the customer datasets.
        
        Return
        ----------
        none
        """

        QWidget.__init__(self)

        self.setWindowTitle("Show All Customers")
        self.resize(850, 400)

        layout = QGridLayout()
        
        df_customer_data = customer_data

        # QTableWidget data
        data = {
            "Kundenname" : df_customer_data["name"].map(str).to_list(),
            "Kundennummer" : df_customer_data["number"].map(str).to_list(),
            "CUCM - Version" : replace_nan(df_customer_data["cucm"].map(str).to_list()),
            "IMP - Version" : replace_nan(df_customer_data["imp"].map(str).to_list()),
            "CUC - Version" : replace_nan(df_customer_data["cuc"].map(str).to_list()),
            "EXP - Version" : replace_nan(df_customer_data["exp"].map(str).to_list()),
            "Vertragsende" : df_customer_data["contract-expire"].map(str).to_list()
        }

        # Create a new table widget
        tab_customers = Table(data, df_customer_data.shape[0], df_customer_data.shape[1]-1)
        layout.addWidget(tab_customers)

        # Button to navigate back to the MainView
        btn_main = QPushButton("Zurück")
        btn_main.clicked.connect(self.raise_main)
        layout.addWidget(btn_main)

        # Button to close the application
        btn_logout = QPushButton("Logout")
        btn_logout.clicked.connect(self.logout)
        layout.addWidget(btn_logout)

        # Button to close the application
        btn_quit = QPushButton("Beenden")
        btn_quit.clicked.connect(sys.exit)
        layout.addWidget(btn_quit)

        # Arrange the layout of the widgets
        self.setLayout(layout)

    def raise_main(self) -> None:
        """ Switches back to the main menu.
        
        Parameters
        ----------
        none

        Return
        ----------
        none
        """

        self.switch_main.emit()

    def logout(self) -> None:
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