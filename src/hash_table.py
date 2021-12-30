# Author: Brian Matthew Alltop
# StudentID: 000820333
# WGU C950 - Data Structures & Algorithms 2


class HashTable:
    """A hash table implementation"""
    def __init__(self, size=10):
        self.values = []
        for _ in range(size):
            self.values.append([])

    def insert_item(self, key, value):
        """Adds key/value pair into hash table.
           Runs at: O(n)"""
        hash_key = self.__generate_hash(key)
        kv = [key, value]

        if self.values[hash_key] is not None:
            for kvp in self.values[hash_key]:
                if kvp[0] == key:
                    kvp[1] = kv
            self.values[hash_key].append(kv)
            return True
        else:
            self.values[hash_key] = list([kv])

    def update_item(self, key, value):
        """Updates and existing key/value pair in hash table.
           Runs at: O(n)"""
        hash_key = self.__generate_hash(key)
        if self.values[hash_key] is None:
            raise KeyError()
        else:
            for kvp in self.values[hash_key]:
                if kvp[0] == key:
                    kvp[1] = value

        raise KeyError()

    def get_item(self, key):
        """Retrieves an item from the hash table associated with the given key.
           Runs at: O(n)"""
        hash_key = self.__generate_hash(key)
        if self.values[hash_key] is None:
            raise KeyError()
        else:
            for kvp in self.values[hash_key]:
                if kvp[0] == key:
                    return kvp[1]
        
        raise KeyError()

    def delete_item(self, key):
        hash_key = self.__generate_hash(key)
        if self.values[hash_key] is None:
            raise KeyError()
        else:
            # In this case we need to remove a sub-index instead of removing the entire value at the given key
            for elm in range(0, self.values[hash_key]):
                if self.values[hash_key][elm][0] == key:
                    return self.values[hash_key].pop(elm)

        raise KeyError()


    def __generate_hash(self, key):
        """Basic hash function.
            Runs at: O(1)"""
        length = len(self.values)
        return int(key) % length


