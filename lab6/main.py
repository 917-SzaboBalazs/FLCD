from ll1 import Ll1

def main():
    input_file = "g1.txt"
    input_string = ""

    ll1 = Ll1(input_file=input_file)
    result = ll1.parse(input=input_string)

    non_terminals = ll1.grammar().get_nonterminals()

    print("Symbol\t\tFirst\t\tFollow")
    for symbol in non_terminals:
        print("{}\t\t{}\t\t{}".format(symbol, ll1.first(symbol), ll1.follow(symbol)))

    if result:
        print(f"Input string {input_string} is accepted by the grammar {input_file}")
    else:
        print(f"Input string {input_string} is NOT accepted by the grammar {input_file}")

if __name__ == "__main__":
    main()
