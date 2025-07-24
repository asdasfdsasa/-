import os
import math
import json

def f(x):
    try:
        return 100 * math.sqrt(abs(1 - 0.01 * x**2)) + 0.01 * (abs(x + 10))
    except ValueError:
        return float('nan')

start = -15
end = 5
step = 0.1

if not os.path.exists('results'):
    os.makedirs('results')

data = []
x = start
while x <= end:
    y = f(x)
    if not math.isnan(y):
        data.append({
            "x": round(x, 4),
            "y": round(y, 4)
        })
    x += step

output_file = os.path.join('results', 'result.json')
with open(output_file, 'w') as file:
    file.write('{\n  "data": [\n')
    for i, point in enumerate(data):
        line = '    ' + json.dumps(point, separators=(',', ':'))
        if i < len(data) - 1:
            line += ','
        file.write(line + '\n')

    file.write('  ]\n}')

print(f"Результаты сохранены в файл: {output_file}")

import matplotlib.pyplot as plt

x_values = [point["x"] for point in data]
y_values = [point["y"] for point in data]

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x) = 100√|1-0.01x²| + 0.01|x + 10|')
plt.title('График функции')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
