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

for raw in triangle_list:
    print(raw.center(100))
