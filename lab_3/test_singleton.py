import denysenko_singleton
import unittest
class TestSingleton(unittest.TestCase):
    def test_result(self):
        s = Singleton(1,2)
        self.assertEqual(s.result(), 3)

    def test_singleton():
        s = Singleton(1,2)
        m = Singleton(3,4)
        self.assertEqual(id(s), id(m))
if __name__ == '__main__':
    unittest.main()
