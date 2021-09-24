class Node:
    def __init__(self, value, parent=None):
        self.left = None
        self.right = None
        self.parent = parent
        self.value = value


class Tree:
    def __init__(self):
        self.root = None

    def search(self, value):
        found_node = self._search(self.root, value)
        if found_node:
            return True
        return False

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        self._insert(self.root, value)

    def min_elem(self):
        pass

    def max_elem(self):
        pass

    def print_elems(self):
        if not self.root:
            print("No elements in tree")
            return
        print(self.root.value, end=", ")
        self._print_node_child(self.root.left)
        self._print_node_child(self.root.right)
        print(chr(8)*2)

    def _print_node_child(self, current_node):
        if current_node:
            print(current_node.value, end=", ")
            self._print_node_child(current_node.left)
        else:
            return

        if current_node.left:
            self._print_node_child(current_node.left)
        if current_node.right:
            self._print_node_child(current_node.right)

    def _search(self, node_to_check, value):
        if (not node_to_check) or node_to_check.value == value:
            return node_to_check

        if value > node_to_check.value:
            return self._search(node_to_check.right, value)
        else:
            return self._search(node_to_check.left, value)

    def _insert(self, node_to_insert, value):
        if value > node_to_insert.value:
            if not node_to_insert.right:
                node_to_insert.right = Node(value, node_to_insert)
                return
            else:
                return self._insert(node_to_insert.right, value)
        else:
            if not node_to_insert.left:
                node_to_insert.left = Node(value, node_to_insert)
                return
            else:
                return self._insert(node_to_insert.left, value)


if __name__ == "__main__":
    test = Tree()
    test.insert(5)
    test.insert(6)
    test.insert(-1)
    test.insert(0)
    test.insert(79)
    test.insert(9)
    test.insert(2)
    print(test.search(5))
    print(test.search(9))
    print(test.search(2))
    print(test.search(0))
    test.print_elems()
