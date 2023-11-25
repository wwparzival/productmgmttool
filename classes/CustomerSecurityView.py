# Standard classes / libraries
from PyQt5.QtWidgets import QWidget, QGridLayout

# Custom classes / libraries
from classes.Table import *

class CustomerSecurityView(QWidget):
    """
    A mockup to show a possible implementation of the security issue overview filted by the customer name.

    Methods
    -------
    None
    """

    def __init__(self, customername: str) -> None:
        """ Initiats the Add customer view.

        Parameters
        ----------
        customername : str
            The customer name to filter the resulting table.
        
        Return
        ----------
        none
        """

        QWidget.__init__(self)

        self.setWindowTitle("Known Security Issues")
        self.resize(850, 400)
        self.move(0, 300)

        layout = QGridLayout()

        # QTableWidget data
        if customername == "Max Mustermann GmbH":
            data = {
                "Kundenname" : ["Max Mustermann GmbH", "Max Mustermann GmbH"],
                "Betroffenes Produkt" : ["CUCM", "IMP"],
                "Produktversion" : ["12.5.1.17900-64", "12.5.1.15900-66"],
                "Behobene Version" : ["12.5.1.18901-1", "12.5.1.18900-6"]
            }
            rows = 2
        elif customername == "Test AG":
            data = {
                "Kundenname" : ["Test AG"],
                "Betroffenes Produkt" : ["CUCM"],
                "Produktversion" : ["14.0.1.10000-20"],
                "Behobene Version" : ["14.0.1.13900-155"]
            }
            rows = 1
        elif customername == "Software-Devs GmbH":
            data = {
                "Kundenname" : ["Software-Devs GmbH"],
                "Betroffenes Produkt" : ["Expressway"],
                "Produktversion" : ["X12.7.0"],
                "Behobene Version" : ["X14.3.1"]
            }
            rows = 1

        # Create a new table widget
        tab_customers = Table(data, rows, 4)
        layout.addWidget(tab_customers)

        # Arrange the layout of the widgets
        self.setLayout(layout)