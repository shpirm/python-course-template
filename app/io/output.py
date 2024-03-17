def output_to_console(text):
    """
    Виводить текст у консоль.
    
    Параметри:
    - text: Текст, який потрібно вивести.
    """
    print(text)

def write_to_file_builtin(filename, text):
    """
    Записує текст до файлу, використовуючи вбудовані можливості Python.
    
    Параметри:
    - filename: Ім'я файлу, в який потрібно записати текст.
    - text: Текст, який потрібно записати.
    """
    with open(filename, "a") as file:
        file.write(text + "\n")
