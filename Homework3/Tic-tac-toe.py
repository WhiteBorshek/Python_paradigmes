from math import sqrt

def mean(values):
    return sum(values) / len(values)

def pearson_correlation(x, y):
    n = len(x)
    mean_x, mean_y = mean(x), mean(y)

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator_x = sqrt(sum((x[i] - mean_x)**2 for i in range(n)))
    denominator_y = sqrt(sum((y[i] - mean_y)**2 for i in range(n)))

    correlation = numerator / (denominator_x * denominator_y) if denominator_x * denominator_y != 0 else 0
    return correlation

# Пример использования:
array_x = [1, 2, 3, 4, 5]
array_y = [2, 4, 5, 4, 5]

correlation = pearson_correlation(array_x, array_y)
print(f"Корреляция Пирсона: {correlation}")
