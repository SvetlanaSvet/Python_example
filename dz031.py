# Вычислить сколько раз встречается k в списке.

list_1 = [3, 5, 3, 3, 5, 3]
k = 5

print(list_1.count(k))

# вариант без метода
count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)