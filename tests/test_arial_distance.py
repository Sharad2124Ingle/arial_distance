import unittest
import sys
import os

from arial_distance.arial_distance import get_distance
# from arial_distance import arial_distance

class TestArialDistance(unittest.TestCase):
    def test_distance(self):
        # Write your test case here
        source = 19.207084243604214, 73.12916639835512
        distination = 19.210002125062804, 73.11869505407905
        self.assertEqual(get_distance(source, distination), 1.146408489108353)

if __name__ == '__main__':
    unittest.main()
