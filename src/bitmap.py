import numpy as np
import BitVector


from BitVector import BitVector

class Bitmap:
    def __init__(self, data):
        """
        Initialize a new Bitmap.

        Args:
            attrs : dict
                A dictionary mapping attribute names with their domains.
        """
        unq_vals = set(data)
        self.size = len(data)
        self.UB = {}
        self.VB = {}
        self.attribute = data

        for i in unq_vals:
            self.UB[i] = BitVector.BitVector(size=self.size)
            self.VB[i] = BitVector.BitVector(size=self.size)

        for index, value in enumerate(self.attribute):
            self.VB[value][index] = 1

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

