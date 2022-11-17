import unittest 
from parameterized import parameterized

from hw_task_2 import get_unique_ids, ids
from hw_task_4 import get_key_from_max_value, stats
from hw_task_5 import get_convert_list_to_dicts, list_


FIXTURES_TASK_2 = [
    (ids, [15, 35, 54, 98, 119, 213])
]

FIXTURES_TASK_4 = [
    (stats, 'yandex')
]

FIXTURES_TASK_5 = [
    (list_, {'2018-01-01': {'yandex': {'cpc': 100}}})
]


class TestFunc(unittest.TestCase):
    @parameterized.expand(FIXTURES_TASK_2)
    def test_get_unique_ids(self, dct, etalon):
        result = get_unique_ids(dct)
        self.assertEqual(result, etalon)
     
    @parameterized.expand(FIXTURES_TASK_4)
    def test_get_key_from_max_value(self, dct, etalon):
        result = get_key_from_max_value(dct)
        self.assertEqual(result, etalon)
        
    @parameterized.expand(FIXTURES_TASK_5)
    def test_get_convert_list_to_dicts(self, lst, etalon):
        result = get_convert_list_to_dicts(lst)
        self.assertEqual(result, etalon)


if __name__ == '__main__':
    unittest.main()