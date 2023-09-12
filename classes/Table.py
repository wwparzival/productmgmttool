# Standard classes / libraries
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QColor
from datetime import datetime

class Table(QTableWidget):
    """
    A class used to provide QTableWidget objects with predefined table content.

    Methods
    -------
    set_data()
        Sets the values of the table cells.
    """

    def __init__(self, data: dict, *args) -> None:
        """ Initiats the Add customer view.

        Parameters
        ----------
        data : dict
            The customer datasets.

        Return
        ----------
        none
        """

        QTableWidget.__init__(self, *args)

        self.data = data
        self.set_data()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
 
    def set_data(self) -> None:
        """ Sets the values of the table cells.

        Parameters
        ----------
        none
        
        Return
        ----------
        none
        """

        table_headers = []
        
        expire_dates = self.data["Vertragsende"]
        
        for col_nr, key in enumerate(self.data.keys()):
            # Adds each key of the dict
            table_headers.append(key)
            for row_nr, content in enumerate(self.data[key]):
                newitem = QTableWidgetItem(content)
                self.setItem(row_nr, col_nr, newitem)
        
        # Mark the customer name cells with a color, corresponding to the contract expiry date
        for idx, expire_date in enumerate(expire_dates):
            # "Red" if contract is expired
            if (datetime.strptime(expire_date, "%d/%m/%Y") - datetime.now()).days <= 0:
                self.item(idx, 0).setBackground(QColor("#ff6961"))
            # "Yellow" if the contract expires in the next year
            elif (datetime.strptime(expire_date, "%d/%m/%Y") - datetime.now()).days <= 365:
                self.item(idx, 0).setBackground(QColor("#fdfd96"))
            # "Green" if contract runs longer than a year
            else:
                self.item(idx, 0).setBackground(QColor("#77dd77"))

        # Adds the headers to the table
        self.setHorizontalHeaderLabels(table_headers)