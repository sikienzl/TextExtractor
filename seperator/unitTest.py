import unittest
import checker

delete_empty_lines1 = '''

'''
delete_empty_lines2 = []

get_wiederholung_list1 = ['dies ist ein test', 'dies ist ein test', 'Der Bär war gesund','dies ist ein test','dies ist ein test','dies ist ein test','dies ist ein test']
get_wiederholung_list2 = ['dies ist ein test']

class checkerTest(unittest.TestCase):
    def test_delete_empty_lines(self):
        self.assertEqual(checker.delete_empty_lines(delete_empty_lines1),delete_empty_lines2)
    def test_get_wiederholung_list(self):
        self.assertEqual(checker.get_wiederholung_list(get_wiederholung_list1), get_wiederholung_list2)

if __name__ == '__main__':
    unittest.main()
