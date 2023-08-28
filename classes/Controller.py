# Standard classes / libraries
import pandas as pd
from hashlib import sha256
from PyQt5.QtWidgets import QMessageBox

# Custom classes / libraries
from classes.CsvFileAccess import *
from classes.LoginView import *
from classes.MainView import *
from classes.ShowCustomersView import *
from classes.AddCustomerView import *
from classes.UpdateCustomerView import *
from classes.DeleteCustomerView import *
from classes.helper import get_row_index

class Controller:
    """ A class used to represent Controller in an MVC architecture.

    Methods
    -------
    raise_main_view()
        Displays the main menu window.
    raise_customers_view()
        Displays the "Show all customers" window. 
    raise_add_customer_view()
        Displays the "Add a customer" window.
    raise_update_customer_view()
        Displays the "Update a customer" window.
    raise_delete_customer_view()
        Displays the "Delete customers" window.
    add_new_customer(data=pandas.DataFrame)
        Stores the new customer and it's information in the database.
    update_customer(updated_customers=pandas.DataFrame)
        Stores the updated customers table in the database.
    delete_customer(row_data=list)
        Deletes a customer from the database.
    """

    show_customers_view = 0
    add_customer_view = 0
    update_customer_view = 0
    delete_customer_view = 0

    def __init__(self) -> None:
        """
        Parameters
        ----------
        None
        """

        self.db_access = CsvFileAccess()
        self.login_view = LoginView(self.validate_login)
        self.login_view.show()

    def raise_main_view(self) -> None:
        """ Displays the main menu window.

        Parameters
        ----------
        none

        Return
        ----------
        none
        """

        self.main_view = MainView(self.user_priv)
        self.main_view.switch_show_customers.connect(self.raise_customers_view)
        self.main_view.switch_add_customer.connect(self.raise_add_customer_view)
        self.main_view.switch_update_customer.connect(self.raise_update_customer_view)
        self.main_view.switch_delete_customer.connect(self.raise_delete_customer_view)
        if self.login_view != 0:
            self.login_view.close()
        if self.show_customers_view != 0:
            self.show_customers_view.close()
        if self.add_customer_view != 0:
            self.add_customer_view.close()
        if self.update_customer_view != 0:
            self.update_customer_view.close()
        if self.delete_customer_view != 0:
            self.delete_customer_view.close()
        self.main_view.show()

    def raise_customers_view(self) -> None:
        """ Displays the "Show all customers" window.

        Parameters
        ----------
        none

        Return
        ----------
        none
        """

        self.show_customers_view = ShowCustomersView(self.db_access.read_all("data/dataset.csv"))
        self.show_customers_view.switch_main.connect(self.raise_main_view)
        self.main_view.close()
        self.show_customers_view.show()

    def raise_add_customer_view(self) -> None:
        """ Displays the "Add a customer" window.

        Parameters
        ----------
        none

        Return
        ----------
        none
        """

        self.add_customer_view = AddCustomerView(self.add_new_customer)
        self.add_customer_view.switch_main.connect(self.raise_main_view)
        self.main_view.close()
        self.add_customer_view.show()

    def raise_update_customer_view(self) -> None:
        """ Displays the "Update a customer" window.

        Parameters
        ----------
        none

        Return
        ----------
        none
        """

        self.update_customer_view = UpdateCustomerView(self.update_customer, self.db_access.read_all("data/dataset.csv"))
        self.update_customer_view.switch_main.connect(self.raise_main_view)
        self.main_view.close()
        self.update_customer_view.show()

    def raise_delete_customer_view(self) -> None:
        """ Displays the "Delete customers" window.

        Parameters
        ----------
        none

        Return
        ----------
        none
        """

        self.delete_customer_view = DeleteCustomerView(self.delete_customer, self.db_access.read_all("data/dataset.csv"))
        self.delete_customer_view.switch_main.connect(self.raise_main_view)
        self.main_view.close()
        self.delete_customer_view.show()

    def validate_login(self, username: str, password: str) -> None:
        """ Validates the login, when the "Login" button in the Login window is clicked.
        After successfull login, the Main window is raised.

        Parameters
        ----------
        username : str
            Contains the login username.
        password : str
            Contains the login password.

        Return
        ----------
        none
        """

        df_users = self.db_access.read_all("data/users.csv")
        # Get the row index of the user in the dataframe
        row_index = get_row_index(df_users["username"].map(str).to_list(), username)

        # Check if user exists and the passwords match for the given user
        if (
                username in df_users["username"].values and
                sha256(bytes(password, "utf-8")).hexdigest() == df_users["password"][row_index]
            ):
            self.user_priv = df_users["privilege"][row_index]
            self.raise_main_view()
        else:
            # Runs and displays the MessageBox, as long as the user acknowledges the popup window
            ack = False
            while not ack:
                choice = QMessageBox.critical(
                    None,
                    " ",
                    "Username oder Passwort falsch!",
                    QMessageBox.Ok
                )

                if choice:
                    ack = True

    def add_new_customer(self, data: pd.DataFrame) -> None:
        """ Stores the new customer and it's information in the database.

        Parameters
        ----------
        data : pandas.DataFrame
            Contains the information of the new customer.

        Return
        ----------
        none
        """

        current_customers = self.db_access.read_all("data/dataset.csv")
        
        new_customer_name = str(data["name"][0])
        new_customer_number = str(data["number"][0])
        
        # Check, if the new customer name is already used by any existing customer
        if new_customer_name in current_customers["name"].map(str).to_list():
            # Runs and displays the MessageBox, as long as the user acknowledges the popup window
            ack = False
            while not ack:
                choice = QMessageBox.critical(
                    None,
                    " ",
                    "Kundenname existiert bereits!",
                    QMessageBox.Ok
                )

                if choice:
                    ack = True
        # Check, if the new customer number is already used by any existing customer
        elif new_customer_number in current_customers["number"].map(str).to_list():
            # Runs and displays the MessageBox, as long as the user acknowledges the popup window
            ack = False
            while not ack:
                choice = QMessageBox.critical(
                    None,
                    " ",
                    "Kundennummer existiert bereits!",
                    QMessageBox.Ok
                )

                if choice:
                    ack = True
        # Check, if the new customer name and number is already used by any existing customer
        elif (
                new_customer_name in current_customers["name"].map(str).to_list() and
                new_customer_number in current_customers["number"].map(str).to_list()
            ):
            # Runs and displays the MessageBox, as long as the user acknowledges the popup window
            ack = False
            while not ack:
                choice = QMessageBox.critical(
                    None,
                    " ",
                    "Kundenname und Kundennummer existieren bereits!",
                    QMessageBox.Ok
                )

                if choice:
                    ack = True
        else:
            # Check for a new ID, which is not already used for an existing customer
            unused_index = False
            new_id = 1

            while not unused_index:
                if new_id not in current_customers["id"].values:
                    unused_index = True
                else:
                    new_id += 1
            data.at[0, "id"] = new_id

            ack = False
            
            # Customer name and customer numbers must be set
            if data["name"][0] and data["number"][0]:
                result =  self.db_access.add(data)

                # Runs and displays the MessageBox, so long till the user acknowledges the popup window
                while not ack:
                    if result[0]:
                        choice = QMessageBox.information(
                            None,
                            " ",
                            "Der Kunde wurde erfolgreich angelegt.",
                            QMessageBox.Ok
                        )
                    if not result[0] and result[1] == 0:
                        choice = QMessageBox.critical(
                            None,
                            " ",
                            "Der Kunde konnte nicht angelegt werden!\nDas File existiert nicht!",
                            QMessageBox.Ok
                        )

                    if choice:
                        ack = True
            else:
                # Runs and displays the MessageBox, until the user acknowledges the popup window.
                while not ack:
                    choice = QMessageBox.critical(
                        None,
                        " ",
                        "Es wurde kein Kundenname und / oder keine Kundennummer angegeben!",
                        QMessageBox.Ok
                    )

                    if choice:
                        ack = True


    def update_customer(self, updated_customers: pd.DataFrame) -> None:
        """ Stores the updated customers table in the database.

        Parameters
        ----------
        updated_customers : pandas.DataFrame
            Contains the information of the Table widget.

        Return
        ----------
        None
        """

        result = self.db_access.update(updated_customers)

        ack = False

        # Runs and displays the MessageBox, as long as the user acknowledges the popup window
        while not ack:
            if result[0]:
                choice = QMessageBox.information(
                    None,
                    " ",
                    "Die Kundendaten wurden erfolgreich geändert.",
                    QMessageBox.Ok
                )
            if not result[0] and result[1] == 0:
                choice = QMessageBox.critical(
                    None,
                    " ",
                    "Der Kundendaten konnten nicht geändert werden. Kein Zugriff auf die Datenbank!",
                    QMessageBox.Ok
                )

            if choice:
                break

    def delete_customer(self, row_data: list) -> bool:
        """ Deletes a customer from the database.

        Parameters
        ----------
        row_data : list
            Contains the row data (customer information) of the table widget, which should be deleted.

        Return
        ----------
        status : bool
            Represents the status, if the delete operation of the customer was successful or not.
        """

        current_customers = self.db_access.read_all("data/dataset.csv")
        # Get the row index, which contains
        row_id = get_row_index(current_customers["number"].map(str).to_list(), str(row_data[1]))
        updated_customers = current_customers.drop(row_id)

        result = self.db_access.delete(updated_customers)

        ack = False
        status = False

        # Runs and displays the MessageBox, as long as the user acknowledges the popup window
        while not ack:
            if result[0]:
                choice = QMessageBox.information(
                    None,
                    " ",
                    "Der Kunde wurde erfolgreich gelöscht.",
                    QMessageBox.Ok
                )
                status = True
            if not result[0] and result[1] == 0:
                choice = QMessageBox.critical(
                    None,
                    " ",
                    "Der Kunde konnte nicht gelöscht werden!\nDas File existiert nicht!",
                    QMessageBox.Ok
                )
                status = False

            if choice:
                break
        
        return status