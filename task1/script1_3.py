#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys

def circular_array_path(n, m):
    result = []
    current_index = 0
    for _ in range(n):
        result.append(current_index + 1)
        current_index = (current_index - 1 + m) % n
        if current_index == 0:
            break
    return result

if __name__ == "__main__":
    # Фильтрация только числовых аргументов
    args = [arg for arg in sys.argv[1:] if arg.isdigit()]
    
    if len(args) < 2:
        print("Нужно ввести два числовых аргумента: n и m")
    else:
        n = int(args[0])
        m = int(args[1])

        path = circular_array_path(n, m)
        print("".join(map(str, path)))


# In[ ]:




