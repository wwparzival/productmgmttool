# Standard classes / libraries
import pandas as pd
from PyQt5.QtCore import pyqtSignal, QPersistentModelIndex
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QMessageBox

# Custom classes / libraries
from classes.Table import *
from classes.helper import replace_nan

class UpdateCustomerView(QWidget):
    """
    A class used to represent the Update Customer View.

    Methods
    -------
    raise_main()
        Switches back to the main menu.
    update_row()
        Stores the updated customers table in the database.
    """

    switch_main = pyqtSignal()

    def __init__(self, cb_update_customer, customer_data: pd.DataFrame) -> None:
        """ Initiats the Update customer view.

        Parameters
        ----------
        cb_update_customer : function
            The callback function of the Controller class.
        customer_data : pandas.Dataframe
            Contains all the customer datasets.

        Return
        ----------
        none
        """

        QWidget.__init__(self)

        self.setWindowTitle("Einen Kunden bearbeiten")
        self.resize(820, 400)
        self.cb_update_customer = cb_update_customer

        layout = QGridLayout()

        self.df_customer_data = customer_data

        # QTableWidget data
        data = {
            "Kundenname" : self.df_customer_data["name"].map(str).to_list(),
            "Kundennummer" : self.df_customer_data["number"].map(str).to_list(),
            "CUCM - Version" : replace_nan(self.df_customer_data["cucm"].map(str).to_list()),
            "IMP - Version" : replace_nan(self.df_customer_data["imp"].map(str).to_list()),
            "CUC - Version" : replace_nan(self.df_customer_data["cuc"].map(str).to_list()),
            "EXP - Version" : replace_nan(self.df_customer_data["exp"].map(str).to_list()),
            "Laufzeit" : self.df_customer_data["contract-expire"].map(str).to_list()
        }

        # Create a new table widget
        self.tab_customers = Table(data, self.df_customer_data.shape[0], self.df_customer_data.shape[1]-1)
        self.tab_customers.resizeColumnsToContents()
        self.tab_customers.resizeRowsToContents()
        layout.addWidget(self.tab_customers)

        # Button to save the updated Table contents to the database.
        btn_update = QPushButton("Änderungen speichern")
        btn_update.clicked.connect(self.update_row)
        layout.addWidget(btn_update)
        
        # Button to navigate back to the MainView
        btn_main = QPushButton("Zurück")
        btn_main.clicked.connect(self.raise_main)
        layout.addWidget(btn_main)

        # Button to close the application
        btn_quit = QPushButton("Beenden")
        btn_quit.clicked.connect(self.close)
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

    def update_row(self) -> None:
        """ Stores the updated customers table in the database.

        Parameters
        ----------
        None

        Return
        ----------
        None
        """

        # Gets all the values from the Table widgets cells and updates the dataframe.
        for row_nr in range(0, self.tab_customers.rowCount()):
            for col_nr in range(0, self.tab_customers.columnCount()):
                self.df_customer_data.at[row_nr, list(self.df_customer_data.columns.values)[col_nr+1]] = self.tab_customers.item(row_nr, col_nr).text()

        # Runs and displays the MessageBox, as long as the user acknowledges the popup window
        ack = False
        while not ack:
            choice = QMessageBox.question(
                None,
                " ",
                "Die geänderten Daten speichern?",
                QMessageBox.Ok,
                QMessageBox.Cancel
            )
            if choice == QMessageBox.Ok:
                ack = True
                self.cb_update_customer(self.df_customer_data)
            if choice == QMessageBox.Cancel:
                break