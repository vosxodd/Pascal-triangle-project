import math
n = int(input('Сколько рядов в треугольнике Паскаля? '))
triangle_list = []
for n in range(n):
    line = [int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k))) for k in range(n + 1)]
    line_string = []
    for number in line:
        line_string.append(str(number))
    line_string = '  '.join(line_string)
    triangle_list.append(line_string)
print(triangle_list)

c = len(triangle_list[-1])
counter = 1
i = 0
for raw in triangle_list:
    if counter % 2 != 0:
        line_string = []
        for number in line:
        print(' ' * (c - i), triangle_list[i])
    elif counter % 2 == 0:
        print(' ' * (c - i - 1), triangle_list[i])
    i += 1
    counter += 1
