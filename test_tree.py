import unittest
import utility

# python3 -m unittest -v <.py>


class TestTree(unittest.TestCase):
    def test_preorder_traversal(self):
        class TestFormat:
            def __init__(self, args, wants) -> None:
                self.args = args
                self.wants = wants
        cases = []
        cases.append(TestFormat(
            utility.TreeNode.turn_list_to_tree([27, 14, 35, 10, 19, 31, 42]),
            [27, 14, 10, 19, 35, 31, 42]))
        cases.append(TestFormat(
            utility.TreeNode.turn_list_to_tree([10, 3, 8, 9, 4]),
            [10, 3, 8, 4, 9]))

        for case in cases:
            result = utility.TreeNode.show_preorder_traversal(case.args)
            self.assertEqual(result, case.wants)

    def test_inorder_traversal(self):
        class TestFormat:
            def __init__(self, args, wants) -> None:
                self.args = args
                self.wants = wants
        cases = []
        cases.append(TestFormat(
            utility.TreeNode.turn_list_to_tree([27, 14, 35, 10, 19, 31, 42]),
            [10, 14, 19, 27, 31, 35, 42]))
        cases.append(TestFormat(
            utility.TreeNode.turn_list_to_tree([10, 3, 8, 9, 4]),
            [3, 4, 8, 9, 10]))

        for case in cases:
            result = utility.TreeNode.show_inorder_traversal(case.args)
            self.assertEqual(result, case.wants)

    def test_postorder_traversal(self):
        class TestFormat:
            def __init__(self, args, wants) -> None:
                self.args = args
                self.wants = wants
        cases = []
        cases.append(TestFormat(
            utility.TreeNode.turn_list_to_tree([27, 14, 35, 10, 19, 31, 42]),
            [10, 19, 14, 31, 42, 35, 27]))

        for case in cases:
            result = utility.TreeNode.show_postorder_traversal(case.args)
            self.assertEqual(result, case.wants)

    def test_traversal_BFS(self):
        class TestFormat:
            def __init__(self, args, wants) -> None:
                self.args = args
                self.wants = wants
        cases = []
        cases.append(TestFormat(
            utility.TreeNode.turn_list_to_tree([27, 14, 35, 10, 19, 31, 42]),
            [27, 14, 35, 10, 19, 31, 42]))

        for case in cases:
            result = utility.TreeNode.traversal_BFS(case.args)
            self.assertEqual(result, case.wants)


if __name__ == '__main__':
    unittest.main()
