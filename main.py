import argparse
from modules.game_state import GameState
from modules.game_visualization import GameVisualization
from modules.solver import Solver

def load_map(map_path):
    """Load the map from the given path"""
    f = open(map_path, 'r')
    map = []
    maxl = 0
    for line in f:
        _line = line.rstrip()
        map.append(list(_line))
        l = len(list(_line))
        if l > maxl:
            maxl = l

    for line in map:
        ldiff = abs(maxl - len(line))
        line += [' '] * ldiff
    f.close()
    return map

def engine(map_name, method):
    map = load_map(f'{map_name}')

    game_state = GameState(map)
    print(f"Using strategy: {method}")
    solver = Solver(game_state, method, map_name)
    solver.solve()
    solution = solver.get_solution()

    if solution is None:
        solution = []

    game_visualization = GameVisualization(game_state, solution)
    game_visualization.start(f"{map_name}, {method}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--map', help='Directory to map file', default='maps/demo.txt')
    parser.add_argument('--method', help='Solve method (bfs, dfs, astar, etc.)', default='astar')
    args = parser.parse_args()

    engine(args.map, args.method)

    print("Action completed")