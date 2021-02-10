from abc import ABC, abstractmethod


class BusinessObject(ABC):
    """Collective base class for the implementation of all relevant classes 
    within this project.
    
    A central attribut of all business objects is the id, which is the primary key
    in a relational database.
    Another attribute of all business objects is the creation date. 
    """

    def __init__(self):
        self._id = 0 #unique id of a business object
        self._creation_date = ''

    def get_id(self):
        """reads out the id."""
        return self._id

    def set_id(self, val):
        """Sets the id."""
        self._id = val

    def get_date(self):
        """Reads out of the creation date."""
        return self._creation_date

    def set_date(self, creation_date):
        """Sets the creation date."""
        self._creation_date = creation_date
