# Author: Brian Matthew Alltop
# StudentID: 000820333
# WGU C950 - Data Structures & Algorithms 2
from typing import Generic, Optional, TypeVar

Key = TypeVar('Key')
Value = TypeVar('Value')


class HashTable(Generic[Key, Value]):
    """A hash table implementation"""

    def __init__(self, capacity=100):
        self.values = []
        self.capacity = capacity
        self._size = 0
        for _ in range(capacity):
            self.values.append([])

    def __len__(self):
        return self._size

    # From here: https://rszalski.github.io/magicmethods/
    # Inherited from Python to make this a legit collection class.
    def __iter__(self):
        not_empty = [x for x in self.values if x != []]
        return iter([el[0] for el in not_empty])

    def __getitem__(self, key: Key):
        hash_key = self.__generate_hash(key)
        if self.values[hash_key] is None:
            raise KeyError()
        else:
            for kvp in self.values[hash_key]:
                if kvp[0] == key:
                    return kvp[1]

        raise KeyError()

    def __setitem__(self, key, value):
        """Adds key/value pair into hash table.
                 Runs at: O(n)"""
        hash_key = self.__generate_hash(key)
        if hash_key > self.capacity:
            self.capacity = hash_key + 5
            self.__resize(hash_key)

        kv = [key, value]

        if self.values[hash_key] is not None:
            for kvp in self.values[hash_key]:
                if kvp[0] == key:
                    kvp[1] = kv
            self.values[hash_key].append(kv)
            self._size += 1
            return True
        else:
            self.values[hash_key] = list([kv])
            self._size += 1

    def __delitem__(self, key: Key):
        """ Removes item from hash table
        :param key: Key of item to remove
        :return: void
        """
        hash_key = self.__generate_hash(key)
        if self.values[hash_key] is None:
            raise KeyError()
        else:
            # In this case we need to remove a sub-index instead of removing the entire value at the given key
            for elm in range(0, self.values[hash_key]):
                if self.values[hash_key][elm][0] == key:
                    return self.values[hash_key].pop(elm)

        raise KeyError()

    def __resize(self):
        """ Resizes hash table in place.
        :return:
        """
        temp = self.values
        self.values = []
        new_values = [] * self.capacity
        for (k, v) in temp:
            new_values[k] = v

    def update_item(self, key: Key, value):
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

    def __generate_hash(self, key: Key):
        """Basic hash function.
            Runs at: O(1)"""
        length = len(self.values)
        return hash(key) % length
