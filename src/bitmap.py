import numpy as np

from BitVector import BitVector

class Bitmap:
    def __init__(self, attrs, data):
        """
        Initialize a new Bitmap.

        Args:
            attrs : dict
                A dictionary mapping attribute names with their domains.
        """
        unq_vals = set(data[0])
        self.UB = {}
        self.VB = []
        self.EB = []
        for i in unq_vals:
            self.UB[i] = {}

    def insert(self, value):
        """
        Insert a new row into the bitmap.

        Args:
            value : int
                new value
        """
        # find i bitvector that val corresponds to
        i = BitVector()
        for bitvec in self.UB:
            if bitvec.intValue() == value:
                # if i does not have enough empty padding space
                # extend i's padding space
        # i's #elements++
        # i[#elements] = 1

        pass

    def update(self, rid, value):
        """
        Update a row in the bitmap.

        Args:
            rid : int
                The id corresponding to the row being updated.
            value : int
                new value
        """

        # (1) find i bitvector that val corresponds to
        i = BitVector()
        for bitvec in self.UB:
            if bitvec.intValue() == value:
                i = bitvec

        old_val = 0 # (2) find old value old_val of row k TODO

        # (3) find the j bitvector that old_val corresponds to
        j = BitVector()
        for bitvec in self.UB:
            if bitvec.intValue() == value:
                j = bitvec
        # (4, 5)
        i[rid] = '1' if i[rid] == '0' else '0'
        j[rid] = '1' if j[rid] == '0' else '0'

        pass

    def delete(self, rid):
        """
        Delete a row from the bitmap.

        Args:
            rid : int
                The id corresponding to the row being deleted.
        """

        # (1) find the val of row k
        val = 0
        # (2) find the i bitvector that val corresponds to
        i = 0
        # (3)
        i[rid] = '1' if i[rid] == '0' else '0'

        pass

    def query(self):
        """
        ???
        """
        pass

