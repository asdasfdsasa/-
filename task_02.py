import argparse
import json
import matplotlib.pyplot as plt
import sys
import os

def main():
    parser = argparse.ArgumentParser(description='Построение графика')
    parser.add_argument(
        'input_file',
        nargs='?',
        help='Путь к JSON файлу',
        default='result.json'
    )
    parser.add_argument('--thin', type=int, default=1)

    args = parser.parse_args()

    try:
        with open(args.input_file) as f:
            data = json.load(f)['data']

        x = [p['x'] for p in data[::args.thin]]
        y = [p['y'] for p in data[::args.thin]]

        plt.figure(figsize=(10, 6))
        plt.plot(x, y)
        plt.title('График функции')
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()