from unittest import TestCase
from linked_lists import Node, has_cycle

class TestHasCycle(TestCase):

    def test_has_cycle_testcase0(self):
        node = Node()
        self.assertEqual(False, has_cycle(node))
