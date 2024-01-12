Github: https://github.com/917-SzaboBalazs/FLCD/tree/main/lab6
Made by: Tankó-Gábor Tamás and Szabó Balázs


Method: __init__(self, parsing_table)
This is the constructor method for the ParserOutput class. It initializes the parsing table and its representation.

Method: transform_parsing_table_into_representation(self)
This method transforms the parsing table into a list of tuples, where each tuple represents a rule in the parsing table.

Method: print_to_screen(self)
This method prints the representation of the parsing table to the screen.

Method: print_to_file(self, filename)
This method writes the representation of the parsing table to a file.

Method: __build_parsing_table(self)
This method is used to build the parsing table for the parser. It iterates over the non-terminals and terminals in the grammar, and fills the parsing table according to the productions in the grammar.