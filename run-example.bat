@ECHO off
python main.py --map maps/maps/sokoban1.txt --method bfs
python main.py --map maps/maps/sokoban1.txt --method dfs
python main.py --map maps/maps/sokoban1.txt --method dfs_limited_depth
python main.py --map maps/maps/sokoban1.txt --method astar
python main.py --map maps/maps/sokoban1.txt --method ucs
python main.py --map maps/maps/sokoban1.txt --method greedy
python main.py --map maps/maps/sokoban1.txt --method idas
PAUSE