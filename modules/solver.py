# Solver for sokuban game using following search strategies:
# - Breadth-first search
# - Depth-first search
# - A* search
# - Uniform-cost search
# - Greedy search
# - IDA* search
# The solver class has the following methods:
# - solve(): solve the game
# """

import time
from collections import deque
from queue import PriorityQueue
from heapq import *

class Solver(object):
    def __init__(self, initial_state, strategy, map_name=''):
        self.initial_state = initial_state
        self.strategy = strategy
        self.solution = None
        self.time = None
        self.states_generated = 0
        self.expanded_nodes = 0
        self.moves_to_target = 0

        self.map_name = map_name

    def solve(self):
        start_time = time.time()
        if self.strategy == 'bfs':
            self.solution = self.bfs()
        elif self.strategy == 'dfs':
            self.solution = self.dfs()
        elif self.strategy == 'dfs_limited_depth':
            self.solution = self.dfs_limited_depth()
        elif self.strategy == 'astar':
            self.solution = self.astar()
        elif self.strategy == 'ucs':
            self.solution = self.ucs()
        elif self.strategy == 'greedy':
            self.solution = self.greedy()
        elif self.strategy == 'idas':
            self.solution = self.idas()
        else:
            raise Exception('Invalid strategy')
        self.time = time.time() - start_time
        self.print_solution()

    def print_solution(self):
        if self.solution is not None:
            print(f"{self.map_name}, {self.strategy} > Solution found:", self.solution)
            print(f"{self.map_name}, {self.strategy} > Number of states generated:", self.states_generated)
            print(f"{self.map_name}, {self.strategy} > Number of expanded nodes:", self.expanded_nodes)
            print(f"{self.map_name}, {self.strategy} > Number of moves to reach the target state:", self.moves_to_target)
            print(f"{self.map_name}, {self.strategy} > Running time to find the solution:", self.time, "seconds")
        else:
            print(f"{self.map_name}, {self.strategy} > No solution found.")

    def bfs(self):
        print("Starting BFS")
        queue = deque([(self.initial_state, [])])
        visited = set()
        self.states_generated = 0
        self.expanded_nodes = 0
        print(f"Initial queue: {queue}")
        while queue:
            state, solution = queue.popleft()
            # print(f"Exploring state with solution {solution}")
            if state.check_solved():
                self.solution = solution
                self.moves_to_target = len(solution)
                return solution
            for direction in ['U', 'D', 'L', 'R']:
                # print(f"Generated new state for direction {direction}")
                new_state = state.move(direction)
                self.states_generated += 1

                # Check if the move results in a valid state
                if new_state not in visited:
                    # print(f"Adding new state to queue with solution {solution + [direction]}")
                    visited.add(new_state)
                    queue.append((new_state, solution + [direction]))
                    self.expanded_nodes = len(visited)
        return None

    def dfs(self):
        print("Starting DFS")
        stack = [(self.initial_state, [])]
        visited = set()
        self.states_generated = 0
        self.expanded_nodes = 0
        print(f"Initial stack: {stack}")
        while stack:
            state, path = stack.pop()
            self.expanded_nodes += 1
            # print(f"Exploring state with solution {path}")
            if state.check_solved():
                self.solution = path
                self.moves_to_target = len(path)
                return path
            visited.add(state)
            for direction in ['U', 'D', 'L', 'R']:
                new_state = state.move(direction)
                self.states_generated += 1
                # double check on valid state, not yet visited
                if new_state is not state and new_state not in visited:
                    stack.append((new_state, path + [direction]))
        return None

    def dfs_limited_depth(self, max_depth=10):
        print("Starting Depth-Limited DFS")
        stack = [(self.initial_state, [], 0)]  # Include depth in the stack tuple
        visited = set()
        self.states_generated = 0
        self.expanded_nodes = 0
        while stack:
            state, path, depth = stack.pop()
            self.expanded_nodes += 1
            # print(f"Exploring state with solution {path} at depth {depth}")

            if depth > max_depth:
                continue

            if state.check_solved():
                self.solution = path
                self.moves_to_target = len(path)
                return path

            visited.add(state)
            for direction in ['U', 'D', 'L', 'R']:
                new_state = state.move(direction)
                self.states_generated += 1
                if new_state is not state and new_state not in visited:
                    stack.append((new_state, path + [direction], depth + 1))
        return None

    def astar(self):
        print("Starting A-star")
        visited = set()
        priority_heap = []

        self.states_generated = 0
        self.expanded_nodes = 0
        # Tuple (total cost, order number of state, state object)
        initial_state_info = (self.initial_state.get_total_cost(), self.states_generated, self.initial_state, [])
        heappush(priority_heap, initial_state_info)

        print(f"Initial queue: {priority_heap}")
        while priority_heap:
            cost, _, current_node, path = heappop(priority_heap)

            if current_node in visited:
                continue

            self.expanded_nodes += 1

            # print(f"Exploring state with solution {path} which, considering heuristics, costs {cost}")

            if current_node.is_solved:
                self.solution = path
                self.moves_to_target = len(path)
                print(f"Search successful at depth {current_node.current_cost}")
                return path

            visited.add(current_node)
            for direction in ['U', 'D', 'L', 'R']:
                new_state = current_node.move(direction)
                if new_state is current_node:
                    continue

                self.states_generated += 1
                if new_state not in visited:
                    new_state_info = (new_state.get_total_cost(), self.states_generated, new_state, path + [direction])
                    heappush(priority_heap, new_state_info)
        return None

    def astar_pq(self):
        print("Starting A-star (PriorityQueue)")
        visited = set()
        priority_queue = PriorityQueue()

        self.states_generated = 0
        self.expanded_nodes = 0
        # Tuple (total cost, order number of state, state object)
        priority_queue.put((self.initial_state.get_total_cost(), self.states_generated, self.initial_state, []))

        print(f"Initial queue: {priority_queue.queue}")
        while not priority_queue.empty():
            cost, _, current_node, path = priority_queue.get()

            if current_node in visited:
                continue

            self.expanded_nodes += 1

            # print(f"Exploring state with solution {path} which, considering heuristics, costs {cost}")

            if current_node.is_solved:
                self.solution = path
                self.moves_to_target = len(path)
                print(f"Search successful at depth {current_node.current_cost}")
                return path


            visited.add(current_node)
            for direction in ['U', 'D', 'L', 'R']:
                new_state = current_node.move(direction)
                if new_state is current_node:
                    continue

                self.states_generated += 1
                if new_state not in visited:
                    priority_queue.put((new_state.get_total_cost(), self.states_generated, new_state, path + [direction]))
        return None

    def ucs(self):
        print("Starting UCS")
        visited = set()
        priority_queue = PriorityQueue()

        self.states_generated = 0
        self.expanded_nodes = 0
        # Tuple (current path cost, order number of state, state object)
        priority_queue.put((self.initial_state.current_cost, self.states_generated, self.initial_state, []))

        print(f"Initial queue: {priority_queue.queue}")
        while not priority_queue.empty():
            cost, _, current_node, path = priority_queue.get()

            # print(f"Exploring state with solution {path}, costing {cost}")

            if current_node in visited:
                continue

            self.expanded_nodes += 1

            if current_node.is_solved:
                self.solution = path
                self.moves_to_target = len(path)
                return path

            visited.add(current_node)

            for direction in ['U', 'D', 'L', 'R']:
                new_state = current_node.move(direction)
                self.states_generated += 1
                if new_state is not current_node and new_state not in visited:
                    priority_queue.put((new_state.current_cost, self.states_generated, new_state, path + [direction]))
        return None

    def greedy(self):
        print("Starting Greedy")
        visited = set()
        priority_queue = PriorityQueue()

        self.states_generated = 0
        self.expanded_nodes = 0
        # Tuple (heuristic, order number of state, state object)
        priority_queue.put((self.initial_state.get_heuristic(), self.states_generated, self.initial_state, []))

        print(f"Initial queue: {priority_queue.queue}")
        while not priority_queue.empty():
            h, _, current_node, path = priority_queue.get()

            # print(f"Exploring state with solution {path} with heuristic {h}")

            if current_node in visited:
                continue

            self.expanded_nodes += 1

            if current_node.is_solved:
                self.solution = path
                self.moves_to_target = len(path)
                return path

            visited.add(current_node)

            for direction in ['U', 'D', 'L', 'R']:
                new_state = current_node.move(direction)
                self.states_generated += 1
                if new_state is not current_node and new_state not in visited:
                    priority_queue.put((new_state.get_heuristic(), self.states_generated, new_state, path + [direction]))
        return None

    def idas(self):
        # Iterative-deepening A-star
        bound = self.initial_state.get_heuristic()
        self.states_generated = 0
        self.expanded_nodes = 0
        previous_expanded_nodes = 0

        print(f"Starting IDA* with initial threshold is {bound}")

        mincost = 0
        node_path = [self.initial_state]

        while mincost != float('inf'):
            # Perform a DFS search with specified bounds (threshold), which increases after each iteration.
            path, mincost = self.__idastar_search(node_path, self.initial_state.current_cost, bound, [])
            # print(f"Updating threshold from {bound} to {mincost}\nExpanded nodes in this iteration: {self.expanded_nodes - previous_expanded_nodes}")
            if mincost == -1:
                return path

            previous_expanded_nodes += self.expanded_nodes - previous_expanded_nodes
            bound = mincost
        return None

    def __idastar_search(self, node_path, g, bound, path):
        # Recursive DFS function that assists IDA* algorithm
        state = node_path[-1]
        f = state.get_total_cost()
        if (f > bound):
            return None, f

        self.expanded_nodes += 1

        # print(f"Exploring state with solution {path}, costing {f} at threshold {bound}")

        if state.is_solved:
            self.solution = path
            self.moves_to_target = len(path)
            return path, -1

        min = float("inf")
        for direction in ['U', 'D', 'R', 'L']:
            new_state = state.move(direction)
            if new_state is state:
                continue
            if new_state in node_path:
                continue

            self.states_generated += 1
            node_path.append(new_state)
            new_path, tmp = self.__idastar_search(node_path, new_state.current_cost, bound, path + [direction])
            if tmp == -1:
                return new_path, -1
            if tmp < min:
                min = tmp
            node_path.pop(-1)
        return None, min

    def get_solution(self):
        return self.solution
