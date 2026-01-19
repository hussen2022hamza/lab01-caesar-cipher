import random

def fermat_test(n, trials=5):
    if n < 5:
        return False
    if n % 2 == 0:
        return False
    
    for _ in range(trials):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def jacobi_symbol(a, n):
    if a == 0:
        return 0
    if a == 1:
        return 1
    
    result = 1
    if a < 0:
        a = -a
        if n % 4 == 3:
            result = -result
    
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    
    return result if n == 1 else 0

def solovay_strassen_test(n, trials=5):
    if n < 5:
        return False
    if n % 2 == 0:
        return False
    
    for _ in range(trials):
        a = random.randint(2, n - 2)
        x = pow(a, (n - 1) // 2, n)
        if x == 0 or x != (n + jacobi_symbol(a, n)) % n:
            return False
    return True

def miller_rabin_test(n, trials=5):
    if n < 5:
        return False
    if n % 2 == 0:
        return False
    
    s, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    
    for _ in range(trials):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        composite = True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                composite = False
                break
        
        if composite:
            return False
    
    return True

def test_number(n):
    print(f"Тестируем число: {n}")
    print(f"Ферма: {'Простое' if fermat_test(n) else 'Составное'}")
    print(f"Соловэй-Штрассен: {'Простое' if solovay_strassen_test(n) else 'Составное'}")
    print(f"Миллер-Рабин: {'Простое' if miller_rabin_test(n) else 'Составное'}")
    print()

if __name__ == "__main__":
    test_numbers = [17, 25, 97, 100, 561]
    for num in test_numbers:
        test_number(num)