from cookbook import cookbook, calculate_products, product_list_1, product_list_2, cookbook_dict, cookbook_tuple
import unittest
from unittest_parametrize import parametrize
from unittest_parametrize import ParametrizedTestCase


class TestCookbook(ParametrizedTestCase):

    # проверка на правильность расчетов
    @parametrize(('cookbook', 'persons','expected_product_list'),
                 [(cookbook, 5, product_list_1),
                           (cookbook, 10, product_list_2)])
    def test_calculate_correct_amounts(self, cookbook, persons, expected_product_list):
        self.assertEqual(calculate_products(cookbook, persons), expected_product_list)

    # проверяем, возвращаемое значение (только список)
    @parametrize(('cookbook','persons'),
                 [(cookbook, 1),
                           (cookbook, 20)])
    def test_calculate_correct_instance(self, cookbook, persons):
        self.assertIsInstance(calculate_products(cookbook, persons), list)

    # проверка принимаемого значения (только список или кортеж)
    @parametrize(('cookbook', 'persons'),
                 [(cookbook_dict, 5),
                           (cookbook_tuple, 8),
                           (cookbook, 2)])
    def test_calculate_input(self, cookbook, persons):
        try:
            self.assertIsInstance(calculate_products(cookbook, persons), list)
        except IndexError:
            print(' !!! Error type of input value  ')











