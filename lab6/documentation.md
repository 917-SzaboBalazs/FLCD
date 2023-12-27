# LL1 Class Documentation

### Github
https://github.com/917-SzaboBalazs/FLCD/tree/main/lab6

### Made by
Szabó Balázs <br>
Tankó-Gábor Tamás

The `Ll1` class is designed for constructing and working with LL(1) parsing tables. It includes methods for obtaining the First and Follow sets of non-terminals, as well as retrieving information from the constructed LL(1) parsing table.

## Constructor

### `__init__(self, grammar)`

- **Parameters:**
  - `grammar`: An instance of a grammar class containing non-terminals, terminals, productions, and the start symbol.

- **Description:**
  - Initializes the LL1 object with the given grammar and constructs the LL(1) parsing table.

## Public Methods

### `get_grammar()`

- **Returns:**
  - Returns the grammar associated with the LL1 object.

### `first(self, S)`

- **Parameters:**
  - `S`: A non-terminal symbol.

- **Returns:**
  - Returns the First set for the given non-terminal symbol.

### `follow(self, S)`

- **Parameters:**
  - `S`: A non-terminal symbol.

- **Returns:**
  - Returns the Follow set for the given non-terminal symbol.

## Private Methods

### `__build_table()`

- **Description:**
  - Builds the LL(1) parsing table by calling private methods `__build_first()` and `__build_follow()`.

### `__build_first()`

This private method constructs the First set column of the LL(1) parsing table. It iterates through the grammar's productions, determining the First set for each non-terminal symbol. The method takes into account both terminal and non-terminal symbols in the productions, considering the rules for computing the First set. The resulting First set column is an essential component of the LL(1) parsing table, providing information about the potential starting symbols for each non-terminal in the grammar.    

- **Returns:**
  - Returns the First set column of the LL(1) parsing table.

### `__build_follow()`

- **Returns:**
  - Returns the Follow set column of the LL(1) parsing table.

This private method constructs the Follow set column of the LL(1) parsing table. It initializes the Follow sets for all non-terminals based on the grammar's productions and then iteratively refines these sets until a stable state is reached. The method considers the relationships between non-terminals in the grammar, updating Follow sets based on the rules of LL(1) parsing. The Follow set column is crucial for determining the possible followers of non-terminals during parsing, aiding in the construction of LL(1) parsing tables.

### `__get_first_terminals(self, rhs)`

- **Parameters:**
  - `rhs`: A list of symbols.

- **Returns:**
  - Returns the list of first terminals encountered in the given list of symbols.

## Example Usage:

```python
# Instantiate LL1 object with a grammar
ll1_parser = Ll1(my_grammar)

# Retrieve First set for a non-terminal symbol
first_set = ll1_parser.first('A')

# Retrieve Follow set for a non-terminal symbol
follow_set = ll1_parser.follow('B')
