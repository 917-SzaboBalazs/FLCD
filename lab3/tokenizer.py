def read_program(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    return lines

def strip_newlines(lines):
    return [line.rstrip() for line in lines if len(line.rstrip()) > 0]

def remove_whitespaces(lines):
    return [line.replace(" ", "") for line in lines if not line.replace(" ", "")[0] == "#"]

def tokenizer():
    tokens = list()

    # Read the program
    lines = read_program("program.txt")

    # Clear empty rows
    lines = strip_newlines(lines=lines)

    # Remove whitespaces and comments
    lines = remove_whitespaces(lines=lines)

    tokens = lines

    return tokens

for i in tokenizer():
    print(i)
