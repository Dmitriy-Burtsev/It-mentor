from random import randint
'''6.1 бинарный поиск
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + right // 2  # Находим середину


        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Если элемент не найден

my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

result = binary_search(my_array, target)

if result != -1:
    print(f"Элемент {target_value} найден на индексе {result}.")
else:
    print(f"Элемент {target_value} не найден в массиве.")'''

6.2
N = 10

a = [randint(1, 99) for n in range(N)]
print(a)

i = 0
while i < N-1:
    j = 0
    while j < N-1:
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
        j += 1
    i += 1

print(a)