# Standard classes / libraries
from PyQt5.QtWidgets import QWidget, QGridLayout

# Custom classes / libraries
from classes.Table import *
from classes.CustomerSecurityView import *

class SecurityIssuesView(QWidget):
    """
    A mockup to show a possible implementation of the security issue overview.

    Methods
    -------
    itemclicked()
        Displays a filtered table based on the clicked customer name.
    """

    def __init__(self) -> None:
        """ Initiats the Add customer view.

        Parameters
        ----------
        None
        
        Return
        ----------
        none
        """

        QWidget.__init__(self)

        self.setWindowTitle("Known Security Issues")
        self.resize(850, 400)
        self.move(0, 100)
        
        layout = QGridLayout()

        # QTableWidget data
        data = {
            "Kundenname" : ["Max Mustermann GmbH", "Max Mustermann GmbH", "Test AG", "Software-Devs GmbH"],
            "Betroffenes Produkt" : ["CUCM", "IMP", "CUCM", "Expressway"],
            "Produktversion" : ["12.5.1.17900-64", "12.5.1.15900-66", "14.0.1.10000-20", "X12.7.0"],
            "Behobene Version" : ["12.5.1.18901-1", "12.5.1.18900-6", "14.0.1.13900-155", "X14.3.1"]
        }

        # Create a new table widget
        tab_customers = Table(data, 4, 4)
        tab_customers.itemClicked.connect(self.itemclicked)
        layout.addWidget(tab_customers)

        # Arrange the layout of the widgets
        self.setLayout(layout)
    
    def itemclicked(self, item: QWidget) -> None:
        """ Initiats the Add customer view.

        Parameters
        ----------
        item : QWidget
            The item of the clicked table cell.
        
        Return
        ----------
        none
        """

        self.test = CustomerSecurityView(item.text())
        self.test.show()