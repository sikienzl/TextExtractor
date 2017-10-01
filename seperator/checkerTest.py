import operator
import seperator.checker

delete_empty_lines1 = '''

'''
delete_empty_lines2 = []

get_wiederholung_list1 = ['dies ist ein test', 'dies ist ein test', 'Der Bär war gesund','dies ist ein test','dies ist ein test','dies ist ein test','dies ist ein test']
get_wiederholung_list2 = ['dies ist ein test']


def test_delete_empty_lines(self):
    operator.eq_(seperator.checker.delete_empty_lines(delete_empty_lines1), delete_empty_lines2)

def test_get_wiederholung_list(self):
    operator.eq__(seperator.checker.get_wiederholung_list(get_wiederholung_list1), get_wiederholung_list2)