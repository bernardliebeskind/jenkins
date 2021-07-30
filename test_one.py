import unittest
import one


# unit testing has to be a subclass of the unit test class
# must name all functions starting with "test" for test class to recognize it

class TestOne(unittest.TestCase):

    def test_one(self):
        result = one.one()
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
