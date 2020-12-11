class Node:
    def __init__(self, value=None, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


class DoubleList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __str__(self):
        result = ''
        current = self.head
        while current is not None:
            result += (',' + str(current))
            current = current.next
        result = '[' + result[1:] + ']'
        return result

    def find_max(self):
        current = self.head
        max_node = current
        while current.next is not None:
            current = current.next
            if current > max_node:
                max_node = current
        return max_node

    def find_min(self):
        current = self.head
        min_node = current
        while current.next is not None:
            current = current.next
            if current < min_node:
                min_node = current
        return min_node

    def remove(self, node):
        if self.is_empty():
            raise ValueError("The List is empty")
        elif node == self.head:
            self.remove_head()
        elif node == self.tail:
            self.remove_tail()
        else:
            current = self.head
            while current.next is not None and current != node:
                current = current.next
            previous_node = current.previous
            next_node = current.next

            previous_node.next = current.next
            next_node.previous = previous_node

    def clear(self):
        current = self.tail
        self.tail = None
        while current.previous is not None:
            current = current.previous

            current.next.value = None
            current.next.previous = None
            current.next = None

        self.head.value = None
        self.head = None

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.head:
            node.next = self.head
            self.head.previous = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.length += 1

    def insert_tail(self, node):
        if self.tail:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.length += 1

    def remove_head(self):
        if self.head is None:
            raise ValueError("The List is empty")
        elif self.head is self.tail:
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.head
            self.head = self.head.next
            self.head.previous = None
            self.length -= 1
            return node

    def remove_tail(self):
        if self.head is None:
            raise ValueError("The List is empty")
        elif self.head is self.tail:
            node = self.tail
            self.head = None
            self.tail = None
            self.length = 0
            return node
        else:
            node = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            self.length -= 1
            return node
