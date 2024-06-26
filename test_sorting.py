from plot_line import counting, quick_sort
import unittest
import random
class Test(unittest.TestCase):
    def test_sort(self):
        a = random.sample(range(-1000, 1000), 10)
        n = a.copy()
        a.sort()
        quick_sort(n, 0, len(n)-1)
        self.assertEqual(a,n)

if __name__ == '__main__':
    unittest.main()

