import numpy as np

class Bitmap:
    def __init__(self, attrs):
        """
        Initialize a new Bitmap.

        Args:
            attrs : dict
                A dictionary mapping attribute names with their domains.
        """
        self.UB = []
        self.VB = []
        self.EB = []
        pass

    def insert(self, values):
        """
        Insert a new row into the bitmap.

        Args:
            values : list
                A list of values corresponding to each attribute for the new record.
        """
        pass

    def update(self, rid, values):
        """
        Update a row in the bitmap.

        Args:
            rid : int
                The id corresponding to the row being updated.
            values : dict
                A dictionary mapping attributes to their new values.
                Only needs to include attributes being updated.
        """
        pass

    def delete(self, rid):
        """
        Delete a row from the bitmap.

        Args:
            rid : int
                The id corresponding to the row being deleted.
        """
        pass

    def query(self):
        """
        ???
        """
        pass

