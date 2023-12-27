from grammar import Grammar

class Ll1:

    def __init__(self, input_file):
        self.__grammar = Grammar(input_file=input_file)
        self.__first_col = dict()
        self.__follow_col = dict()
        self.__parsing_table = dict()

        self.__build_table()

    def first(self, symbol):
        return self.__first_col[symbol]
    
    def grammar(self):
        return self.__grammar

    def get_parsed_table(self):
        return self.__parsing_table
    
    def parse(self, input):
        # TODO: Implement parsing algorithm
        pass
    
    def __check_ll1(self):
        if not self.__grammar.check_cfg():
            return False

        productions = self.__grammar.get_productions().get_all()

        for rhs in productions.values():
            no_non_terminals = 0
            terminals = dict()

            for rule in rhs:
                if rule[0] in self.__grammar.get_nonterminals():
                    no_non_terminals += 1

                    if no_non_terminals > 1:
                        return False
                    
                    elif no_non_terminals == 1 and len(rhs) > 1:
                        return False
                    
                elif rule[0] in self.__grammar.get_terminals():
                    terminals[rule[0]] = terminals.get(rule[0], 0) + 1

                    if terminals[rule[0]] > 1:
                        return False
                    
        return True
    
    def __build_table(self):
        if not self.__check_ll1():
            raise ValueError("Grammar is not LL(1)")

        self.__build_first()
        self.__build_follow()
        self.__build_parsing_table()

    def __build_first(self):
        non_terminals = self.__grammar.get_nonterminals()
        terminals = self.__grammar.get_terminals()
        productions = self.__grammar.get_productions().get_all()
        first_col = self.__first_col

        for symbol in non_terminals:
            first_col[symbol] = set()

        for lhs, rhs in reversed(productions.items()):
            for rule in rhs:
                if rule[0] in terminals:
                    first_col[lhs[0]].add(str(rule[0]))

                elif rule[0] in non_terminals:
                    first_col[lhs[0]].add(str(first_col[rule[0]]))

                else:
                    raise ValueError("Invalid symbol in production rule: {}".format(rule[0]))

    def __build_follow(self):
        non_terminals = self.__grammar.get_nonterminals()
        terminals = self.__grammar.get_terminals()
        productions = self.__grammar.get_productions().get_all()
        first_col = self.__first_col
        follow_col = self.__follow_col
        for symbol in non_terminals:
            follow_col[symbol] = set()

        follow_col[self.__grammar.get_input_symbol()] = set('$')

        for key in productions.keys():

            for lhs, rhs in productions.items():
                for rule in rhs:
                    for i in range(len(rule)):
                        symbol = rule[i]

                        if symbol == key[0]:

                            if i == len(rule) - 1:
                                follow_col[symbol].add(str(follow_col[lhs[0]]))

                            elif rule[i + 1] in terminals:
                                follow_col[symbol].add(str(rule[i + 1]))

                            elif rule[i + 1] in non_terminals:
                                follow_col[symbol].add(str(first_col[rule[i + 1]]))
                            
                            else:
                                raise ValueError("Invalid symbol in production rule: {}".format(rule[i + 1]))
                            
    def __build_parsing_table(self):
        non_terminals = self.__grammar.get_nonterminals()
        terminals = self.__grammar.get_terminals()
        productions = self.__grammar.get_productions().get_all()

        for non_terminal in non_terminals:
            self.__parsing_table[non_terminal] = dict()

            for terminal in terminals:
                self.__parsing_table[non_terminal][terminal] = None

            self.__parsing_table[non_terminal]['$'] = None

        for lhs, rhs in productions.items():
            for rule in rhs:
                if rule[0] in terminals:
                    self.__parsing_table[lhs[0]][rule[0]] = rule

                elif rule[0] in non_terminals:
                    for terminal in self.__first_col[rule[0]]:
                        self.__parsing_table[lhs[0]][terminal] = rule

                else:
                    raise ValueError("Invalid symbol in production rule: {}".format(rule[0]))
