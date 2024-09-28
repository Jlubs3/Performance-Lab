import json
import sys

def load_json_file(file_path):
    """Функция для чтения JSON файла."""
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json_file(data, file_path):
    """Функция для записи данных в JSON файл."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def build_value_map(values_data):
    """Создает словарь для быстрого поиска значений по id из values.json."""
    return {item['id']: item['value'] for item in values_data['values']}

def update_tests_with_values(tests, value_map):
    """Рекурсивно обновляет тесты из tests.json с соответствующими значениями из value_map."""
    for test in tests:
        test_id = test.get('id')
        if test_id in value_map:
            test['value'] = value_map[test_id]
        
        # Если у теста есть вложенные тесты (children), обработать их рекурсивно
        if 'children' in test:
            update_tests_with_values(test['children'], value_map)

def main():
    # Проверка количества аргументов
    if len(sys.argv) != 4:
        print("Usage: python program.py <values.json> <tests.json> <report.json>")
        sys.exit(1)
    
    # Получаем пути к файлам из аргументов командной строки
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]
    
    # Чтение входных файлов
    values_data = load_json_file(values_file)
    tests_data = load_json_file(tests_file)
    
    # Создание карты соответствий id -> value
    value_map = build_value_map(values_data)
    
    # Обновление структуры tests значениями из value_map
    update_tests_with_values(tests_data['tests'], value_map)
    
    # Сохранение обновленных данных в файл report.json
    save_json_file(tests_data, report_file)

if __name__ == "__main__":
    main()
