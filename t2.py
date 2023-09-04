# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

sum = int(input('Сумма чисел х и у равна '))
prod = int(input('Произведение чисел х и у равно '))
x, y = 0, 0
for x in range(1001):
    y = sum - x
    if x + y == sum and x * y == prod:
        print(f'x = {x}, y = {y}')