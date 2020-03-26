#### By Christian Micklisch 🐴 Manoj Krishna Mohan
# What to do:

Your program should be well documented, and you should turn in the following in hard copy:

1. An  external  documentation  describing  the n-queens  formulation,  the  program  structure,  global variables,  the  function/procedure  to  compute  the  heuristic  function,  and  other  functions/procedures, etc.
2. Your program source codes (with necessary inline documentation);
3. The execution results as specified above.

# N-Queens problem formulation
The N-Queens problem is a NP-Complete problem. The problem is to find the arrangement of N queens on an NxN chess board, such that no queen can attack any other queens on the board. The chess queens can attack in any direction as horizontal, vertical, horizontal and diagonal way. The attacks can also be direct or indirect. 
```	
   { 0,  👑,  0,  0}
   { 0,  0,  0,  👑}
   { 👑,  0,  0,  0}
   { 0,  0,  👑,  0}
```
The above board represents a 4x4 board such that no queens attack each other. In our project, we have tried to use the column-wise movement, sideways movement method and also the Random restart methodologies to achieve the solution.

# The Program structure
The programs for defining and generating the NxN chess board and also the other files which include the hill-climbing algorithms and the test cases are listed as below.
All the functions are called inside of the main.py file which runs once the test cases are generated. The logic for hillclimbing is defined in the hill_climbing.py and the generated state is once again evaluated by the evaluate.py file.
The subfolder test_files contains all the respective test cases that run before the User inputs the values for generating the N-Queens board.
```
├──test_files
│   ├── test.py
│   ├── test_evaluate.py
│   ├── test_generate.py
│   └── test_hill_climbing.py
├── evaluate.py
├── generate_nxn.py
├── hill_climbing.py
└── main.py

```
# hill-climbing-search

Hill Climbing implementation 

## Hill Climbing Results
```
Running 100 cases for hill climbing
Rate of success:  0.15
Rate of failure:  0.85
Average steps for success:  5.0
Average steps for failure:  3.988235294117647
```
## Sideways Move Results
```
Running 100 cases for sideways move with 25 steps
Rate of success:  0.88(This varies with every run, since it is at random)
Rate of failure:  0.12
Average steps for success:  22.579545454545453
Average steps for failure:  65.41666666666667
```
## Random Restart Results
```
Running 100 cases for random restart move with 25 restarts
Rate of success:  0.99
Rate of failure:  0.01
Average steps for success:  30.363636363636363
Average steps for failure:  108.0
```

<!-- Test Cases -->

# OUTPUT Currentlys
```
Run evaluation or run a single size (eval/single)?eval
Running evaluation for 8-queens problem at, 100 unique cases
Running 100 case(s) for hill climbing
Moves for initial state:
- - - Q - - - - 
Q - - - - - - - 
- - - - - - - - 
- Q - - - - - Q 
- - - - - - - - 
- - - - Q - Q - 
- - - - - Q - - 
- - Q - - - - - 
Move:  1 

- - - Q - - - - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - Q 
- - - - - - - - 
- - - - - - Q - 
- - - - - Q - - 
- - Q - - - - - 

Move:  2 

- - - Q - - - - 
Q - - - - - - - 
- - - - Q - - - 
- - - - - - - Q 
- Q - - - - - - 
- - - - - - Q - 
- - - - - Q - - 
- - Q - - - - - 

Move:  3 

- - - Q - - - - 
Q - - - - - - - 
- - - - Q - - - 
- - - - - - - Q 
- Q - - - - - - 
- - - - - - Q - 
- - - - - - - - 
- - Q - - Q - - 

Move:  4 

- - - Q - - - - 
Q - - - - - - - 
- - - - Q - - - 
- - - - - - - Q 
- Q - - - - - - 
- - - - - - Q - 
- - Q - - - - - 
- - - - - Q - - 

Moves for initial state:
- Q - - - - - - 
- - - - - - - Q 
- - - - - - - - 
- - - - - - - - 
- - - - Q - Q - 
- - - - - - - - 
- - - - - - - - 
Q - Q Q - Q - - 
Move:  1 

- Q - - - - - - 
- - - - - - - Q 
- - - - - - - - 
Q - - - - - - - 
- - - - Q - Q - 
- - - - - - - - 
- - - - - - - - 
- - Q Q - Q - - 

Move:  2 

- Q - - - - - - 
- - - - - - - Q 
- - - Q - - - - 
Q - - - - - - - 
- - - - Q - Q - 
- - - - - - - - 
- - - - - - - - 
- - Q - - Q - - 

Move:  3 

- - - - - - - - 
- - - - - - - Q 
- - - Q - - - - 
Q - - - - - - - 
- - - - Q - Q - 
- Q - - - - - - 
- - - - - - - - 
- - Q - - Q - - 

Move:  4 

- - - - Q - - - 
- - - - - - - Q 
- - - Q - - - - 
Q - - - - - - - 
- - - - - - Q - 
- Q - - - - - - 
- - - - - - - - 
- - Q - - Q - - 

Move:  5 

- - - - Q - - - 
- - - - - - - Q 
- - - Q - - - - 
Q - - - - - - - 
- - - - - - Q - 
- Q - - - - - - 
- - - - - Q - - 
- - Q - - - - - 

Moves for initial state:
- - - - - - - - 
- - Q - - Q - Q 
- - - - - - Q - 
Q - - Q - - - - 
- - - - - - - - 
- - - - - - - - 
- Q - - - - - - 
- - - - Q - - - 
Move:  1 

- - - - - Q - - 
- - Q - - - - Q 
- - - - - - Q - 
Q - - Q - - - - 
- - - - - - - - 
- - - - - - - - 
- Q - - - - - - 
- - - - Q - - - 

Move:  2 

- - - - - Q - - 
- - Q - - - - Q 
- - - - - - Q - 
- - - Q - - - - 
Q - - - - - - - 
- - - - - - - - 
- Q - - - - - - 
- - - - Q - - - 

Move:  3 

- - - - - Q - - 
- - Q - - - - - 
- - - - - - Q - 
- - - Q - - - - 
Q - - - - - - - 
- - - - - - - Q 
- Q - - - - - - 
- - - - Q - - - 

Moves for initial state:
Q - - Q - - - - 
- Q - - - - - - 
- - - - - - Q - 
- - - - - - - - 
- - Q - - - - - 
- - - - Q Q - - 
- - - - - - - - 
- - - - - - - Q 
Move:  1 

- - - Q - - - - 
- Q - - - - - - 
- - - - - - Q - 
Q - - - - - - - 
- - Q - - - - - 
- - - - Q Q - - 
- - - - - - - - 
- - - - - - - Q 

Move:  2 

- - - Q - - - - 
- - - - - - - - 
- - - - - - Q - 
Q - - - - - - - 
- - Q - - - - - 
- - - - Q Q - - 
- Q - - - - - - 
- - - - - - - Q 

Move:  3 

- - - - - - - - 
- - - Q - - - - 
- - - - - - Q - 
Q - - - - - - - 
- - Q - - - - - 
- - - - Q Q - - 
- Q - - - - - - 
- - - - - - - Q 

Move:  4 

- - - - - Q - - 
- - - Q - - - - 
- - - - - - Q - 
Q - - - - - - - 
- - Q - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - - - Q 

Rate of success:  0.1
Rate of failure:  0.9
Average steps for success:  5.3
Average steps for failure:  4.111111111111111
Running 100 case(s) for sideways move with 25 steps
Moves for initial state:
- Q - - - Q - - 
- - - - - - - - 
Q - - - Q - - - 
- - - - - - - - 
- - - - - - Q - 
- - Q - - - - - 
- - - Q - - - Q 
- - - - - - - - 
Move:  1 

- - - - - Q - - 
- - - - - - - - 
Q - - - Q - - - 
- - - - - - - - 
- - - - - - Q - 
- - Q - - - - - 
- - - Q - - - Q 
- Q - - - - - - 

Move:  2 

- - - - - Q - - 
Q - - - - - - - 
- - - - Q - - - 
- - - - - - - - 
- - - - - - Q - 
- - Q - - - - - 
- - - Q - - - Q 
- Q - - - - - - 

Move:  3 

- - - Q - Q - - 
Q - - - - - - - 
- - - - Q - - - 
- - - - - - - - 
- - - - - - Q - 
- - Q - - - - - 
- - - - - - - Q 
- Q - - - - - - 

Move:  4 

- - - Q Q - - - 
Q - - - - - - - 
- - - - - Q - - 
- - - - - - - - 
- - - - - - Q - 
- - Q - - - - - 
- - - - - - - Q 
- Q - - - - - - 

Move:  5 

- - - - Q - - - 
Q - - - - - - - 
- - - - - Q - - 
- - - Q - - - - 
- - - - - - Q - 
- - Q - - - - - 
- - - - - - - Q 
- Q - - - - - - 

Move:  6 

- - Q - - - - - 
Q - - - - - - - 
- - - - - Q - - 
- - - Q - - - - 
- - - - - - Q - 
- - - - Q - - - 
- - - - - - - Q 
- Q - - - - - - 

Move:  7 

- - - - Q - - - 
Q - - - - - - - 
- - - - - Q - - 
- - - Q - - - - 
- - - - - - Q - 
- - Q - - - - - 
- - - - - - - Q 
- Q - - - - - - 

Move:  8 

- - - - Q - - - 
Q - - - - - - - 
- - - - - Q - - 
- - - Q - - - - 
- - - - - - Q - 
- Q - - - - - - 
- - - - - - - Q 
- - Q - - - - - 

Move:  9 

- - - - Q - - - 
- - - Q - - - - 
- - - - - Q - - 
Q - - - - - - - 
- - - - - - Q - 
- Q - - - - - - 
- - - - - - - Q 
- - Q - - - - - 

Move:  10 

- - - - Q - - - 
- - - - - - - - 
- - - - - Q - - 
Q - - - - - - - 
- - - - - - Q - 
- Q - Q - - - - 
- - - - - - - Q 
- - Q - - - - - 

Move:  11 

- - - - Q - - - 
- Q - - - - - - 
- - - - - Q - - 
Q - - - - - - - 
- - - - - - Q - 
- - - Q - - - - 
- - - - - - - Q 
- - Q - - - - - 

Moves for initial state:
Q - Q - - - Q - 
- Q - - Q - - Q 
- - - - - - - - 
- - - - - - - - 
- - - Q - - - - 
- - - - - - - - 
- - - - - Q - - 
- - - - - - - - 
Move:  1 

Q - Q - - - Q - 
- - - - Q - - Q 
- - - - - - - - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - - - - 
- - - - - Q - - 
- - - - - - - - 

Move:  2 

Q - - - - - Q - 
- - - - Q - - Q 
- - - - - - - - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - - - - 
- - - - - Q - - 
- - Q - - - - - 

Move:  3 

Q - - - - - Q - 
- - - - Q - - - 
- - - - - - - - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - - - Q 
- - - - - Q - - 
- - Q - - - - - 

Move:  4 

Q - - - - - - - 
- - - - Q - - - 
- - - - - - Q - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - - - Q 
- - - - - Q - - 
- - Q - - - - - 

Move:  5 

Q - - - - - - - 
- - - - Q - - - 
- - - - - - Q - 
- - - Q - - - - 
- Q - - - - - - 
- - - - - - - Q 
- - - - - Q - - 
- - Q - - - - - 

Move:  6 

Q - - - - - - - 
- - - - Q - - - 
- - - - - - Q - 
- - - - - Q - - 
- Q - - - - - - 
- - - - - - - Q 
- - - Q - - - - 
- - Q - - - - - 

Move:  7 

Q Q - - - - - - 
- - - - Q - - - 
- - - - - - Q - 
- - - - - Q - - 
- - - - - - - - 
- - - - - - - Q 
- - - Q - - - - 
- - Q - - - - - 

Move:  8 

- Q - - - - - - 
- - - - Q - - - 
- - - - - - Q - 
- - - - - Q - - 
Q - - - - - - - 
- - - - - - - Q 
- - - Q - - - - 
- - Q - - - - - 

Move:  9 

- Q - - - - - - 
- - - - Q - - - 
- - - - - - Q - 
- - - - - - - - 
Q - - - - - - - 
- - - - - Q - Q 
- - - Q - - - - 
- - Q - - - - - 

Move:  10 

- Q - - - - - - 
Q - - - - - - - 
- - - - - - Q - 
- - - - - - - - 
- - - - Q - - - 
- - - - - Q - Q 
- - - Q - - - - 
- - Q - - - - - 

Move:  11 

- - - - - - - - 
Q - - - - - - - 
- - - - - - Q - 
- Q - - - - - - 
- - - - Q - - - 
- - - - - Q - Q 
- - - Q - - - - 
- - Q - - - - - 

Move:  12 

- - - - - Q - - 
Q - - - - - - - 
- - - - - - Q - 
- Q - - - - - - 
- - - - Q - - - 
- - - - - - - Q 
- - - Q - - - - 
- - Q - - - - - 

Move:  13 

- - - - - Q - - 
Q - - - - - - - 
- - - - - - - Q 
- Q - - - - - - 
- - - - Q - - - 
- - - - - - Q - 
- - - Q - - - - 
- - Q - - - - - 

Move:  14 

- - - - - Q - Q 
Q - - - - - - - 
- - - - - - - - 
- Q - - - - - - 
- - - - Q - - - 
- - - - - - Q - 
- - - Q - - - - 
- - Q - - - - - 

Move:  15 

- - - - Q Q - - 
Q - - - - - - - 
- - - - - - - - 
- Q - - - - - - 
- - - - - - - Q 
- - - - - - Q - 
- - - Q - - - - 
- - Q - - - - - 

Move:  16 

- - - - - Q - - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - - - Q 
- - - - - - Q - 
- - - Q - - - - 
- - Q - - - - - 

Move:  17 

- - - - - Q - - 
- - - Q - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - - - Q 
- - - - - - Q - 
Q - - - - - - - 
- - Q - - - - - 

Move:  18 

- - - - - Q - - 
- - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - Q - - - Q 
- - - - - - Q - 
Q - - - - - - - 
- - Q - - - - - 

Move:  19 

- - - - - Q - - 
- - - - - - - Q 
- - - - Q - - - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - - Q - 
Q - - - - - - - 
- - Q - - - - - 

Move:  20 

- - - - - - Q - 
- - - - - - - Q 
- - - - Q - - - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - Q - - 
Q - - - - - - - 
- - Q - - - - - 

Move:  21 

- - - - - - - - 
- - - - - - - Q 
- - - - Q - - - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - Q Q - 
Q - - - - - - - 
- - Q - - - - - 

Move:  22 

- - - - - Q - - 
- - - - - - - Q 
- - - - Q - - - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - - Q - 
Q - - - - - - - 
- - Q - - - - - 

Move:  23 

- - - - - Q - - 
- - - - - - - Q 
- - - - Q - - - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - - Q - 
- - Q - - - - - 
Q - - - - - - - 

Move:  24 

- - - - Q - - - 
- - - - - - - Q 
- - - - - Q - - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - - Q - 
- - Q - - - - - 
Q - - - - - - - 

Move:  25 

Q - - - Q - - - 
- - - - - - - Q 
- - - - - Q - - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - - Q - 
- - Q - - - - - 
- - - - - - - - 

Move:  26 

Q - - - Q - - - 
- - - - - - - Q 
- - - - - Q - - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - - Q - 
- - - - - - - - 
- - Q - - - - - 

Move:  27 

- - - - Q - - - 
- - - - - - - Q 
- - - - - Q - - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - - Q - 
Q - - - - - - - 
- - Q - - - - - 

Move:  28 

- - - - Q - - - 
- - - - - - - Q 
- - - - - Q - - 
- Q - - - - - - 
Q - - - - - - - 
- - - - - - Q - 
- - - Q - - - - 
- - Q - - - - - 

Move:  29 

Q - - - Q - - - 
- - - - - - - Q 
- - - - - Q - - 
- Q - - - - - - 
- - - - - - - - 
- - - - - - Q - 
- - - Q - - - - 
- - Q - - - - - 

Move:  30 

Q - - - - - - - 
- - - - - - - Q 
- - - - Q Q - - 
- Q - - - - - - 
- - - - - - - - 
- - - - - - Q - 
- - - Q - - - - 
- - Q - - - - - 

Move:  31 

Q - - - - - - - 
- - - - - - - Q 
- - - - Q Q - - 
- - - - - - Q - 
- - - - - - - - 
- Q - - - - - - 
- - - Q - - - - 
- - Q - - - - - 

Move:  32 

Q - - - - - - - 
- - - - - - - Q 
- - - - Q Q - - 
- - - - - - - - 
- - - - - - Q - 
- Q - - - - - - 
- - - Q - - - - 
- - Q - - - - - 

Move:  33 

Q - - - Q - - - 
- - - - - - - Q 
- - - - - Q - - 
- - - - - - - - 
- - - - - - Q - 
- Q - - - - - - 
- - - Q - - - - 
- - Q - - - - - 

Move:  34 

Q - - - Q - - - 
- - - - - - - Q 
- - - - - Q - - 
- - Q - - - - - 
- - - - - - Q - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - - - - 

Move:  35 

Q - - - Q - - - 
- - - - - - - Q 
- - - - - Q - - 
- - - - - - Q - 
- - Q - - - - - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - - - - 

Move:  36 

Q - - - Q - - - 
- - - - - - - Q 
- - - - - Q - - 
- - - - - - - - 
- - Q - - - - - 
- Q - - - - - - 
- - - Q - - - - 
- - - - - - Q - 

Move:  37 

- - - - Q - Q - 
- - - - - - - Q 
- - - - - Q - - 
- - - - - - - - 
- - Q - - - - - 
- Q - - - - - - 
- - - Q - - - - 
Q - - - - - - - 

Move:  38 

- - - - Q - - - 
- - - - - - - Q 
- - - - - Q - - 
- - - - - - - - 
- - Q - - - Q - 
- Q - - - - - - 
- - - Q - - - - 
Q - - - - - - - 

Move:  39 

- - - - Q - - - 
- - - - - - - Q 
- - - - - Q - - 
- - Q - - - - - 
- - - - - - Q - 
- Q - - - - - - 
- - - Q - - - - 
Q - - - - - - - 

Move:  40 

- - - Q - - - - 
- - - - - - - Q 
- - - - - Q - - 
- - Q - - - - - 
- - - - - - Q - 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - - - - 

Move:  41 

- - - Q - - - - 
- - - - - - - Q 
- - - - - - - - 
- - Q - - - - - 
- - - - - Q Q - 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - - - - 

Move:  42 

- - - Q - - - - 
- - - - - - - Q 
- - - - - - Q - 
- - Q - - - - - 
- - - - - Q - - 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - - - - 

Move:  43 

- - - Q - - - - 
- - - - - - - Q 
- - Q - - - - - 
- - - - - - Q - 
- - - - - Q - - 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - - - - 

Move:  44 

- - - Q - - - - 
- - - - - - - Q 
- - Q - - - - - 
- - - - - - - - 
- - - - - Q - - 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - - Q - 

Move:  45 

- - - - - - Q - 
- - - - - - - Q 
- - Q - - - - - 
- - - - - - - - 
- - - - - Q - - 
- Q - - - - - - 
- - - - Q - - - 
Q - - Q - - - - 

Move:  46 

- - - Q - - Q - 
- - - - - - - Q 
- - Q - - - - - 
- - - - - - - - 
- - - - - Q - - 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - - - - 

Move:  47 

- - - Q - - - - 
- - - - - - - Q 
- - Q - - - - - 
- - - - - - - - 
- - - - - Q - - 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - - Q - 

Move:  48 

- - - Q - - - - 
- - - - - Q - - 
- - Q - - - - - 
- - - - - - - - 
- - - - - - - Q 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - - Q - 

Move:  49 

- - - Q - - - - 
- - - - - - - - 
- - Q - - - - - 
- - - - - Q - - 
- - - - - - - Q 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - - Q - 

Move:  50 

- - - Q - - - - 
- - - - - - - - 
- - Q - - - - - 
- - - - - - Q - 
- - - - - - - Q 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - Q - - 

Move:  51 

- - - Q - - - - 
- - - - - - - Q 
- - Q - - - - - 
- - - - - - Q - 
- - - - - - - - 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - Q - - 

Move:  52 

- - - Q - Q - - 
- - - - - - - Q 
- - Q - - - - - 
- - - - - - Q - 
- - - - - - - - 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - - - - 

Move:  53 

- - - - - Q - - 
- - - - - - - Q 
- - Q - - - - - 
- - - - - - Q - 
- - - Q - - - - 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - - - - 

Move:  54 

- - - - - Q - - 
- - - - - - - Q 
- - - Q - - - - 
- - - - - - Q - 
- - Q - - - - - 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - - - - 

Move:  55 

- - Q - - Q - - 
- - - - - - - Q 
- - - Q - - - - 
- - - - - - Q - 
- - - - - - - - 
- Q - - - - - - 
- - - - Q - - - 
Q - - - - - - - 

Move:  56 

- - Q - - - - - 
- - - - - - - Q 
- - - Q - - - - 
- - - - - - Q - 
- - - - - - - - 
- Q - - - - - - 
- - - - Q Q - - 
Q - - - - - - - 

Move:  57 

- - Q - - - - - 
- - - - - - - Q 
- - - - - - Q - 
- - - Q - - - - 
- - - - - - - - 
- Q - - - - - - 
- - - - Q Q - - 
Q - - - - - - - 

Move:  58 

- - Q - - - - - 
- - - - - - - Q 
- - - - - - Q - 
- - - Q - - - - 
- Q - - - - - - 
- - - - - - - - 
- - - - Q Q - - 
Q - - - - - - - 

Move:  59 

- - Q - - - - - 
- - - - - - - Q 
- - - - - - Q - 
- - - Q - - - - 
- - - - Q - - - 
- - - - - - - - 
- Q - - - Q - - 
Q - - - - - - - 

Move:  60 

- - Q - - - - - 
- - - - Q - - Q 
- - - - - - Q - 
- - - Q - - - - 
- - - - - - - - 
- - - - - - - - 
- Q - - - Q - - 
Q - - - - - - - 

Move:  61 

- - Q - - - - - 
- - - - Q - - Q 
- - - - - - Q - 
- - - Q - - - - 
Q - - - - - - - 
- - - - - - - - 
- Q - - - Q - - 
- - - - - - - - 

Move:  62 

- - Q - - - - - 
- - - - Q - - Q 
- - - - - - Q - 
- - - Q - - - - 
Q - - - - - - - 
- - - - - - - - 
- Q - - - - - - 
- - - - - Q - - 

Move:  63 

- - Q - - - - - 
- - - - - - - Q 
- - - - - - Q - 
- - - Q - - - - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - Q - - 

Move:  64 

- - Q - - - - - 
- - - - - - - Q 
- - - - - - Q - 
- - - - - Q - - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - Q - - - - 

Move:  65 

- - Q - - Q - - 
- - - - - - - Q 
- - - - - - Q - 
- - - - - - - - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - Q - - - - 

Move:  66 

- - Q - - Q - - 
- - - - - - - Q 
- - - - - - Q - 
Q - - - - - - - 
- - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - Q - - - - 

Move:  67 

- - - - - Q - - 
- - - - - - - Q 
- - - - - - Q - 
Q - - - - - - - 
- - Q - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - Q - - - - 

Move:  68 

- - - - - Q - - 
- - Q - - - - - 
- - - - - - Q - 
Q - - - - - - - 
- - - - - - - Q 
- - - - Q - - - 
- Q - - - - - - 
- - - Q - - - - 

Move:  69 

- - - - - Q - - 
- - Q - - - - - 
- - - - - - Q - 
Q - - - - - - - 
- - - - - - - Q 
- Q - - - - - - 
- - - - Q - - - 
- - - Q - - - - 

Move:  70 

- - - - - Q - - 
- - Q Q - - - - 
- - - - - - Q - 
Q - - - - - - - 
- - - - - - - Q 
- Q - - - - - - 
- - - - Q - - - 
- - - - - - - - 

Move:  71 

- - - - - Q - - 
- - - Q - - - - 
- - - - - - Q - 
Q - - - - - - - 
- - - - - - - Q 
- Q - - - - - - 
- - - - Q - - - 
- - Q - - - - - 

Moves for initial state:
- - - - - - - - 
Q - Q - - Q Q - 
- - - - - - - - 
- - - - - - - - 
- - - - - - - Q 
- - - Q Q - - - 
- - - - - - - - 
- Q - - - - - - 
Move:  1 

Q - - - - - - - 
- - Q - - Q Q - 
- - - - - - - - 
- - - - - - - - 
- - - - - - - Q 
- - - Q Q - - - 
- - - - - - - - 
- Q - - - - - - 

Move:  2 

Q - Q - - - - - 
- - - - - Q Q - 
- - - - - - - - 
- - - - - - - - 
- - - - - - - Q 
- - - Q Q - - - 
- - - - - - - - 
- Q - - - - - - 

Move:  3 

Q - Q - - - - - 
- - - - - Q Q - 
- - - Q - - - - 
- - - - - - - - 
- - - - - - - Q 
- - - - Q - - - 
- - - - - - - - 
- Q - - - - - - 

Move:  4 

- - Q - - - - - 
- - - - - Q Q - 
- - - Q - - - - 
Q - - - - - - - 
- - - - - - - Q 
- - - - Q - - - 
- - - - - - - - 
- Q - - - - - - 

Move:  5 

- - Q - - - - - 
- - - - - Q - - 
- - - Q - - - - 
Q - - - - - - - 
- - - - - - - Q 
- - - - Q - - - 
- - - - - - Q - 
- Q - - - - - - 

Move:  6 

- - - Q - - - - 
- - - - - Q - - 
- - Q - - - - - 
Q - - - - - - - 
- - - - - - - Q 
- - - - Q - - - 
- - - - - - Q - 
- Q - - - - - - 

Move:  7 

- - - - - - - - 
- - - - - Q - - 
- - Q Q - - - - 
Q - - - - - - - 
- - - - - - - Q 
- - - - Q - - - 
- - - - - - Q - 
- Q - - - - - - 

Move:  8 

- - Q - - - - - 
- - - - - Q - - 
- - - Q - - - - 
Q - - - - - - - 
- - - - - - - Q 
- - - - Q - - - 
- - - - - - Q - 
- Q - - - - - - 

Moves for initial state:
- - Q - - - - - 
Q - - - - - - - 
- Q - - - - Q Q 
- - - - Q - - - 
- - - - - - - - 
- - - Q - Q - - 
- - - - - - - - 
- - - - - - - - 
Move:  1 

- - Q - - - - - 
Q - - - - - - - 
- - - - - - Q Q 
- - - - Q - - - 
- Q - - - - - - 
- - - Q - Q - - 
- - - - - - - - 
- - - - - - - - 

Move:  2 

- - Q Q - - - - 
Q - - - - - - - 
- - - - - - Q Q 
- - - - Q - - - 
- Q - - - - - - 
- - - - - Q - - 
- - - - - - - - 
- - - - - - - - 

Move:  3 

Q - - Q - - - - 
- - Q - - - - - 
- - - - - - Q Q 
- - - - Q - - - 
- Q - - - - - - 
- - - - - Q - - 
- - - - - - - - 
- - - - - - - - 

Move:  4 

- - - Q - - - - 
- - Q - - - - - 
- - - - - - Q Q 
- - - - Q - - - 
- Q - - - - - - 
- - - - - Q - - 
Q - - - - - - - 
- - - - - - - - 

Move:  5 

- - Q Q - - - - 
- - - - - - - - 
- - - - - - Q Q 
- - - - Q - - - 
- Q - - - - - - 
- - - - - Q - - 
Q - - - - - - - 
- - - - - - - - 

Move:  6 

- - Q Q - - - - 
- - - - - - - - 
- - - - - - - Q 
- - - - Q - - - 
- Q - - - - - - 
- - - - - Q - - 
Q - - - - - - - 
- - - - - - Q - 

Move:  7 

- - Q Q - - - - 
- - - - - - - - 
- - - - - - - Q 
- - - - Q - - - 
Q - - - - - - - 
- - - - - Q - - 
- Q - - - - - - 
- - - - - - Q - 

Move:  8 

- - Q Q - - - - 
- - - - - - - - 
- - - - - - Q - 
- - - - Q - - - 
Q - - - - - - - 
- - - - - Q - - 
- Q - - - - - - 
- - - - - - - Q 

Move:  9 

- - Q Q - - - - 
- - - - - - - - 
- - - - - - Q - 
- - - - - Q - - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - - - Q 

Move:  10 

- - - Q - - - - 
- - Q - - - - - 
- - - - - - Q - 
- - - - - Q - - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - - - Q 

Move:  11 

- - Q - - - - - 
- - - Q - - - - 
- - - - - - Q - 
- - - - - Q - - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - - - Q 

Move:  12 

- - Q Q - - - - 
- - - - - - - - 
- - - - - - Q - 
- - - - - Q - - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - - - Q 

Move:  13 

- - - Q - - - - 
- - Q - - - - - 
- - - - - - Q - 
- - - - - Q - - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - - - Q 

Move:  14 

- - - Q - - - - 
- - - - - - Q - 
- - Q - - - - - 
- - - - - Q - - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - - - Q 

Move:  15 

- - - Q - - - - 
- - - - - - Q - 
- - - - - - - - 
- - - - - Q - - 
Q - Q - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - - - Q 

Move:  16 

- - - Q - - - - 
Q - - - - - - - 
- - - - - - - - 
- - - - - Q - - 
- - Q - - - Q - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - - - Q 

Move:  17 

- - - Q - - - - 
Q - - - - - - - 
- - - - - - Q - 
- - - - - Q - - 
- - Q - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - - - Q 

Move:  18 

- - - Q - - - - 
Q - - - - - - - 
- - - - - - Q - 
- - - - - Q - - 
- - Q - - - - - 
- Q - - - - - - 
- - - - Q - - - 
- - - - - - - Q 

Move:  19 

- - - Q - - - - 
Q - - - - - - - 
- - - - - - Q - 
- - - - - Q - - 
- - - - - - - - 
- Q Q - - - - - 
- - - - Q - - - 
- - - - - - - Q 

Move:  20 

- - - Q - - - - 
Q - - - - - - - 
- - - - - - Q - 
- - - - - - - - 
- - - - - Q - - 
- Q Q - - - - - 
- - - - Q - - - 
- - - - - - - Q 

Move:  21 

- - - Q - - - - 
Q - - - - - - - 
- - - - - - Q - 
- - - - - - - - 
- - Q - - - - - 
- Q - - - Q - - 
- - - - Q - - - 
- - - - - - - Q 

Move:  22 

- - - Q - - - - 
Q - - - - - - - 
- - - - - - Q - 
- - - - Q - - - 
- - Q - - - - - 
- Q - - - Q - - 
- - - - - - - - 
- - - - - - - Q 

Move:  23 

- - - Q - - - - 
Q - - - - - - - 
- - - - - - Q - 
- - - - Q - - - 
- Q Q - - - - - 
- - - - - Q - - 
- - - - - - - - 
- - - - - - - Q 

Move:  24 

- - - Q - - - - 
- - - - - - Q - 
Q - - - - - - - 
- - - - Q - - - 
- Q Q - - - - - 
- - - - - Q - - 
- - - - - - - - 
- - - - - - - Q 

Move:  25 

- - - Q - - - - 
- - - - - - Q - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - Q - - 
- - Q - - - - - 
- - - - - - - Q 

Move:  26 

- - Q - - - - - 
- - - - - - Q - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - Q - - 
- - - Q - - - - 
- - - - - - - Q 

Move:  27 

- - - - - Q - - 
- - - - - - Q - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - Q - - - - - 
- - - Q - - - - 
- - - - - - - Q 

Move:  28 

- - - - - Q - - 
- - - - - - Q - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - - - - 
- - Q Q - - - - 
- - - - - - - Q 

Move:  29 

- - - - - Q - - 
- - - - - - Q - 
Q Q - - - - - - 
- - - - Q - - - 
- - - - - - - - 
- - - - - - - - 
- - Q Q - - - - 
- - - - - - - Q 

Move:  30 

- - - - - Q - - 
- - - - - - - - 
Q Q - - - - - - 
- - - - Q - - - 
- - - - - - Q - 
- - - - - - - - 
- - Q Q - - - - 
- - - - - - - Q 

Move:  31 

- - - Q - - - - 
- - - - - - - - 
Q Q - - - - - - 
- - - - Q - - - 
- - - - - - Q - 
- - - - - - - - 
- - Q - - Q - - 
- - - - - - - Q 

Move:  32 

- - - Q - - - - 
- - - - - - - - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - Q - 
- - - - - - - - 
- - Q - - Q - - 
- - - - - - - Q 

Move:  33 

- - - Q - - - - 
- - - - - Q - - 
Q - - - - - - - 
- - - - Q - - - 
- Q - - - - Q - 
- - - - - - - - 
- - Q - - - - - 
- - - - - - - Q 

Move:  34 

- - - Q - - - - 
- - - - - Q - - 
Q - - - - - - - 
- Q - - - - - - 
- - - - Q - Q - 
- - - - - - - - 
- - Q - - - - - 
- - - - - - - Q 

Move:  35 

- - - Q - - - - 
- - - - - Q - - 
Q - - - - - - - 
- Q - - - - - - 
- - - - - - Q - 
- - - - Q - - - 
- - Q - - - - - 
- - - - - - - Q 

Move:  36 

- - - Q - - - - 
- - - - - Q - - 
Q - - - - - - - 
- - - - - - Q - 
- Q - - - - - - 
- - - - Q - - - 
- - Q - - - - - 
- - - - - - - Q 

Move:  37 

- - - Q - - - - 
- - - - - Q Q - 
Q - - - - - - - 
- - - - - - - - 
- Q - - - - - - 
- - - - Q - - - 
- - Q - - - - - 
- - - - - - - Q 

Move:  38 

- - - Q - - - - 
- - - - - Q Q - 
- - - - Q - - - 
- - - - - - - - 
- Q - - - - - - 
Q - - - - - - - 
- - Q - - - - - 
- - - - - - - Q 

Move:  39 

- - - Q - - - - 
- - - - - Q Q - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - - - - 
Q - - - - - - - 
- - Q - - - - - 
- - - - - - - Q 

Move:  40 

- - - Q - - - - 
- - - - - - Q - 
- - - - Q - - - 
- Q - - - - - - 
- - - - - Q - - 
Q - - - - - - - 
- - Q - - - - - 
- - - - - - - Q 

Rate of success:  0.95
Rate of failure:  0.05
Average steps for success:  25.389473684210525
Average steps for failure:  67.2
Average steps for success sideways:  7.042105263157895
Running 100 case(s) for random restart move with 25 restarts
Rate of success:  0.99
Rate of failure:  0.01
Average steps for success:  30.939393939393938
Average steps for failure:  103.0
Average steps for success restarts:  5.313131313131313
Running 100 case(s) for random restart move with 25 restarts and sideways moves
Rate of success:  1.0
Rate of failure:  0.0
Average steps for success:  40.19
Average steps for failure:  Unkown
Average steps for success sideways:  8.41
Average steps for success restarts:  0.71
```
