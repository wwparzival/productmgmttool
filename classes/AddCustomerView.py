# Standard classes / libraries
import pandas as pd
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import pyqtSignal, QRegExp
from PyQt5.QtGui import QRegExpValidator

class AddCustomerView(QWidget):
    """
    A class used to represent the Add Customer View.

    Methods
    -------
    raise_main()
        Switches back to the main menu.
    add_new_customer()
        Takes the values of the input widgets and calls the callback function to save the new customer.
    """

    switch_main = pyqtSignal()
    regex_name = QRegExp("^.{1,30}$")
    regex_number = QRegExp("^[0-9]{1,5}$")
    regex_uc_version = QRegExp("^[0-9]{2}\.[0-9]\.[0-9]\.[0-9]{5}\-[0-9]{2}$")
    regex_exp_version = QRegExp("^X[0-9]{1,2}\.[0-9]\.[0-9]{1,2}$")
    regex_contract_expiry = QRegExp("^[0-3]?[0-9]\/[0-3]?[0-9]\/20[2-9][3-9]$")

    def __init__(self, cb_add_customer) -> None:
        """ Initiats the Add customer view.

        Parameters
        ----------
        cb_add_customer : function
            The callback function of the Controller class.
        
        Return
        ----------
        none
        """

        QWidget.__init__(self)

        self.setWindowTitle("Add a customer")
        self.cb_add_customer = cb_add_customer

        layout = QGridLayout()

        # Label Widget for customer name
        lbl_name = QLabel("Kundenname")
        layout.addWidget(lbl_name)

        # Entry Widget for customer name
        self.ent_name = QLineEdit(self)
        self.ent_name.setPlaceholderText("Maximal 30 Zeichen")
        self.ent_name.setValidator(QRegExpValidator(self.regex_name))
        layout.addWidget(self.ent_name) 

        # Label Widget for customer number
        lbl_number = QLabel("Kundennummer")
        layout.addWidget(lbl_number)

        # Entry Widget for customer number
        self.ent_number = QLineEdit(self)
        self.ent_number.setPlaceholderText("1 - 99999")
        self.ent_number.setValidator(QRegExpValidator(self.regex_number))
        layout.addWidget(self.ent_number) 

        # Label Widget for cucm version
        lbl_cucm = QLabel("CUCM - Version")
        layout.addWidget(lbl_cucm)

        # Entry Widget for cucm version
        self.ent_cucm = QLineEdit(self)
        self.ent_cucm.setPlaceholderText("Bsp.: 12.5.1.17900-22")
        self.ent_cucm.setValidator(QRegExpValidator(self.regex_uc_version))
        layout.addWidget(self.ent_cucm)

        # Label Widget for imp version
        lbl_imp = QLabel("IMP - Version")
        layout.addWidget(lbl_imp)

        # Entry Widget for imp version
        self.ent_imp = QLineEdit(self)
        self.ent_imp.setPlaceholderText("Bsp.: 12.5.1.17900-22")
        self.ent_imp.setValidator(QRegExpValidator(self.regex_uc_version))
        layout.addWidget(self.ent_imp)

        # Label Widget for cuc version
        lbl_cuc = QLabel("CUC - Version")
        layout.addWidget(lbl_cuc)

        # Entry Widget for cuc version
        self.ent_cuc = QLineEdit(self)
        self.ent_cuc.setPlaceholderText("Bsp.: 12.5.1.17900-22")
        self.ent_cuc.setValidator(QRegExpValidator(self.regex_uc_version))
        layout.addWidget(self.ent_cuc)

        # Label Widget for expressway version
        lbl_exp = QLabel("EXP - Version")
        layout.addWidget(lbl_exp)

        # Entry Widget for exp version
        self.ent_exp = QLineEdit(self)
        self.ent_exp.setPlaceholderText("Bsp.: X14.0.2")
        self.ent_exp.setValidator(QRegExpValidator(self.regex_exp_version))
        layout.addWidget(self.ent_exp)

        # Label Widget for contract expiry date
        lbl_contract = QLabel("Datum Vertragsende")
        layout.addWidget(lbl_contract)

        # Entry Widget for contract expiry date
        self.ent_contract = QLineEdit(self)
        self.ent_contract.setPlaceholderText("Bsp.: 1/10/2025")
        self.ent_contract.setValidator(QRegExpValidator(self.regex_contract_expiry))
        layout.addWidget(self.ent_contract)

        # Button to save the new customer
        btn_add = QPushButton("Kunden anlegen", self)
        btn_add.clicked.connect(self.add_new_customer)
        layout.addWidget(btn_add)

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

    def add_new_customer(self) -> None:
        """ Takes the values of the input widgets and calls the callback function to save the new customer.
        
        Parameters
        ----------
        none

        Return
        ----------
        none
        """

        # Store the input value in a dict
        data = {
            "id" : [0],
            "name" : [self.ent_name.text()],
            "number" : [self.ent_number.text()],
            "cucm" : [self.ent_cucm.text()],
            "imp" : [self.ent_imp.text()],
            "cuc" : [self.ent_cuc.text()],
            "exp" : [self.ent_exp.text()],
            "contract-expire" : [self.ent_contract.text()]
        }

        # Call the callback function of the Controller class
        self.cb_add_customer(pd.DataFrame(data=data))

        # Clearing the input fields after the new customer was tried to be saved
        self.ent_name.setText("")
        self.ent_number.setText("")
        self.ent_cucm.setText("")
        self.ent_imp.setText("")
        self.ent_cuc.setText("")
        self.ent_exp.setText("")
        self.ent_contract.setText("")