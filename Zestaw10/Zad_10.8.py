from random_queue import RandomQueue

randomQueue = RandomQueue()

for i in range(10):
    randomQueue.insert(i)
print(randomQueue)

while not randomQueue.is_empty():
    print(randomQueue.remove())