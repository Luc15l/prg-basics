import queue
stack = queue.LifoQueue()


stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(17)
x = stack.get()
y = stack.get()
print(x+y)
wynik = 0
while not stack.empty():
    wynik += stack.get()

print("Sum of remaining stack elements:", wynik)
