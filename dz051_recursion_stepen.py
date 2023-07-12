# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def recursion_stepen(a, b):
    if b == 0:  return 1
    elif b == 1: return a
    else:
        return a * recursion_stepen(a, b-1)
    
a = int(input('Введите число: '))
b = int(input('Введите степень числа: '))
print(recursion_stepen(a,b))