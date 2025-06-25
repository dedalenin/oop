def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} вызвана с аргументами: {args}")
        return func(*args, **kwargs)
    return wrapper

def limit_calls(max_times):
    def decorator(func):
        call_count = 0
        def wrapper(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count > max_times:
                return "Превышен лимит вызовов!"
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Применяем оба декоратора (порядок важен!)
@limit_calls(max_times=3)
@log_calls
def greet(name):
    return f"Привет, {name}!"

# Тестируем
print(greet("Алиса"))  # OK
print(greet("Боб"))    # OK
print(greet("Чарли"))  # OK
print(greet("Дэвид"))  # Лимит