#Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.

num = int(input('Введите число '))
search = 1
power = -1
while search <= num:
    search *= 2
    power += 1
    print(power, end=' ')
print('\n')