from grammar import Grammar
from ll1 import Ll1

def test(parser):
    print("Symbol | First       | Follow")

    for symbol in parser.get_grammar().get_nonterminals():
        first = parser.first(symbol)
        follow = parser.follow(symbol)
        print(f"{symbol:<6} | {first:<11} | {follow}")


if __name__ == "__main__":
    grammar = Grammar(input_file="g1.txt")
    parser = Ll1(grammar=grammar)

    test(parser)
