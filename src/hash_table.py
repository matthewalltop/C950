# Author: Brian Matthew Alltop
# StudentID: 000820333
# WGU C950 - Data Structures & Algorithms 2

class HashTable:
    """A hash table implementation"""
    def __init__(self, size=10):
        self.values = []
        for _ in range(size):
            self.values.append([])

    def add_or_update(self, key, value):
        """Adds key/value pair into hash table.
           Runs at: O(n)"""
        hash_key = self.__generate_hash(key)
        key_value = [hash_key, value]

        if self.values[hash_key] is not None and len(self.values[hash_key]) != 0:
            for kvp in self.values[hash_key]:
                # Update the value if it already exists
                if kvp[0] == hash_key:
                    kvp[1] = value
                    break
                else:
                    self.values[hash_key].append(key_value)
        else:
            # This is new, add it
            self.values[hash_key] = []
            self.values[hash_key].append(key_value)



    def get_item(self, key):
        hash_key = self.__generate_hash(key)
        if self.values[hash_key] is None:
            raise KeyError()
        else:
            for kvp in self.values[hash_key]:
                if kvp[0] == key:
                    return kvp[1]
        
        raise KeyError()


    def __generate_hash(self, key):
        """Basic hash function.
            Runs at: O(1)"""
        length = len(self.values)
        return int(key) % length


