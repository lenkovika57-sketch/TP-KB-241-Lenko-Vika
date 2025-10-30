print("\nТестування функцій списків")

list = [9, 1, 2, 8, 10, 3]
print("Початковий список:", list)

list.append(4)
print("append(4):", list)

list.extend([5, 6])
print("extend([5, 6]):", list)

list.insert(2, 99)
print("insert(2, 99):", list)

list.remove(99)
print("remove(99):", list)

list.sort()
print("sort():", list)

list.reverse()
print("reverse():", list)

copy_list = list.copy()
print("copy():", copy_list)

list.clear()
print("clear():", list)