from ll1 import Ll1

def main():
    input_file = "g1.txt"
    input_string = "abcc$"

    ll1 = Ll1(input_file=input_file)
    result = ll1.parse(input=input_string)

    print(ll1.get_parsed_table())

    if result:
        print(f"Input string {input_string} is accepted by the grammar {input_file}")
    else:
        print(f"Input string {input_string} is not accepted by the grammar {input_file}")

if __name__ == "__main__":
    main()
