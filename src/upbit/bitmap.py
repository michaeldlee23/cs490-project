import numpy as np

from BitVector import BitVector
<<<<<<< HEAD
import WAH
=======
>>>>>>> 18dead974ed491643174c8c58ba3ec60ba5a6f3f

class Bitmap:
    def __init__(self, data):
        """
        Initialize a new Bitmap.
<<<<<<< HEAD
=======

>>>>>>> 18dead974ed491643174c8c58ba3ec60ba5a6f3f
        Args:
            attrs : dict
                A dictionary mapping attribute names with their domains.
        """
        unq_vals = set(data)
        self.size = len(data)
        self.UB = {}
        self.VB = {}
        self.attribute = data
<<<<<<< HEAD
        self.fences = {}
=======
>>>>>>> 18dead974ed491643174c8c58ba3ec60ba5a6f3f

        for i in unq_vals:
            self.UB[i] = BitVector(size=self.size)
            self.VB[i] = BitVector(size=self.size)

        for index, value in enumerate(self.attribute):
            self.VB[value][index] = 1

<<<<<<< HEAD
    def insert(self, value):
        """
        Insert a new row into the bitmap.
=======

    def insert(self, value):
        """
        Insert a new row into the bitmap.

>>>>>>> 18dead974ed491643174c8c58ba3ec60ba5a6f3f
        Args:
            value : int
                new value
        """
<<<<<<< HEAD
        # find i bitvector that val corresponds to
        #i = BitVector()
        #for bitvec in self.UB:
        #    if bitvec.intValue() == value:
        #        if str(i)[-1] != 0: # if i does not have enough empty padding space
        #            i.pad_from_right(1) # extend i's padding space

        # i's #elements++ adjusts itself from padding i think?
        #i[-1] = '1' # i[#elements] = 1

        #UBi = self.UB[value]
=======

>>>>>>> 18dead974ed491643174c8c58ba3ec60ba5a6f3f
        self.attribute.append(value)
        hasPadding = 1

        # Checking if any of the last values of either VB or UB are 1
        # to see if there is padding space
        for val in self.VB:
            if self.VB[val][-1] == 1 or self.UB[val][-1] == 1:
                hasPadding = 0
                break

        if hasPadding == 0:  #Add padding space to each vb and ub
            for val in self.VB:
                self.VB[val].pad_from_right(1)
                self.UB[val].pad_from_right(1)
            self.size += 1
<<<<<<< HEAD
        #Set last value (if padded space was added or not?) to 1
        if value not in self.UB.keys():
            self.VB[value] = BitVector(size = self.size)
            self.UB[value] = BitVector(size = self.size)
        self.UB[value][-1] = 1
=======

        #Set last value (if padded space was added or not?) to 1
>>>>>>> 18dead974ed491643174c8c58ba3ec60ba5a6f3f
        self.VB[value][-1] = 1


    def update(self, rid, value):
        """
        Update a row in the bitmap.
<<<<<<< HEAD
=======

>>>>>>> 18dead974ed491643174c8c58ba3ec60ba5a6f3f
        Args:
            rid : int
                The id corresponding to the row being updated.
            value : int
                new value
        """

<<<<<<< HEAD
        # find i bitvector that val corresponds to
        #for idx in range(len(self.UB)): # iterate through all ub's
        #    if self.UB[idx].intValue() == value: # if one ub's intValue is 10
        #        for ub in range(len(self.UB)):
        #            if ub[idx] == 1: # ub is 20's UB (old value)
        #                if self.UB[idx] == '0': # negate new value
        #                    self.UB[idx] = '1'
        #                else:
        #                    self.UB[idx] = '0'
        #
        #                if ub == '0': # negate old value
        #                    ub = '1'
        #                else:
        #                    ub = '0'
        #                break

=======
>>>>>>> 18dead974ed491643174c8c58ba3ec60ba5a6f3f
        old_val = 0
        # Negate the old value
        for val in self.VB:
            if self.VB[val][rid] == 1:      #If old vb is 1, change ub to 1
                old_val = val
                self.UB[val][rid] = 1
            elif self.VB[val][rid] == 0 and self.UB[val][rid] == 1: #If ub is 1 and vb is 0, change ub to 0
                self.UB[val][rid] = 0

        # Negate the new value
        if self.UB[value][rid] == 0:    #If ub at rid is 0, then change to 1, otherwise change to 0
            self.UB[value][rid] = 1
        else:
            self.UB[value][rid] = 0

<<<<<<< HEAD
    def delete(self, rid):
        """
        Delete a row from the bitmap.
=======

    def delete(self, rid):
        """
        Delete a row from the bitmap.

>>>>>>> 18dead974ed491643174c8c58ba3ec60ba5a6f3f
        Args:
            rid : int
                The id corresponding to the row being deleted.
        """

<<<<<<< HEAD
        # We need to retrieve the value Bi of this row k
        #for idx in range(len(self.VB)):
        #    if self.VB[idx][rid] == 1:
                # Find the update bitvector corresponding to this value Bi
                # Negate the contents of the selected update bitvector for row k
        #        if self.UB[idx] == '0': # negate new value
        #            self.UB[idx] = '1'
        #        else:
        #            self.UB[idx] = '0'

=======
>>>>>>> 18dead974ed491643174c8c58ba3ec60ba5a6f3f
        # Find the value of rid
        # For each value, look through VB at the rid
        for val in self.VB:
            # If value at rid is 1 and UB is untouched, update UB
            if self.VB[val][rid] == 1 and self.UB[val][rid] == 0:
                self.UB[val][rid] = 1
            # But if this rid has been switched to this value and hasn't been merged yet,
            # then, update the UB
            elif self.VB[val][rid] == 0 and self.UB[val][rid] == 1:
                self.UB[val][rid] = 0
        pass

<<<<<<< HEAD
    def query(self, value):
        """
        ???
        """
        # (1) find i bitvector that val corresponds to
        #i = BitVector()
        #for idx in range(len(self.UB)):
        #    if self.UB[idx].intValue() == value:
        #        # if Ui contains only zero then
        #        if int(str(self.UB[idx])) == 0:
        #            return self.VB[idx]
        #        else:
        #            return self.UB[idx] ^ self.VB[idx]
        #return None

        # If the UB is all zeros, return the VB

        made = ""
        if self.UB[value].intValue() == 0:
            made = self.VB[value]
        # Else, return the VB XOR UB
        else:
            made = self.VB[value] ^ self.UB[value]
        comp, fence = WAH.compress(made)
        que = BitVector(bitstring = comp)
        print(comp)
        print(fence)
        counter = 0
        table_index = []
        for i in fence:
            if que[counter] == 0:
                for x in range(i, min(i+31, len(self.attribute))):
                    if self.attribute[x] == value:
                        table_index.append(self.attribute[x])
            elif que[counter] == 1 and que[counter+1] == 1:
                count = BitVector(bitstring = que[counter+2:counter+31]).intValue()
                for q in range(i, i + (31 * count)):
                    table_index.append(self.attribute[q])
            counter += 31
        print(table_index)
        return table_index
=======

    def query(self, value):
        """
        Search for a bitvector of a certain value.

        Args:
            value : int
                The
        """

        # Make sure value is valid key
        if value in self.VB.keys():
            # If the UB is all zeros, return the VB
            if self.UB[value].intValue() == 0:
                return self.VB[value]
            # Else, return the VB XOR UB
            else:
                return self.VB[value] ^ self.UB[value]
        else:
            return None

>>>>>>> 18dead974ed491643174c8c58ba3ec60ba5a6f3f
