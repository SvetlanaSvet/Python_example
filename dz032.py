# Требуется найти в списке самый близкий по величине элемент
# к заданному числу k и вывести его.

lst = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
x = 10

min = abs(lst[0] - x)
index = 0

for i in range(1, len(lst)):
    diff = abs(lst[i] - x)
    if diff < min:
        min = diff
        index = i
        
print(lst[index])