class Ll1:

    def __init__(self, grammar):
        self.gramamr = grammar
        self.table = list()

        self.__build_table()

    def get_grammar(self):
        return self.gramamr

    def first(self, S):
        return self.table[0][S]

    def follow(self, S):
        return self.table[1][S]
    
    def __build_table(self):
        first_column = self.__build_first()
        follow_column = self.__build_follow()

        self.table.append(first_column)
        self.table.append(follow_column)

    def __build_first(self):
        non_terminals = self.gramamr.get_nonterminals()
        productions = self.gramamr.get_productions().get_all()
        first_col = dict()

        for symbol in non_terminals:
            first_col[symbol] = ""

        for key, value in reversed(productions.items()):
            first_terminal = self.__get_first_terminals(rhs=value)
            
            if len(first_terminal) > 0:
                first_col[key[0]] = str(first_terminal)
            else:
                first_col[key[0]] = first_col[value[0][0]]

        return first_col

    def __build_follow(self):
        non_terminals = self.gramamr.get_nonterminals()
        follow_col = {symbol: set() for symbol in non_terminals}

        start_symbol = self.gramamr.get_input_symbol()
        follow_col[start_symbol] = {'$'}

        productions = self.gramamr.get_productions().get_all()

        while True:
            prev_follow_col = {k: set(v) for k, v in follow_col.items()}

            for key, value in productions.items():
                for i, symbol in enumerate(value):
                    if symbol in non_terminals:
                        next_symbols = value[i + 1:] if i + 1 < len(value) else []
                        first_of_next = self.__get_first_terminals(next_symbols)

                        follow_col[symbol] |= first_of_next - {''}

                        if '' in first_of_next:
                            follow_col[symbol] |= follow_col[key[0]]

                        if i + 1 < len(value) and value[i + 1] in non_terminals:
                            follow_col[value[i + 1]] |= follow_col[symbol]

            if prev_follow_col == follow_col:
                break

        follow_col = {k: list(v) for k, v in follow_col.items()}

        print("Follow sets during computation:")
        for symbol, follow_set in follow_col.items():
            print(f"{symbol}: {follow_set}")

        return follow_col


    def __get_first_terminals(self, rhs):
        terminals = self.gramamr.get_terminals()
        result = list()

        for r in rhs:
            for symbol in r:
                if symbol in terminals:
                    result.append(symbol)
                    break
        
        return result
