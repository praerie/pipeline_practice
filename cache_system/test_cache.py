import unittest
from hash_table import HashTable

class TestAssetCache(unittest.TestCase):

    def setUp(self):
        # create a new hash table before each test
        self.cache = HashTable()

    def test_put_and_get(self):
        # test that a key-value pair can be added and retrieved
        self.cache.put("SHOT_014_ANIM", "cache/anim/shot_014/charA_cache_v03.abc")
        result = self.cache.get("SHOT_014_ANIM")
        self.assertEqual(result, "cache/anim/shot_014/charA_cache_v03.abc")

    def test_update_existing_key(self):
        # test that inserting a key again updates the value
        self.cache.put("SHOT_014_ANIM", "old_path.abc")
        self.cache.put("SHOT_014_ANIM", "new_path.abc")
        result = self.cache.get("SHOT_014_ANIM")
        self.assertEqual(result, "new_path.abc")

    def test_delete_key(self):
        # test that a key-value pair can be deleted
        self.cache.put("SHOT_015_LIGHT", "cache/light/shot_015/rig.mb")
        self.assertTrue(self.cache.delete("SHOT_015_LIGHT"))
        self.assertIsNone(self.cache.get("SHOT_015_LIGHT"))

    def test_nonexistent_key(self):
        # test that getting a non-existent key returns None
        result = self.cache.get("SHOT_999_COMP")
        self.assertIsNone(result)

    def test_collision_handling(self):
        # test that collisions are handled correctly using linked lists

        class TestHash(HashTable):
            # override hash function to force collision
            def _hash(self, key): return 0

        test_cache = TestHash()
        test_cache.put("A", "value1")
        test_cache.put("B", "value2")

        self.assertEqual(test_cache.get("A"), "value1")
        self.assertEqual(test_cache.get("B"), "value2")

if __name__ == "__main__":
    unittest.main()
