from symbolTable import SymbolTable
from pif import Pif
from tokenizer import Tokenizer
import re

class Scanner:

    def __init__(self, program_name) -> None:
        self.__program_name = program_name
        self.__operators = ["+", "-", "*", "/", "=", "<", ">=", "<=", "==", "!=", ">", "#", "(", ")", "[", "]", "{", "}", ":", ";"]
        self.__reserved_words = ['input', 'print', 'list', 'int', 'append', 'pop', 'if', 'else', 'while']
        self.__identifier_regex = r'\b[a-zA-Z][a-zA-Z0-9]*\b'
        self.__constant_regex = r'\b[-+]?[1-9][0-9]*\b|\b0\b'

        self.__symbolTable = SymbolTable()
        self.__pif = Pif()
        self.__tokenizer = Tokenizer(self.__operators, self.__program_name)

    def _is_operator_or_separator(self, token):
        return token in self.__operators

    def _is_keyword(self, token):
        return token in self.__reserved_words
    
    def _is_identifier(self, token):
        return bool(re.match(self.__identifier_regex, token))

    def _is_constant(self, token):
        return bool(re.match(self.__constant_regex, token))

    def scan(self):
        tokens = self.__tokenizer.get_tokens()
        lexical_erros = list()

        for token in tokens:
            
            if self._is_operator_or_separator(token) or self._is_keyword(token):
                self.__pif.add(token, -1)

            elif self._is_identifier(token) or self._is_constant(token):
                st_pos = self.__symbolTable.find_by_value(token)
                
                if st_pos is None:
                    pos = self.__symbolTable.size()
                    self.__symbolTable.insert(pos, token)

                else:
                    pos = st_pos[0]

                if self._is_identifier(token):
                    self.__pif.add("id", pos)
                else:
                    self.__pif.add("const", pos)
                    
            else:
                lexical_erros.append(token)

        print(f"lexical error - {lexical_erros[0]}" if len(lexical_erros) > 0 else "lexically correct")

    def log_to_file(self):
        with open("pif.out", "w") as file:
            print("token | ST_pos", file=file)

            for token, pos in self.__pif.get_all():
                print(f"{token} | {pos}", file=file)

        with open("st.out", "w") as file:
            print("ST_pos | symbol", file=file)

            for pos, symbol in self.__symbolTable.get_all():
                print(f"{pos} | {symbol}", file=file)




