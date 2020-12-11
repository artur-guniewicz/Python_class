from Zestaw9.double_list import Node, DoubleList

L = DoubleList()

print(L)

L.insert_tail(Node(6))
L.insert_tail(Node(3))
L.insert_tail(Node(1))
L.insert_tail(Node(0))
L.insert_tail(Node(26))
L.insert_tail(Node(7))
L.insert_tail(Node(2))
L.insert_tail(Node(11))

print(L)

L.remove(Node(1))

print(L)

L.remove(Node(26))

print(L)

print("MIN:", L.find_min())
print("MAX:", L.find_max())
print("Is empty? ->", L.is_empty())

L.clear()
print("Is empty after clear? ->", L.is_empty())
