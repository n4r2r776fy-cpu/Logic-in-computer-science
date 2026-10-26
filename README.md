import multiprocessing
import time


# ==============================================================================
# ЗАВДАННЯ 1: Створення програми для аналізу власного коду (Ілюстрація проблеми зупинки)
# ==============================================================================

def target_program_finite():
    """Приклад програми, яка гарантовано завершується."""
    print("  [Цільова програма] Виконуються обчислення...")
    time.sleep(2)  # Імітація роботи протягом 2 секунд
    return "Завершено успішно"


def target_program_infinite():
    """Приклад програми, яка застрягає в нескінченному циклі."""
    print("  [Цільова програма] Запуск нескінченного циклу...")
    while True:
        time.sleep(0.5)


def run_with_timeout(func, timeout_seconds=10):
    """
    Аналізатор: приймає функцію та намагається визначити,
    чи завершиться вона за timeout_seconds.
    """
    process = multiprocessing.Process(target=func)
    process.start()

    # Очікуємо виконання фіксований час
    process.join(timeout_seconds)

    if process.is_alive():
        # Якщо програма все ще виконується — примусово завершуємо
        process.terminate()
        process.join()
        return f"РЕЗУЛЬТАТ: Програма не завершилася протягом {timeout_seconds} секунд (зупинено примусово)."
    else:
        return "РЕЗУЛЬТАТ: Програма успішно завершила роботу вчасно."


# ==============================================================================
# ЗАВДАННЯ 2: Пошук шаблонів у нескінченних послідовностях
# ==============================================================================

def find_pisano_period(modulus, max_search_steps=10000):
    """
    Алгоритм пошуку патерну (періоду Пізано) для остач від ділення
    послідовності Фібоначчі на число modulus.
    """
    a, b = 0, 1
    sequence = [a, b]

    for step in range(2, max_search_steps):
        a, b = b, (a + b) % modulus
        sequence.append(b)

        # Перевірка на початок нового періоду (період завжди починається з 0, 1)
        if sequence[-2] == 0 and sequence[-1] == 1:
            period_length = step - 1
            return period_length, sequence[:-2]

    return None, sequence


# ==============================================================================
# ЗАВДАННЯ 3: Моделювання Машини Тьюрінга (Візуалізація алгоритмічної нерозв'язності)
# ==============================================================================

class TuringMachine:
    def __init__(self, tape_content, initial_state, transition_rules, max_steps=100):
        self.tape = list(tape_content)
        self.head_position = 0
        self.state = initial_state
        self.rules = transition_rules
        self.max_steps = max_steps
        self.step_count = 0

    def step(self):
        if self.state == 'HALT':
            return False

        current_symbol = self.tape[self.head_position]
        key = (self.state, current_symbol)

        if key not in self.rules:
            self.state = 'HALT'
            return False

        new_state, write_symbol, direction = self.rules[key]

        # Запис символу
        self.tape[self.head_position] = write_symbol
        # Зміна стану
        self.state = new_state

        # Зсув головки (R = +1, L = -1, N = 0)
        if direction == 'R':
            self.head_position += 1
            if self.head_position >= len(self.tape):
                self.tape.append('_')  # Розширення стрічки вправо
        elif direction == 'L':
            self.head_position -= 1
            if self.head_position < 0:
                self.tape.insert(0, '_')  # Розширення стрічки вліво
                self.head_position = 0

        self.step_count += 1
        return True

    def run(self):
        print(f"Початковий стан: стрічка={''.join(self.tape)}, стан={self.state}")
        while self.step_count < self.max_steps:
            tape_str = "".join(self.tape)
            head_str = " " * self.head_position + "^"
            print(f"Крок {self.step_count:2d} | Стрічка: {tape_str} | Стан: {self.state}")

            if not self.step():
                break

        if self.state == 'HALT':
            print(f"Машина зупинилася на кроці {self.step_count}. Підсумкова стрічка: {''.join(self.tape)}")
        else:
            print(f"Досягнуто ліміту кроків ({self.max_steps}). Машина застрягла в нескінченному циклі!")


# ==============================================================================
# ГОЛОВНИЙ БЛОК ВИКОНАННЯ
# ==============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("ЗАВДАННЯ 1: Симуляція Проблеми Зупинки")
    print("=" * 70)

    print("\n[Тест 1] Запуск скінченної програми:")
    res1 = run_with_timeout(target_program_finite, timeout_seconds=5)
    print(res1)

    print("\n[Тест 2] Запуск нескінченної програми:")
    res2 = run_with_timeout(target_program_infinite, timeout_seconds=5)
    print(res2)

    print("\nОбговорення (Завдання 1.3):")
    print("- Обмеження: Використання тайм-ауту — це лише евристика.")
    print("- Якщо програма працює довше 5 секунд, це не доводить, що вона працюватиме вічно.")
    print("- Математично доведено (Алан Тьюрінг, 1936), що створити універсальну програму-аналізатор")
    print("  для будь-якої довільної програми НЕМУЖЛИВО через парадокс самопосилання.")

    print("\n" + "=" * 70)
    print("ЗАВДАННЯ 2: Пошук патернів у нескінченних послідовностях")
    print("=" * 70)

    mod = 10
    length, seq = find_pisano_period(modulus=mod)
    print(f"Пошук циклу в остачах Фібоначчі за модулем {mod}:")
    print(f"Довжина патерну (Період Пізано): {length}")
    print(f"Перші 20 елементів остач: {seq[:20]}...")

    print("\nОбговорення (Завдання 2.2 - 2.3):")
    print("- Чому завдання нерозв'язне загалом: Для довільної нескінченної послідовності")
    print("  неможливо перевірити нескінченну кількість елементів за скінченний час.")
    print("- Практичні рішення: У машинному навчанні та аналізі даних (NLP, аудіо)")
    print("  використовують не абсолютні доведення, а ймовірнісні апроксимації (RNN, Transformers, FFT),")
    print("  працюючи з фіксованими вікнами даних.")

    print("\n" + "=" * 70)
    print("ЗАВДАННЯ 3: Моделювання Машини Тьюрінга")
    print("=" * 70)

    # Правила для машини, яка входить у нескінченний цикл (хитається вліво-вправо)
    # Формат правил: (поточний_стан, прочитаний_символ): (новий_стан, записаний_символ, напрямок)
    loop_rules = {
        ('q0', '1'): ('q1', '1', 'R'),
        ('q1', '_'): ('q0', '_', 'L'),
    }

    print("Запуск Машини Тьюрінга з нескінченним циклом:")
    tm = TuringMachine(tape_content="1_", initial_state='q0', transition_rules=loop_rules, max_steps=10)
    tm.run()

    print("\nОбговорення (Завдання 3.3):")
    print("- Проблема зупинки Машини Тьюрінга: Машина Тьюрінга виконує інструкції локально.")
    print("- Вона не має глобального механізму аналізу свого майбутнього стану.")
    print("- Спроба побудувати супер-машину, яка б перевіряла інші машини, призводить до того,")
    print("  що сам перевіряльник зациклюється при спробі змоделювати нескінченний процес.")