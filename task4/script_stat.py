import sys
import statistics

def min_moves_to_equal_elements(nums):
    # Находим медиану массива
    median = int(statistics.median(nums))
    
    # Подсчитываем количество ходов для приведения всех элементов к медиане
    moves = sum(abs(num - median) for num in nums)
    
    return moves

def main():
    # Получаем имя файла из аргументов командной строки
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        return
    
    filename = sys.argv[1]
    
    try:
        # Чтение чисел из файла
        with open(filename, 'r') as file:
            nums = [int(line.strip()) for line in file]
        
        # Вывод минимального количества ходов
        print(min_moves_to_equal_elements(nums))
        
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print("File contains non-integer values.")

if __name__ == "__main__":
    main()

