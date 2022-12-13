from secondqueues import Queue

fifo = Queue("1st", "2nd", "3rd")
print("In queue:", len(fifo))

for element in fifo:
    print(element)
