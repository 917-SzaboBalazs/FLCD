import re

class Tokenizer:

    def __init__(self, split_symbols, program_name=None) -> None:
        self.__lines = None
        self.__split_symbols = split_symbols
        self.__program_name = program_name
        

    def read_program(self, program_name):
        self.__program_name = program_name

        if self.__lines is not None:
            self.__lines.clear()

        if self.__program_name is None:
            raise ValueError("Input program is missing")
        
        with open(self.__program_name) as file:
            self.__lines = file.readlines()

    def _strip_newlines(self):
        if self.__lines is not None:
            self.__lines = [line.rstrip() for line in self.__lines if len(line.rstrip()) > 0]

    def _remove_whitespaces(self):
        if self.__lines is not None:
            self.__lines = [line.replace(" ", "") for line in self.__lines if not line.replace(" ", "")[0] == "#"]

    def _tokenize(self):
        tokens = []

        if self.__lines is not None:
            operators_pattern = '|'.join(re.escape(operator) for operator in self.__split_symbols)
            rest_of_pattern = r"\w+|\s+"
            pattern = f"({operators_pattern}|{rest_of_pattern})"

            for line in self.__lines:
                line_tokens = re.findall(pattern, line)
                tokens.extend(line_tokens)

        return tokens

    def get_tokens(self):

        # Read the program
        self.read_program(self.__program_name)

        # Clear empty rows
        self._strip_newlines()

        # Remove whitespaces and comments
        self._remove_whitespaces()

        # Get all tokens
        tokens = self._tokenize()

        return tokens
