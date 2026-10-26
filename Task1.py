import multiprocessing
import time

def finite_program():
    time.sleep(2)
    return "Програма успішно завершилась"

def infinite_program():
    while True:
        pass

def run_with_timeout(func, timeout=10):
    process = multiprocessing.Process(target=func)
    process.start()
    process.join(timeout)
    
    if process.is_alive():
        process.terminate()
        process.join()
        return "Помилка: Програма не завершилась (Timeout)"
    return "Успіх: Програма завершилась вчасно"

# Тестування
if __name__ == '__main__':
    print("Тест 1 (скінченна):", run_with_timeout(finite_program))
    print("Тест 2 (нескінченна):", run_with_timeout(infinite_program))