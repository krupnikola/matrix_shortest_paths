import unittest
from path_finder import PathFinder


class TestPath(unittest.TestCase):

    def test_one_path(self):
        map = 'tests/3x3_one_path.xml'
        self.assertEqual(PathFinder.get_shortest_paths(map)['paths'],
                         [{'points': [{'row': 1, 'col': 1}, {'row': 2, 'col': 1}, {'row': 2, 'col': 2},
                                      {'row': 2, 'col': 3}]}])

    def test_multiple_paths(self):
        map = 'tests/3x3_two_paths.xml'
        self.assertEqual(PathFinder.get_shortest_paths(map)['paths'],
                         [{'points': [{'col': 1, 'row': 1}, {'col': 1, 'row': 2}, {'col': 1, 'row': 3},
                                      {'col': 2, 'row': 3}]}, {
                              'points': [{'col': 1, 'row': 1}, {'col': 1, 'row': 2}, {'col': 2, 'row': 2},
                                         {'col': 2, 'row': 3}]}])

    def test_no_paths(self):
        map = 'tests/3x3_no_paths.xml'
        self.assertEqual(PathFinder.get_shortest_paths(map)['paths'], [{'points': ['No paths found']}],)

    def test_start_or_end_out_of_matrix(self):
        map = 'tests/3x3_start_out_of_matrix.xml'
        self.assertEqual(PathFinder.get_shortest_paths(map), "Start/End node not in matrix.")

    def test_invalid_xml_content(self):
        map = 'tests/3x3_invalid_xml_tag.xml'
        self.assertEqual(PathFinder.get_shortest_paths(map), "Invalid content of .xml file.")


if __name__ == '__main__':
    unittest.main()
