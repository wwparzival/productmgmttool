# Standard classes / libraries
import pandas as pd
import os

# Custom classes / libraries
from interfaces.DatabaseAccess import *

class CsvFileAccess(DatabaseAccess):
    """
    A class used to provide database access objects.

    Methods
    -------
    read()
        Reads a single dataset.
    read_all(str)
        Reads all datasets from the given path and returns them in a Dataframe.
    write()
        Not used.
    add(pandas.Dataframe)
        Adds a new Customer dataset to the database.
    update(pandas.Dataframe)
        Updates the customer datasets in the database.
    delete(pandas.Dataframe)
        Stores the Customer dataset with the delete rows to the database.
    """

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CsvFileAccess, cls).__new__(cls)
        return cls.instance

    def read(self) -> None:
        """ Reads a single dataset.

        Parameters
        ----------
        None

        Return
        ----------
        None
        """

        pass

    def read_all(self, path: str) -> pd.DataFrame:
        """ Reads all datasets from the given path and returns them in a Dataframe.

        Parameters
        ----------
        path : str
            The path of the file.
        
        Return
        ----------
        pandas.Dataframe
        """

        df = pd.DataFrame({})
    
        try:
            df = pd.read_csv(path)
        except:
            print("no file")
        finally:
            return df

    def write(self):
        pass

    def add(self, new_customer: pd.DataFrame) -> list:
        """ Adds a new Customer dataset to the database.

        Parameters
        ----------
        new_customer : pandas.Dataframe
            A dataframe, containing the customer data.
        
        Return
        ----------
        list
        """

        current_customers = self.read_all(self.path + "/data/dataset.csv")

        unused_index = False
        new_id = 1

        # Check for a new ID, which is not already used.
        while not unused_index:
            if new_id not in current_customers["id"].values:
                unused_index = True
            else:
                new_id += 1
        new_customer.at[0, "id"] = new_id

        # Stores the result codes
        # Element 0:
        #   False, if an error happened
        #   True, if no error happend
        # Element 1:
        #   Only used in conjunction with "False"
        #   Defines the type of error
        result = [False, -1]

        try:
            if not os.path.isfile(self.path + "/data/dataset.csv"):
                # Set to 0 for file error
                result[1] = 0
                raise Exception("File doesn't exist")
            else:
                new_customer.to_csv(self.path + "/data/dataset.csv", mode="a", header=False, index=False)
                result[0] = True
        finally:
            return result

    def update(self, updated_customers: pd.DataFrame) -> list:
        """ Updates the customer datasets in the database.

        Parameters
        ----------
        updated_customers : pandas.Dataframe
            A dataframe, containing the updated customer datasets.
        
        Return
        ----------
        list
        """

        # Stores the result codes
        # Element 0:
        #   False, if an error happened
        #   True, if no error happend
        # Element 1:
        #   Only used in conjunction with "False"
        #   Defines the type of error
        result = [False, -1]

        try:
            if not os.path.isfile(self.path + "/data/dataset.csv"):
                # Set to 0 for file error
                result[1] = 0
                raise Exception("File doesn't exist")
            else:
                updated_customers.to_csv(self.path + "/data/dataset.csv", mode="w", header=True, index=False)
                result[0] = True
        finally:
            return result

    def delete(self, updated_customers: pd.DataFrame) -> list:
        """ Stores the Customer dataset with the delete rows to the database.

        Parameters
        ----------
        updated_customers : pandas.Dataframe
            A dataframe, containing the updated customer datasets.
        
        Return
        ----------
        list
        """

        # Stores the result codes
        # Element 0:
        #   False, if an error happened
        #   True, if no error happend
        # Element 1:
        #   Only used in conjunction with "False"
        #   Defines the type of error
        result = [False, -1]

        try:
            if not os.path.isfile(self.path + "/data/dataset.csv"):
                # Set to 0 for file error
                result[1] = 0
                raise Exception("File doesn't exist")
            else:
                updated_customers.to_csv(self.path + "/data/dataset.csv", mode="w", header=True, index=False)
                result[0] = True
        finally:
            return result