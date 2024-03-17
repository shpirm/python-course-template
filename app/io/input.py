import pandas as pd

def input_from_console():
    """
    Запитує та повертає текст, введений користувачем з консолі.
    """
    return input("Введіть текст: ")

def read_from_file_builtin(filename):
    """
    Зчитує та повертає вміст файлу, використовуючи вбудовані можливості Python.
    
    Параметри:
    - filename: Ім'я файлу, з якого потрібно зчитати дані.
    """
    with open(filename, "r") as file:
        return file.read()

def read_from_file_pandas(filename):
    """
    Зчитує та повертає вміст файлу, використовуючи бібліотеку pandas.
    
    Параметри:
    - filename: Ім'я файлу, з якого потрібно зчитати дані.
    """
    return pd.read_csv(filename, header=None).to_string(index=False, header=False)
