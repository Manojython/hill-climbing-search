#### By Christian Micklisch 🐴 Manoj Krishna Mohan

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

 Hill climbing search is an optimization technique which belongs to category of Informed Search strategy. It is an iterative algorithm that starts with an arbitrary solution to a problem, then attempts to find a better solution by making incremental changes to the solution. If the increment produces a better solution, it proceeds with the incrementing until the best solution is found.

The steps involved in a Hill Climbing Search is as follows:
- Evaluate the initial state, if it is goal state then return success and Stop
- Loop Until a solution is found or there is no new operator left to apply
- Select and apply an operator to the current state
- Check new state:
- - If it is goal state, then return success and quit 
- - If it is better than the current state then assign new state as a current state
- - If not better than the current state, then proceed to the next loop or iteration until 		solution is found

# Global Variables

In this project, we define few Global Variables that require input from the USER. We first ask the USER, if he wants to run a Evaluation on the 8-QUEENS puzzle or if he wants to run a *Hill Climibing Search* on a single matrix of values. We also let the USER input his own size for which the search has to be performed.
In the Evaluation, we have a fixed amount of runs, i.e **100** and the number of **sideways_move** as mentioned in the lecture to be limited to **100**. The board size is also fixed to be a 8x8 board with **8 Queens**.
```
def run_evaluation():

    amount = 100
    sideways_amount = 25
    restarts = 25
    board_size = 8
    print("Running evaluation for 8-queens problem at,", amount,"unique cases")
    run_hill_climbing(amount, board_size)
    run_hill_climbing_sideways(amount, sideways_amount, board_size)
    run_hill_climbing_random_restart(amount, restarts, board_size)
    run_hill_climbing_random_restart_sideways(amount, restarts, board_size)
```
The Single run function is as defined below with several parameters that is required as input.
We get the **size** of the board from USER and also the **number of restarts** that are required to find the solution:
```
def get_size_input():
    size = int(input("What is the size you want to test?:"))
    amount = int(input("How many restarts do you want to have?:"))
    run_hill_climbing_random_restart(1, amount, size)
```



# Hill Climbing Implementation and Procedures
The Implementations of our Algorithms are divided as follows:
We have the ```generate_nxn.py ``` file which is used for generating the initial state of the board. We use the random library in the python modules and use it to generate the NxN board by placing queens in a random fashion, but making sure there is only one queen per column/per row.
We later use the ```generate_successors``` method to generate the succesor states of the initial generated matrix. Later we evaluate the same generated matrix with the methods that can be found in the ```evaluate.py``` file. The evaluation is done by counting the number of attacks that a Queen is vulnerable to in a *row-wise, column-wise,diagonally as well as in the reverse diagonal* manner. Based on this evaluation we do a Hill Climbing Search to get the next state and repeat the same until a state is acheived where no queens attack each other.
We also define another method to ```generate_sideways_successors``` board in order to increase the rate of success.
We also have the Random Restart method in the ```hill_clibing.py``` file. This file contains our main algorithm for performing the hill climbing search. We define a class create a Node and which additionally creates the additional nodes/states.
The Random-restart hill climbing as defined in the method ```climb_random_restart``` takes in the number of restarts and the state of the board as the arguments. It is used for conducting a series of hill-climbing searches from randomly generated initial states with the number of restarts limit.
If it reaches a limit then it means the solution could not be achieved.
The random restart is again improvised with the ```climb_random_restart_sideways``` move available too.

The actual rate of success without sideways move is around 14%.
Whereas with sideways included, the rate of success increases to 94%

Below is the results that were obtained with the hill climbing algorithm:

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
# References and Citations:
 - Notes from the Lecture by Prof. Dewan
 - Artificial Intelligence: A Modern Approach by Stuart Russell, Peter Norvig
 - https://en.wikipedia.org/wiki/Hill_climbing
 - https://www.javatpoint.com/hill-climbing-algorithm-in-ai