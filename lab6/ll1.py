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
        self.table.append(first_column)

        follow_column = self.__build_follow()
        self.table.append(follow_column)

    def __build_first(self):
        non_terminals = self.gramamr.get_nonterminals()
        terminals = self.gramamr.get_terminals()
        productions = self.gramamr.get_productions().get_all()
        first_col = dict()

        for symbol in non_terminals:
            first_col[symbol] = set()

        for lhs, rhs in reversed(productions.items()):
            for rule in rhs:
                if rule[0] in terminals:
                    first_col[lhs[0]] = first_col[lhs[0]].union(rule[0])

                elif rule[0] in non_terminals:
                    first_col[lhs[0]] = first_col[lhs[0]].union(first_col[rule[0]])

                else:
                    raise ValueError("Invalid symbol in production rule: {}".format(rule[0]))

        return first_col

    def __build_follow(self):
        non_terminals = self.gramamr.get_nonterminals()
        terminals = self.gramamr.get_terminals()
        productions = self.gramamr.get_productions().get_all()
        first_col = self.table[0]
        follow_col = dict()

        for symbol in non_terminals:
            follow_col[symbol] = set()

        follow_col[self.gramamr.get_input_symbol()] = set('$')

        for key in productions.keys():

            for lhs, rhs in productions.items():
                for rule in rhs:
                    for i in range(len(rule)):
                        symbol = rule[i]

                        if symbol == key[0]:

                            if i == len(rule) - 1:
                                follow_col[symbol] = follow_col[symbol].union(follow_col[lhs[0]])

                            elif rule[i + 1] in terminals:
                                follow_col[symbol] = follow_col[symbol].union([rule[i + 1]])

                            elif rule[i + 1] in non_terminals:
                                follow_col[symbol] = follow_col[symbol].union(first_col[rule[i + 1]])
                            
                            else:
                                raise ValueError("Invalid symbol in production rule: {}".format(rule[i + 1]))

        return follow_col
