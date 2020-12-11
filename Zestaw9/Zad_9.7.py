from Zestaw9.bst import *

T = Node(78)
T.insert(Node(64))
T.insert(Node(98))
T.insert(Node(45))
T.insert(Node(111))
T.insert(Node(34))
T.insert(Node(187))
T.insert(Node(23))
T.insert(Node(57))
T.insert(Node(4))
T.insert(Node(57))
T.insert(Node(90))
T.insert(Node(123))
T.insert(Node(15))

print("MIN:", bst_min(T))
print("MAX:", bst_max(T))
