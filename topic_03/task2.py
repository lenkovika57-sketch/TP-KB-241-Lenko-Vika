print("\nТестування функцій списку")

nums = [1, 2, 3, 4, 5]
print("Початковий список:", nums)

nums.append(6)
print("append(6):", nums)

nums.extend([7, 8])
print("extend([7, 8]):", nums)

nums.insert(3, 20)
print("insert(3, 20):", nums)

nums.remove(20)
print("remove(20):", nums)

nums_copy = nums.copy()
print("copy():", nums_copy)

nums.reverse()
print("reverse():", nums)

nums.sort()
print("sort():", nums)

nums.clear()
print("clear():", nums)