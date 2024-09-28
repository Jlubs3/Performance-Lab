import sys
import math

def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        x, y = map(float, file.readline().split())  # Чтение координат центра
        r = float(file.readline().strip())  # Чтение радиуса
    return x, y, r

def read_points_data(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            points.append(tuple(map(float, line.split())))  # Чтение координат точек
    return points

def calculate_position(x_center, y_center, radius, points):
    results = []
    for x, y in points:
        distance = math.sqrt((x - x_center)**2 + (y - y_center)**2)  # Вычисляем расстояние до центра
        if math.isclose(distance, radius, rel_tol=1e-9):  # Проверка, лежит ли точка на окружности
            results.append(0)
        elif distance < radius:
            results.append(1)  # Точка внутри окружности
        else:
            results.append(2)  # Точка снаружи окружности
    return results

def main():
    # Получаем аргументы командной строки
    if len(sys.argv) != 3:
        print("Usage: python program.py <circle_file> <points_file>")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    # Чтение данных
    x_center, y_center, radius = read_circle_data(circle_file)
    points = read_points_data(points_file)

    # Расчет положения точек
    results = calculate_position(x_center, y_center, radius, points)

    # Вывод результатов
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
