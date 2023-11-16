# Finite Automaton (FA) Class Documentation

**Github Link**: https://github.com/917-SzaboBalazs/FLCD/tree/main/lab4

The `FA` class is designed to represent a Finite Automaton, a mathematical model of computation. This class encapsulates the properties and behavior of a finite automaton, providing methods to interact with its definition and determine if a given sequence is accepted by the automaton.

## Constructor

### `__init__(self)`

The constructor initializes the `FA` object with the following instance variables:

- `__input_file`: The path to the input file.
- `__all_states`: A list containing all states of the automaton.
- `__input_symbols`: A list containing all input symbols.
- `__initial_state`: The initial state of the automaton.
- `__final_states`: A list containing all final states of the automaton.
- `__transition_function`: A dictionary representing the transition function of the automaton.

## Methods

### `get_input_file(self)`

Returns the path of the input file.

### `get_all_states(self)`

Returns a list of all states in the automaton.

### `get_input_symbols(self)`

Returns a list of input symbols.

### `get_initial_state(self)`

Returns the initial state of the automaton.

### `get_final_states(self)`

Returns a list of final states of the automaton.

### `get_transition_function(self)`

Returns the transition function of the automaton as a dictionary.

### `read_from_file(self, input_file)`

Reads the automaton definition from a specified input file. It populates the instance variables based on the content of the file.

- Parameters:
  - `input_file`: Path to the input file.

### `seq_is_accepted(self, seq)`

Checks if a given sequence is accepted by the automaton.

- Parameters:
  - `seq`: The input sequence to be checked.
- Returns:
  - `True` if the sequence is accepted, `False` otherwise.

## Example Usage

```python
# Instantiate FA object
fa_instance = FA()

# Read automaton definition from file
fa_instance.read_from_file("path/to/automaton_definition.txt")

# Check if a sequence is accepted
result = fa_instance.seq_is_accepted("input_sequence")
```

## Input file format (EBNF)
```
input_file = states | "\n" | symbols | "\n" |  initial_state |
"\n" | final_states | "\n" | transition_function

letter = "abc..zAB...Z"
digit = "01..9" 

states = state | {"," | state}
state = letter | digit

symbols = symbol | {"," | symbol}
symbol = letter | digit

initial_state = state

final_states = state | {"," | state}

transition_function = transition | {"\n", transition}
transition = "(" | state | "," | symbol | ")" | "=" | state
```
