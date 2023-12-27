from grammar import Grammar
from ll1 import Ll1

def test(parser):
    print(parser.get_grammar().get_productions())

    print("{:<6} | {:<20} | {:<12}".format("Symbol", "First", "Follow"))  # Align the column headers

    for symbol in parser.get_grammar().get_nonterminals():
        first = parser.first(symbol)
        follow = parser.follow(symbol)
        
        print("{:<6} | {:<20} | {:<12}".format(symbol, str(first), str(follow)))  # Convert first and follow sets to strings before formatting


if __name__ == "__main__":
    grammar = Grammar(input_file="g1.txt")
    parser = Ll1(grammar=grammar)

    test(parser)
