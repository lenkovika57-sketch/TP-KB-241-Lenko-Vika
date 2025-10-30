def find_insert_position(sorted_list, new_value):
    for i, val in enumerate(sorted_list):
        if new_value < val:
            return i
    return len(sorted_list)  

numbers = [1, 3, 5, 7, 9]
print("Початковий список:", numbers)

new_num = int(input("Введіть число для вставки: "))
pos = find_insert_position(numbers, new_num)

numbers.insert(pos, new_num)
print("Новий список:", numbers)