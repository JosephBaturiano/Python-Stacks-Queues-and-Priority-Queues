from thirdqueues import Stack

lifo = Stack("1st", "2nd", "3rd")
print("Nos of stack:", len(lifo))

for element in lifo:
    print(element)

print("Current number of stack:", len(lifo))
