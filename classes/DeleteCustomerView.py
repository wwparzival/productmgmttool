# Standard classes / libraries
import sys
import pandas as pd
from PyQt5.QtCore import pyqtSignal, QPersistentModelIndex
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QMessageBox

# Custom classes / libraries
from classes.Table import *
from classes.helper import replace_nan

class DeleteCustomerView(QWidget):
    """ A class used to represent the "Delete Customers" window.

    Methods
    -------
    raise_main()
        Displays the main menu window.
    delete_row(index=QPersistentModelIndex)
        Deletes the customer from the Table widget and from the database.
    logout()
        Logs the user out of the application, to return to the LoginView.
    """

    switch_main = pyqtSignal()
    switch_logout = pyqtSignal()

    def __init__(self, cb_delete_customer, customer_data: pd.DataFrame) -> None:
        """ Initiats the Delete customer view.

        Parameters
        ----------
        cb_delete_customer : function
            The callback function of the Controller class.
        customer_data : pandas.Dataframe
            Contains all the customer datasets.

        Return
        ----------
        none
        """

        QWidget.__init__(self)
        
        self.setWindowTitle("Einen Kunden löschen")
        self.resize(910, 400)
        self.cb_del_customer = cb_delete_customer

        layout = QGridLayout()

        df_customer_data = customer_data
        # Add a new column to the dataframe
        df_customer_data["button"] = ""

        # QTableWidget data
        data = {
            "Kundenname" : df_customer_data["name"].map(str).to_list(),
            "Kundennummer" : df_customer_data["number"].map(str).to_list(),
            "CUCM - Version" : replace_nan(df_customer_data["cucm"].map(str).to_list()),
            "IMP - Version" : replace_nan(df_customer_data["imp"].map(str).to_list()),
            "CUC - Version" : replace_nan(df_customer_data["cuc"].map(str).to_list()),
            "EXP - Version" : replace_nan(df_customer_data["exp"].map(str).to_list()),
            "Vertragsende" : df_customer_data["contract-expire"].map(str).to_list(),
            "Button" : df_customer_data["button"].to_list()
        }

        # Create a new table widget
        self.tab_customers = Table(data, df_customer_data.shape[0], df_customer_data.shape[1]-1)

        # Adds "Delete buttons" in the cell of the last column / in every row
        for row in range(df_customer_data.shape[0]):
            btn_del = QPushButton("Löschen")
            index = QPersistentModelIndex(self.tab_customers.model().index(row, df_customer_data.shape[1]-2))
            btn_del.clicked.connect(lambda *args, index=index: self.delete_row(index))
            self.tab_customers.setCellWidget(row, df_customer_data.shape[1]-2, btn_del)

        self.tab_customers.resizeColumnsToContents()
        self.tab_customers.resizeRowsToContents()
        layout.addWidget(self.tab_customers)

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

    def delete_row(self, index: QPersistentModelIndex) -> None:
        """ Deletes the row from the Table widget and writes the table content to the database.
        
        Parameters
        ----------
        index : PyQt5.QtCore.QPersistentModelIndex
            The row index of the delete button in the cell of the Table widget.
        
        Return
        ----------
        none
        """

        if index.isValid():
            # Gets all the customer details from the row, where the Delete button was clicked.
            row_data = []
            for i in range(0, self.tab_customers.columnCount()-1):
                row_data.append(self.tab_customers.item(index.row(), i).text())

            # Runs and displays the MessageBox, as long as the user acknowledges the popup window
            ack = False
            while not ack:
                choice = QMessageBox.question(
                    None,
                    " ",
                    "Den Kunden wirklich löschen?",
                    QMessageBox.Ok,
                    QMessageBox.Cancel
                )
                if choice == QMessageBox.Ok:
                    ack = True
                    result = self.cb_del_customer(row_data)
                    if result == True:
                        self.tab_customers.removeRow(index.row())
                if choice == QMessageBox.Cancel:
                    ack = True

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