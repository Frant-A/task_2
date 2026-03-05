def merge_sorted(list1, list2):
    sum = list1 + list2
    for i in sum:
        k = int(i)
        both.append(k)

    for i in range(len(both)):
        for j in range(i + 1, len(both)):
            if both[i] > both[j]:
                min = both[i]
                both[i] = both[j]
                both[j] = min
    return both
both = []
a = input("Введите целые числа в строку через пробел:\n")
b = input("Введите целые числа в строку через пробел:\n")

list1 = a.split()
list2 = b.split()

result = merge_sorted(list1, list2)
print(result)


