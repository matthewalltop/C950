import unittest

from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def test_hash_table_init(self):
        self.hash_map = HashTable()
        self.assertEqual(self.hash_map.capacity, 100)
        self.assertEqual(self.hash_map._size, 0)

    def test_hash_table_set_item(self):
        self.hash_map = HashTable()
        self.hash_map['key'] = 'value'
        self.assertEqual(self.hash_map['key'], 'value')

    def test_hash_table_get_item(self):
        self.hash_map = HashTable()
        self.hash_map['key'] = 'value'
        self.assertEqual(self.hash_map['key'], 'value')

    def test_hash_table_iter(self):
        self.hash_map = HashTable()
        self.hash_map['key'] = 'value'
        self.hash_map['key2'] = 'value2'
        self.hash_map['key3'] = 'value3'
        for elm in self.hash_map:
            self.assertIn(elm, [[['key', 'value']], [['key2', 'value2']], [['key3', 'value3']]])


if __name__ == '__main__':
    unittest.main()
