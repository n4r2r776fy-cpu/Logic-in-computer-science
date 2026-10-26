def find_pattern_fibonacci(modulus, max_steps=1000):
    seq = [0, 1]
    for i in range(2, max_steps):
        next_val = (seq[i-1] + seq[i-2]) % modulus
        seq.append(next_val)
        # Перевірка на повторення початкового патерну [0, 1]
        if seq[i-1] == 0 and seq[i] == 1:
            return f"Знайдено період довжиною {i-1} для модуля {modulus}"
    return "Патерн не знайдено у заданих межах"

print(find_pattern_fibonacci(10)) # Шукаємо повторення останньої цифри