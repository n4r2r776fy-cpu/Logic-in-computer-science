def turing_machine_infinite_loop():
    tape = [0, 0, 0, 0, 0]
    head = 2
    state = 'A'
    steps = 0
    
    # Правила: (поточний_стан, поточний_символ) -> (новий_стан, новий_символ, рух)
    rules = {
        ('A', 0): ('B', 1, 1),  # Рух вправо (1)
        ('B', 0): ('A', 1, -1), # Рух вліво (-1)
        ('A', 1): ('B', 0, 1),
        ('B', 1): ('A', 0, -1)
    }
    
    while steps < 20: # Штучне обмеження кроків для візуалізації
        symbol = tape[head]
        new_state, new_symbol, move = rules.get((state, symbol), ('HALT', symbol, 0))
        
        if new_state == 'HALT':
            print("Машина зупинилася.")
            break
            
        tape[head] = new_symbol
        head += move
        state = new_state
        steps += 1
        print(f"Крок {steps}: Стрічка {tape}, Стан {state}, Головка на {head}")

turing_machine_infinite_loop()