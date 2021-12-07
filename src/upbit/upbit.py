import numpy as np

from bitmap import Bitmap

class UpBit:
    def __init__(self, dataset):
        # for each attribute in dataset, create a Bitmap
        bitmaps = {attr: Bitmap(data) for (attr, data) in dataset}
        attributes = [attr for attr in dataset.keys()]

    def insert(self, record):
        """
        Insert a new record into the index.

        Args:
            record : dict
                dictionary of form {attr : value}

        Returns:
            None
        """
        # Find the i bitvector that val corresponds to
        # if Ui does not have enough empty padding space
        #     extend Ui padding space
        # Ui.num_elements += 1
        # Ui[Ui.num_elements] = 1
        for attr, value in record.items():
            bitmaps[attr].insert(value)

    def update(self, rid, values):
        """
        Update a row in the index

        Args:
            rid : int
                The id corresponding to the row being updated
            values : dict
                dictionary of attributes with their new values

        Returns:
            None
        """
        # Find the i bitvector that val corresponds to
        # Find the old value old_val of row rid
        # Find the j bitvector that old_val corresponds to
        # Ui[k] = !Ui[k]
        # Uj[k] = !Uj[k]
        for attr, value in values.items():
            bitmaps[attr].update(rid, value)

    def delete(self, rid):
        """
        Delete a row from the index

        Args:
            rid : int
                The id corresponding to the row being deleted

        Returns:
            None
        """
        # Find the val of row rid
        # Find the i bitvector that val corresponds to
        # Ui[k] = !Ui[k]
        for attr in attributes:
            bitmaps[attr].delete(rid)

    def get_value(rid):
        # for each i in domain
        #     temp_bit = Vi.get_bit(rid) XOR Ui.get_bit(rid)
        #     if temp_bit
        #         return val_i

    def get_bit(B, rid):
        # position = fence_pointer.nearest(rid)
        # while position < rid
        #     if isFill(B[position])
        #         value, length = decode(B[pos])
        #         if (position + length) * 31 < rid:
        #             position += length
        #         else:
        #             return value
        #     else:
        #         if position * 31 - rid < 31:
        #             return B[position] & (1 << (rid % 31))
        #         else:
        #             position += 1

    def query(self, val):
        """
        Determines whehter the given value exists in the indexed column, and in which position.

        Args:
            val : int
                The search value

        Returns:
            result : BitVector
                A BitVector corresponding to which records matched the query
        """
        # Find the i bitvector that val corresponds to
        # if Ui contains only zeros then
        #     return Vi
        # else
        #     return Vi XOR Ui
        pass

