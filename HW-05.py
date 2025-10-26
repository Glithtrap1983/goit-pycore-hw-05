

# def caching_fibonacci():
#     cache = {}
    

#     def fibonacci(n):
#         if n <= 0: return 0
#         if n == 1: return 1
#         if n in cache: return cache[n]

#         cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         return cache[n]

#     return fibonacci


# # Отримуємо функцію fibonacci
# fib = caching_fibonacci()

# # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
# print(fib(10))  # Виведе 55
# print(fib(15))  # Виведе 610






# import re


# def generator_numbers(text):
#    num = re.findall(r'\d+\.\d+|\d+', text)
#    for n in num:
#       yield float(n)
# def sum_profit(text, func):
#    return sum(func(text))



# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")











def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

contacts = {}

@input_error
def add(args):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change(args):
    name, phone = args
    if name not in contacts: raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def phone(args):
    name = args[0]
    return f"{name}: {contacts[name]}"

def show_all():
    return "\n".join([f"{n}: {p}" for n, p in contacts.items()]) or "No contacts."

while True:
    cmd = input("Enter command: ").lower()
    if cmd in ["exit", "close"]: break
    elif cmd == "add": print(add(input("Enter name and phone: ").split()))
    elif cmd == "change": print(change(input("Enter name and new phone: ").split()))
    elif cmd == "phone": print(phone(input("Enter name: ").split()))
    elif cmd == "all": print(show_all())
    else: print("Unknown command.")
