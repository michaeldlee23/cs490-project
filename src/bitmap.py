import numpy as np

from BitVector import BitVector


# noinspection PyInterpreter
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
            # ****
            # Can you index into a BitVector like this??????

    def insert(self, value):
        """
        Insert a new row into the bitmap.

        Args:
            value : int
                new value
        """
        # find i bitvector that val corresponds to
        #i = BitVector()
        #for bitvec in self.UB:
        #    if bitvec.intValue() == value:
        #        # if i does not have enough empty padding space
                # extend i's padding space
        # i's #elements++
        # i[#elements] = 1

        #bv = BitVector(intVal=self.UB, size=self.size++)

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
        # i = BitVector()
        #for bitvec in self.UB:
        #    if bitvec.intValue() == value:
        #        i = bitvec

        #old_val = 0 # (2) find old value old_val of row k TODO

        # (3) find the j bitvector that old_val corresponds to
        #j = BitVector()
        #for bitvec in self.UB:
        #    if bitvec.intValue() == value:
        #        j = bitvec
        # (4, 5)
        #i[rid] = '1' if i[rid] == '0' else '0'
        #j[rid] = '1' if j[rid] == '0' else '0'

        #Find the i bitvector that val corresponds to

        old_val = 0

        #Getting the old_val and updating the old row
        for val in self.VB:
            if self.VB[val][rid] == 1:
                old_val = val
                self.UB[val][rid] = 1

        #Update row for new value
        self.UB[value][rid] = 1

        pass

    def delete(self, rid):
        """
        Delete a row from the bitmap.

        Args:
            rid : int
                The id corresponding to the row being deleted.
        """

        # (1) find the val of row k
        #val = 0
        # (2) find the i bitvector that val corresponds to
        #i = 0
        # (3)
        #i[rid] = '1' if i[rid] == '0' else '0'

        #Find the value of rid
        #For each value, look through VB at the rid
        for val in self.VB:
            #If value at rid is 1 and UB is untouched, update UB
            if self.VB[val][rid] == 1 and self.UB[val][rid] == 0:
                self.UB[val][rid] = 1
            #**** MAY NOT NEED THIS BELOW
            #But if this rid has been switched to this value and hasn't been merged yet,
            #then, update the UB
            elif self.VB[val][rid] == 0 and self.UB[val][rid] == 1:
                self.UB[val][rid] = 0

        pass

    def search(self, val):
        """
        Find whether a value exists and if so, in which position(s)

        Args:
            val: int
                The attribute value that is being searched for

        """

        #Find the i bitvector that val corresponds to
        #i = BitVector()
        #for bitvec in self.UB:
        #    if bitvec.intValue() == 0:
        #****** Don't think I even need to do this

        #If the UB is all zeros, return the VB
        if self.UB[val].intValue() == 0:
            return self.VB[val]
        #Else, return the VB XOR UB
        else:
            return self.VB[val] ^ self.UB[val]

        pass

