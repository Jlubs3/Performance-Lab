#!/usr/bin/env python
# coding: utf-8
def circular_array_path(n, m):
    result = []
    current_index = 0
    for _ in range(n):
        result.append(current_index + 1)
        current_index = (current_index-1 + m) % n
        if current_index == 0:
            break
    return result

if __name__ == "__main__":
    n = 5  # Пример значения n
    m = 4  # Пример значения m

    path = circular_array_path(n, m)
    print("".join(map(str, path)))
