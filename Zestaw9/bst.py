class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def insert(self, node):
        if self.value < node.value:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
        elif self.value > node.value:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            pass

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, value):
        if self.value == value:
            return self
        if value < self.value:
            if self.left:
                return self.left.search(value)
        else:
            if self.right:
                return self.right.search(value)
        return None


def bst_min(root):
    if root.left is not None:
        return bst_min(root.left)
    else:
        return root


def bst_max(root):
    if root.right is not None:
        return bst_max(root.right)
    else:
        return root
