import json
import sys

def load_json_file(filepath):
    """Функция для загрузки JSON файла."""
    with open(filepath, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {filepath}: {e}")
            sys.exit(1)

def save_json_file(filepath, data):
    """Функция для сохранения данных в JSON файл."""
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def fill_values(test_structure, values_map):
    """Рекурсивная функция для заполнения полей 'value' на основе 'id'."""
    # Заполняем поле value, если найден id в values_map
    if 'id' in test_structure:
        test_id = test_structure['id']
        if test_id in values_map:
            test_structure['value'] = values_map[test_id]
    
    # Обрабатываем вложенные структуры, если они есть
    if 'tests' in test_structure:
        for sub_test in test_structure['tests']:
            fill_values(sub_test, values_map)
    
    # Также обрабатываем вложенные структуры с ключом 'values'
    if 'values' in test_structure:
        for sub_test in test_structure['values']:
            fill_values(sub_test, values_map)

    return test_structure

def main():
    # Проверка, что переданы три пути к файлам
    if len(sys.argv) != 4:
        print("Usage: python script.py <values.json> <tests.json> <report.json>")
        return
    
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    # Чтение данных из файлов
    values_data = load_json_file(values_file)
    tests_data = load_json_file(tests_file)

    # Достаем список из ключа 'values'
    if 'values' not in values_data or not isinstance(values_data['values'], list):
        print(f"Expected 'values' key with a list in {values_file}")
        sys.exit(1)

    values_list = values_data['values']

    # Преобразуем список с данными о значениях в словарь для удобного поиска по id
    try:
        values_map = {item['id']: item['value'] for item in values_list}
    except KeyError as e:
        print(f"Missing key in values_data: {e}")
        sys.exit(1)

    # Рекурсивное заполнение полей 'value' в структуре tests.json
    filled_report = fill_values(tests_data, values_map)

    # Сохранение результата в report.json
    save_json_file(report_file, filled_report)

if __name__ == "__main__":
    main()
