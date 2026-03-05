def fibonacci(n, first = 0, second = 1):
    prev, curr = first, second
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

first = int(input("Введите 1е число: "))
second = int(input("Введите 2е число: "))
n = int(input("Введите номер члена последовательности: "))
res = fibonacci(n, first, second)

print(res)
