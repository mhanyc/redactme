import unittest
from extract_names import parse_file


class TestNLTKExtration(unittest.TestCase):
    def test_sample_extraction(self):
        """
        Compare nltk's entity extraction to a freshly computed sample.
        This will mostly just insure you have nltk installed properly
        """
        known_wonderland_names = {'Please', 'Down', 'MARMALADE', 'Latitude',
                                  'Which', 'White Rabbit', 'Australia',
                                  'Dinah', 'No', 'Rabbit', 'Alice'}

        computed_names = parse_file('tests/wonderland_test.txt')

        assert(known_wonderland_names == computed_names)


if __name__ == '__main__':
    unittest.main()
