def euklid_simply(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a or b

def euklid_extended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        div, x, y = euklid_extended(b % a, a)
    return (div, y - (b // a) * x, x)

def euklid_binary(a, b):
    g = 1
    while a % 2 == 0 and b % 2 == 0:
        a = a // 2
        b = b // 2
        g = g * 2
    u, v = a, b
    while u != 0:
        if u % 2 == 0:
            u = u // 2
        if v % 2 == 0:
            v = v // 2
        if u >= v:
            u = u - v
        else:
            v = v - u
    d = g * v
    return d

def euklid_bin_extended(a, b):
    g = 1
    while a % 2 == 0 and b % 2 == 0:
        a = a // 2
        b = b // 2
        g = g * 2
    u = a
    v = b
    A = 1
    B = 0
    C = 0
    D = 1
    while u != 0:
        if u % 2 == 0:
            u = u // 2
            if A % 2 == 0 and B % 2 == 0:
                A = A // 2
                B = B // 2
            else:
                A = (A + b) // 2
                B = (B - a) // 2
        if v % 2 == 0:
            v = v // 2
            if C % 2 == 0 and D % 2 == 0:
                C = C // 2
                D = D // 2
            else:
                C = (C + b) // 2
                D = (D - a) // 2
        if u >= v:
            u = u - v
            A = A - C
            B = B - D
        else:
            v = v - u
            C = C - A
            D = D - B
    d = g * v
    x = C
    y = D
    return (d, x, y)
a = int(input("Введите первое число (a): "))
b = int(input("Введите второе число (b): "))

result1 = euklid_simply(a, b)
print(f"1. Простой алгоритм Евклида:")
print(f"   НОД({a}, {b}) = {result1}")


result2 = euklid_extended(a, b)
print(f"\n2. Расширенный алгоритм Евклида:")
print(f"   НОД({a}, {b}) = {result2[0]}")
print(f"   Коэффициенты: {a}*{result2[1]} + {b}*{result2[2]} = {result2[0]}")


result3 = euklid_binary(a, b)
print(f"\n3. Бинарный алгоритм Евклида:")
print(f"   НОД({a}, {b}) = {result3}")


result4 = euklid_bin_extended(a, b)
print(f"\n4. Расширенный бинарный алгоритм:")
print(f"   НОД({a}, {b}) = {result4[0]}")
print(f"   Коэффициенты: {a}*{result4[1]} + {b}*{result4[2]} = {result4[0]}")
