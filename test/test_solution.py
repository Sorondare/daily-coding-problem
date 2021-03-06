import unittest

from problems import *


class Problem1(unittest.TestCase):

    def test_simple_solution(self):
        numbers = [10, 15, 3, 7]
        k = 17

        self.assertTrue(problem_1.simple_solution(numbers, k))

    def test_optimized_solution(self):
        numbers = [10, 15, 3, 7]
        k = 17

        self.assertTrue(problem_1.optimized_solution(numbers, k))


class Problem2(unittest.TestCase):

    def test_solution(self):
        integers = [1, 2, 3, 4, 5]

        self.assertEqual([120, 60, 40, 30, 24], problem_2.solution(integers))

    def test_solution_without_division(self):
        integers = [1, 2, 3, 4, 5]

        self.assertEqual([120, 60, 40, 30, 24], problem_2.solution_without_division(integers))


class Problem3(unittest.TestCase):

    def test_solution(self):
        node = problem_3.Node('root', problem_3.Node('left', problem_3.Node('left.left')), problem_3.Node('right'))

        self.assertEqual('left.left', problem_3.deserialize(problem_3.serialize(node)).left.left.val)
        self.assertEqual('right', problem_3.deserialize(problem_3.serialize(node)).right.val)

    def test_json(self):
        node = problem_3.Node('root', problem_3.Node('left', problem_3.Node('left.left')), problem_3.Node('right'))

        self.assertEqual('left.left', problem_3.deserialize_json(problem_3.serialize_json(node)).left.left.val)


class Problem4(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(2, problem_4.solution([3, 4, -1, 1]))
        self.assertEqual(3, problem_4.solution([1, 2, 0]))


class Problem5(unittest.TestCase):

    def test_car(self):
        self.assertEqual(3, problem_5.car(problem_5.cons(3, 4)))

    def test_cdr(self):
        self.assertEqual(4, problem_5.cdr(problem_5.cons(3, 4)))


class Problem6(unittest.TestCase):

    def test_XOR_list(self):
        xor_list = problem_6.XORLinkedList()

        for i in range(5):
            xor_list.add(i)

        self.assertEqual(2, xor_list.get(2).value)


class Problem7(unittest.TestCase):

    def test_solution(self):
        message = '111'

        self.assertEqual(3, problem_7.solution(message))

    def test_solution_with_long_message(self):
        message = '1234'

        self.assertEqual(3, problem_7.solution(message))


class Problem8(unittest.TestCase):

    def test_solution(self):
        tree = problem_8.Node(0, problem_8.Node(1),
                              problem_8.Node(0, problem_8.Node(1, problem_8.Node(1), problem_8.Node(1)),
                                             problem_8.Node(0)))

        self.assertEqual(5, problem_8.solution(tree))


class Problem9(unittest.TestCase):

    def test_solution(self):
        integers = [2, 4, 6, 2, 5]

        self.assertEqual(13, problem_9.solution(integers))

    def test_solution_not_adjacent(self):
        integers = [5, 1, 1, 5]

        self.assertEqual(10, problem_9.solution(integers))


class Problem11(unittest.TestCase):

    def test_solution(self):
        strings = ['dog', 'deer', 'deal']

        self.assertEqual(['deer', 'deal'], problem_11.solution(strings, 'de'))

    def test_solution_with_preprocess(self):
        strings = ['dog', 'deer', 'deal']

        self.assertEqual(['deer', 'deal'], problem_11.solution_with_preprocess(strings, 'de'))


class Problem12(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(5, problem_12.solution(4))


class Problem13(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(3, problem_13.solution("abcba", 2))

    def test_longuest_substring(self):
        self.assertEqual(7, problem_13.solution("aabihdanccab", 7))
