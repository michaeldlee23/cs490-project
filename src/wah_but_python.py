class wah_py:
    def __init__(self, data):
        to_compress = data
        compressed = []
        counter = 0
        previous_bit_bunch = 0
    
    def compress(self, input):
        bits = input()
        # Take in 31 bits, compress and add signal bit and add to compressed list, update previous list using counter as marker
        # three conditions: if 31 bits are all 0, if 31 bits are all 1, or if 31 bits are mixed,
        # if mixed add 31 bits to full list and add signal bit, else add signal bit and if next 31 bits are all same with same
        # bit number update count of previous marked by counter and check if type is same as previous_bit_bunch

    def update_count(self, bit_type):
        # Increasing count when consecutive bunch of same bits occur
        pass

    #Possibly add function to return full list or maybe just use compress for everything except update_count.