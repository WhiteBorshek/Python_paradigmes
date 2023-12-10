def sum_list(lst):
    if not lst:
        return 0  # Сумма пустого списка равна 0
    else:
        return lst[0] + sum_list(lst[1:])

# Пример использования:
my_list = [1, 2, 3, 4, 5]
result = sum_list(my_list)
print(f"Результат: {result}")
