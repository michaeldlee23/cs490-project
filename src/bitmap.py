import numpy as np

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
                if str(i)[-1] != 0: # if i does not have enough empty padding space
                    i.pad_from_right(1) # extend i's padding space
        
        # i's #elements++ adjusts itself from padding i think?
        i[-1] = '1' # i[#elements] = 1

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

        # find i bitvector that val corresponds to
        for idx in range(len(self.UB)): # iterate through all ub's
            if self.UB[idx].intValue() == value: # if one ub's intValue is 10
                for ub in range(len(self.UB)):
                    if ub[idx] == 1: # ub is 20's UB (old value)
                        if self.UB[idx] == '0': # negate new value
                            self.UB[idx] = '1'
                        else:
                            self.UB[idx] = '0'
                        
                        if ub == '0': # negate old value
                            ub = '1'
                        else:
                            ub = '0'
                        break

        
        pass

    def delete(self, rid):
        """
        Delete a row from the bitmap.

        Args:
            rid : int
                The id corresponding to the row being deleted.
        """

        # We need to retrieve the value Bi of this row k
        for idx in range(len(self.VB)):
            if self.VB[idx][rid] == 1:
                # Find the update bitvector corresponding to this value Bi
                # Negate the contents of the selected update bitvector for row k
                if self.UB[idx] == '0': # negate new value
                    self.UB[idx] = '1'
                else:
                    self.UB[idx] = '0'
        pass

    def query(self, value):
        """
        ???
        """
        # (1) find i bitvector that val corresponds to
        i = BitVector()
        for idx in range(len(self.UB)):
            if self.UB[idx].intValue() == value:
                # if Ui contains only zero then
                if int(str(self.UB[idx])) == 0:
                    return self.VB[idx]
                else:
                    return self.UB[idx] ^ self.VB[idx]
        return None

