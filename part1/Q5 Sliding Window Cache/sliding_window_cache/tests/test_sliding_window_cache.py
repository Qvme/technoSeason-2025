import unittest
from src.sliding_window_cache import SlidingWindowCache, SlidingWindowException

class TestSlidingWindowCache(unittest.TestCase):
    def test_add_and_get_recent_windows(self):
        cache = SlidingWindowCache(capacity=5)
        cache.add("key1", "value1")
        cache.add("key2", "value2")
        cache.add("key3", "value3")
        cache.add("key4", "value4")
        cache.add("key5", "value5")

        self.assertEqual(list(cache.get_recent_windows(3)), [("key5", "value5"), ("key4", "value4"), ("key3", "value3")])
        self.assertEqual(list(cache.get_recent_windows(3, reverse=True)), [("key3", "value3"), ("key4", "value4"), ("key5", "value5")])

    def test_get_recent_windows_with_negative_n(self):
        cache = SlidingWindowCache(capacity=5)
        with self.assertRaises(SlidingWindowException) as context:
            cache.get_recent_windows(-1)
        self.assertEqual(str(context.exception), "requested no of windows should be positive")

    def test_get_recent_windows_with_n_greater_than_capacity(self):
        cache = SlidingWindowCache(capacity=5)
        with self.assertRaises(SlidingWindowException) as context:
            cache.get_recent_windows(6)
        self.assertEqual(str(context.exception), "request exceeds cache size.")

if __name__ == '__main__':
    unittest.main()
