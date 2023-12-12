from grammar import Grammar
from ll1 import Ll1

if __name__ == "__main__":
    grammar = Grammar(input_file="g1.txt")
    parser = Ll1(grammar=grammar)

    
