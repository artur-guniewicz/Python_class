from queue import *
import unittest


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_str(self):
        self.assertEqual(str(self.queue), '[]')

    def test_eq(self):
        self.assertEqual(self.queue, Queue())

    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), True)

    def test_is_full(self):
        self.assertEqual(self.queue.is_full(), False)

    def test_pop(self):
        with self.assertRaises(ValueError):
            Queue().get()
        self.queue.put(31)
        self.assertEqual(self.queue.get(), 31)

    def test_push(self):
        self.queue.put(15)
        self.queue.put(18)
        self.queue.put(21)
        self.assertEqual(self.queue, Queue([15, 18, 21]))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()