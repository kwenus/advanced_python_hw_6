from vote_function import vote, ls_1, ls_2, ls_3, ls_4
import unittest
from unittest_parametrize import parametrize
from unittest_parametrize import ParametrizedTestCase


class TestVote(ParametrizedTestCase):

    # проверка на правильный вывод
    @parametrize(('ls','expected_output'),
                 [(ls_1, 1),
                           (ls_2, 2),
                           (ls_3, 'b'),
                           (ls_4, -4)])
    def test_vote_correct_output(self, ls, expected_output):
        self.assertEqual(vote(ls), expected_output)



