from unittest import TestCase
from linked_list import Node, LinkedList

class TestMyLinkedList(TestCase):
    def test_add_reverse(self):
        try:
            from build import add_reverse
        except ImportError:
            self.assertFalse("no function found")

        self.assertEqual(add_reverse(None, None), None)
        self.assertEqual(add_reverse(Node(5), None), None)
        self.assertEqual(add_reverse(None, Node(10)), None)

        print('Test: Add values of different lengths')
        # Input 1: 6->5->None
        # Input 2: 9->8->7
        # Result: 5->4->8
        first_list = LinkedList(Node(6))
        first_list.append(5)
        second_list = LinkedList(Node(9))
        second_list.append(8)
        second_list.append(7)
        result = add_reverse(first_list, second_list)
        self.assertEqual(result.get_all_data(), [5, 4, 8])

        print('Test: Add values of same lengths')
        # Input 1: 6->5->4
        # Input 2: 9->8->7
        # Result: 5->4->2->1
        first_head = Node(6)
        first_list = LinkedList(first_head)
        first_list.append(5)
        first_list.append(4)
        second_head = Node(9)
        second_list = LinkedList(second_head)
        second_list.append(8)
        second_list.append(7)
        result = add_reverse(first_list, second_list)
        self.assertEqual(result.get_all_data(), [5, 4, 2, 1])
