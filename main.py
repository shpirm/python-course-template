from app.io.input import input_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_to_console, write_to_file_builtin

def main():
    data_source = 'data/'

    input_text = input_from_console()
    output_to_console(input_text)
    write_to_file_builtin(data_source + "output_console.txt", input_text)

    # builtin Python
    text_from_file_builtin = read_from_file_builtin(data_source + "input.txt")
    output_to_console(text_from_file_builtin)
    write_to_file_builtin(data_source + "output_txt.txt", text_from_file_builtin)

    # pandas
    text_from_file_pandas = read_from_file_pandas(data_source + "input.csv")
    output_to_console(text_from_file_pandas)
    write_to_file_builtin(data_source + "output_csv.txt", text_from_file_pandas)

if __name__ == "__main__":
    main()
