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
        productions = self.gramamr.get_productions().get_all()
        follow_col = dict()

        for symbol in non_terminals:
            follow_col[symbol] = ""

        # TODO: FILL THE `follow_col` dictionary

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
