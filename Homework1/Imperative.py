def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

# Пример использования:
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = sort_list_imperative(numbers)
print("Отсортированный по убыванию список:", sorted_numbers)
