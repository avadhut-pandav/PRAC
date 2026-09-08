# Pseudocode & Flowcharts — All 4 Practicals (13 sub-tasks)

Each practical shares ONE core algorithm flowchart/pseudocode; only the
"evaluate/goal-test" step changes per sub-task. That specific change is
noted under each sub-task.

---

## PRACTICAL 1 — HILL CLIMBING

### General Flowchart
```
        ┌────────────────────┐
        │  Start: random      │
        │  initial state      │
        └─────────┬───────────┘
                   ▼
        ┌────────────────────┐
        │ Evaluate current    │
        │ state (heuristic)   │
        └─────────┬───────────┘
                   ▼
        ┌────────────────────┐
        │ Generate neighbour  │
        │ states               │
        └─────────┬───────────┘
                   ▼
             Is any neighbour
             BETTER than current? ──No──► STOP (return current
                   │                       as solution / local optimum)
                  Yes
                   ▼
        ┌────────────────────┐
        │ Move to the best    │
        │ neighbour            │
        └─────────┬───────────┘
                   │
                   └──────────► (loop back to "Evaluate")
```

### General Pseudocode
```
function HILL_CLIMBING(initial_state):
    current = initial_state
    loop:
        neighbours = GENERATE_NEIGHBOURS(current)
        best = the neighbour with the best score
        if SCORE(best) is not better than SCORE(current):
            return current                # local/global optimum reached
        current = best
```

**1a. Game Playing (8-Queens):** heuristic = number of queen pairs attacking each other (minimise). Uses random-restart when stuck.

**1b. Planning (Blocks World):** heuristic = number of blocks already in their goal position (maximise); neighbours = swap any two blocks.

**1c. Scheduling & Path Finding:**
- *Scheduling*: heuristic = total waiting time of jobs (minimise); neighbours = swap two jobs in the sequence.
- *Path finding*: heuristic = Manhattan distance to goal (minimise); neighbours = up/down/left/right grid cells.

---

## PRACTICAL 2 — SIMULATED ANNEALING

### General Flowchart
```
   ┌───────────────────────┐
   │ Start: random solution,│
   │ set high Temperature T │
   └───────────┬─────────────┘
               ▼
   ┌───────────────────────┐
   │ Pick a random neighbour│
   └───────────┬─────────────┘
               ▼
        Δ = cost(neighbour) − cost(current)
               ▼
        Is Δ better (improves cost)?
          │Yes                │No
          ▼                   ▼
   Accept neighbour     Accept with probability
   as current           e^(−Δ / T)  (may accept worse
          │              solution to escape local optima)
          └─────────┬──────────┘
                     ▼
           Decrease Temperature T
           (T = T × cooling_rate)
                     ▼
             Is T below minimum? ──No──► loop back to "pick neighbour"
                     │Yes
                     ▼
              STOP — return best solution found
```

### General Pseudocode
```
function SIMULATED_ANNEALING(initial_state):
    current = initial_state
    T = T_initial
    best = current
    while T > T_min:
        neighbour = RANDOM_NEIGHBOUR(current)
        Δ = COST(neighbour) - COST(current)
        if Δ < 0 or RANDOM(0,1) < exp(-Δ / T):
            current = neighbour
            if COST(current) < COST(best):
                best = current
        T = T * cooling_rate
    return best
```

**2a. TSP:** cost = total tour distance; neighbour = swap two cities in the route.
**2b. Knapsack:** cost = −value if within weight capacity else penalised to 0; neighbour = flip include/exclude of one item.
**2c. Job-shop scheduling:** cost = total completion time of all jobs; neighbour = swap two jobs' order.
**2d. Vehicle routing:** cost = total distance of the route starting/ending at the depot; neighbour = swap two stops.

---

## PRACTICAL 3 — MINIMAX ALGORITHM

### General Flowchart
```
        ┌─────────────────────┐
        │ Current board state   │
        └──────────┬─────────────┘
                    ▼
           Is it a terminal state
           (win/lose/draw) or max depth? ──Yes──► return static
                    │No                            evaluation score
                    ▼
        Whose turn is it?
      ┌─────────────┴─────────────┐
      ▼                           ▼
 MAXIMIZING player           MINIMIZING player
 (AI) picks the move          (opponent) picks the
 with the HIGHEST score       move with the LOWEST score
      │                           │
      ▼                           ▼
  For each legal move: recursively call MINIMAX
  on the resulting board, then take max / min
      │                           │
      └─────────────┬─────────────┘
                     ▼
        Return best score & move up the tree
```

### General Pseudocode
```
function MINIMAX(board, depth, isMaximizing):
    if GAME_OVER(board) or depth == 0:
        return EVALUATE(board)

    if isMaximizing:
        best = -infinity
        for each legal move:
            score = MINIMAX(apply(move), depth-1, False)
            best = max(best, score)
        return best
    else:
        best = +infinity
        for each legal move:
            score = MINIMAX(apply(move), depth-1, True)
            best = min(best, score)
        return best
```

**3a. Tic-Tac-Toe:** full search to terminal state (no depth limit needed, small tree); evaluation = +1 AI win / −1 opponent win / 0 draw.
**3b. Chess:** depth-limited (e.g. depth=2) because the game tree is huge; evaluation = material balance (sum of piece values).
**3c. Connect Four:** depth-limited (e.g. depth=4); evaluation = piece-count difference, +100/−100 for a win/loss.

---

## PRACTICAL 4 — MONTE CARLO TREE SEARCH (MCTS)

### General Flowchart
```
        ┌─────────────────────┐
        │   Root = current      │
        │   state                │
        └──────────┬─────────────┘
                    ▼
      ┌─────────────────────────────┐
      │ 1. SELECTION                  │
      │  Walk down the tree picking    │
      │  child with best UCB1 score    │
      └──────────────┬─────────────────┘
                      ▼
      ┌─────────────────────────────┐
      │ 2. EXPANSION                  │
      │  Add one new child node for a  │
      │  previously untried move       │
      └──────────────┬─────────────────┘
                      ▼
      ┌─────────────────────────────┐
      │ 3. SIMULATION (Rollout)       │
      │  Play out randomly to the end  │
      │  (or fixed depth), get reward  │
      └──────────────┬─────────────────┘
                      ▼
      ┌─────────────────────────────┐
      │ 4. BACKPROPAGATION             │
      │  Update visit-count & value    │
      │  for every node on the path    │
      │  back to the root              │
      └──────────────┬─────────────────┘
                      ▼
        Repeat steps 1-4 for N iterations
                      ▼
        Return the child of ROOT with the
        highest visit count as the best move
```

### General Pseudocode
```
function MCTS(root_state, iterations):
    root = Node(root_state)
    repeat "iterations" times:
        node = root
        # 1. Selection
        while node is fully expanded and has children:
            node = SELECT_BEST_UCB1(node)
        # 2. Expansion
        if node has untried moves:
            node = EXPAND(node)
        # 3. Simulation
        reward = ROLLOUT(node.state)
        # 4. Backpropagation
        while node is not null:
            node.visits += 1
            node.value += reward
            node = node.parent
    return CHILD_OF_ROOT_WITH_MOST_VISITS(root)
```

**4a. Sliding Puzzle / Sudoku:** state = board configuration; reward = 1 if solved else based on how close it is (fewer misplaced tiles).
**4b. Knapsack:** each tree level = take/skip one item; reward = total value of a completed (random) selection.
**4c. TSP:** each tree level = choose the next city to visit; reward = negative tour length (shorter tour = higher reward).

---

## Files delivered
```
P1_HillClimbing/       1a_game_playing_8queens.py, 1b_planning_blocks.py, 1c_scheduling_pathfinding.py
P2_SimulatedAnnealing/ 2a_tsp.py, 2b_knapsack.py, 2c_job_shop_scheduling.py, 2d_vehicle_routing.py
P3_Minimax/             3a_tictactoe.py, 3b_chess.py, 3c_connect_four.py
P4_MCTS/                4a_sliding_puzzle.py, 4b_knapsack.py, 4c_tsp.py
```
Every script is self-contained: run with `python3 filename.py`.
Each one prints its result in the console AND saves a `.png` visualization
(board / route / chart) in the same folder — open the PNG to see the graph/map.

Note: `3b_chess.py` needs one extra library: `pip install python-chess`
