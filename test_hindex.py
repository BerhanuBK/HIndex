import unittest
import hindex

class TestHindex(unittest.TestCase):
    def test_hindex(self):
        obj = hindex.Solution()
        result = obj.hIndex([0, 1, 3, 5, 6])
        self.assertEqual(result, 3)
        result = obj.hIndex([1,3,1])
        self.assertEqual(result, 1)
        result = obj.hIndex([0, 0])
        self.assertEqual(result, 0)

if __name__== "__main__":
    unittest.main()