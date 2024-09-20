import unittest
from modules.game_state import GameState
from modules.game_visualization import GameVisualization
from modules.solver import Solver

# This will grab memory usage after a specific amount of time.
# May vary on different hardware and implementation.

def load_map(map_path):
    """Load the map from the given path"""
    f = open(map_path, 'r')
    map = []
    maxl = 0
    for line in f:
        map.append(list(line))
        l = len(list(line))
        if l > maxl:
            maxl = l

    for line in map:
        ldiff = abs(maxl - len(line))
        line += [' '] * ldiff
    f.close()
    return map

class SokobanTest_Sokoban1(unittest.TestCase):
    def engine(self, map_name, method):
        print(f">> Testing map: {map_name}")
        map = load_map(f'maps/{map_name}')

        game_state = GameState(map)
        strategy = method
        # strategy = 'bfs'
        # strategy = 'dfs'
        # strategy = 'dfs_limited_depth'
        # strategy = 'astar'
        # strategy = 'ucs'
        # strategy = 'greedy'
        # strategy = 'custom'
        print(f"Using strategy: {strategy}")
        solver = Solver(game_state, strategy)
        solver.solve()
        solution = solver.get_solution()

        game_visualization = GameVisualization(game_state, solution)
        game_visualization.start(f'{map_name}, {method}')

    def test_bfs_sokoban1(self):
        self.engine('sokoban1.txt', 'bfs')

    def test_dfs_sokoban1(self):
        self.engine('sokoban1.txt', 'dfs')

    def test_dfs_ld_sokoban1(self):
        self.engine('sokoban1.txt', 'dfs_limited_depth')

    def test_ucs_sokoban1(self):
        self.engine('sokoban1.txt', 'ucs')

    def test_astar_sokoban1(self):
        self.engine('sokoban1.txt', 'astar')

    def test_greedy_sokoban1(self):
        self.engine('sokoban1.txt', 'greedy')

    def test_custom_sokoban1(self):
        self.engine('sokoban1.txt', 'custom')

class SokobanTest_Sokoban2(unittest.TestCase):
    def engine(self, map_name, method):
        print(f">> Testing map: {map_name}")
        map = load_map(f'maps/{map_name}')

        game_state = GameState(map)
        strategy = method
        # strategy = 'bfs'
        # strategy = 'dfs'
        # strategy = 'dfs_limited_depth'
        # strategy = 'astar'
        # strategy = 'ucs'
        # strategy = 'greedy'
        # strategy = 'custom'
        print(f"Using strategy: {strategy}")
        solver = Solver(game_state, strategy)
        solver.solve()
        solution = solver.get_solution()

        game_visualization = GameVisualization(game_state, solution)
        game_visualization.start(f'{map_name}, {method}')

    def test_bfs_sokoban2(self):
        self.engine('sokoban2.txt', 'bfs')

    def test_dfs_sokoban2(self):
        self.engine('sokoban2.txt', 'dfs')

    def test_dfs_ld_sokoban2(self):
        self.engine('sokoban2.txt', 'dfs_limited_depth')

    def test_ucs_sokoban2(self):
        self.engine('sokoban2.txt', 'ucs')

    def test_astar_sokoban2(self):
        self.engine('sokoban2.txt', 'astar')

    def test_greedy_sokoban2(self):
        self.engine('sokoban2.txt', 'greedy')

    def test_custom_sokoban2(self):
        self.engine('sokoban2.txt', 'custom')

if __name__ == '__main__':
    unittest.main()
