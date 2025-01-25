from graph import Graph, Node
from search_algorithms import Search_Algorithms

import shutil
import os, sys

points = {
    1: {
        "start": Node(0, 40),
        "end": Node(39, 1)
    },
    2: {
        "start": Node(2, 63),
        "end": Node(63, 2)
    },
    3: {
        "start": Node(0, 18),
        "end": Node(19, 2)
    },
    4: {
        "start": Node(0, 30),
        "end": Node(21, 4)
    },    
}

maze_idx = int(sys.argv[2])
maze_path = f"../mazes/csv/maze{maze_idx}.csv"
solve_path = f"./solves/maze{maze_idx}"

alg = sys.argv[1]

os.makedirs("solves", exist_ok=True)
os.makedirs(solve_path, exist_ok=True)
shutil.copy(maze_path, solve_path + f"/{alg}.csv")

graph = Graph(solve_path + f"/{alg}.csv")
graph.get_paths()
start = graph.search_node(points[maze_idx]["start"])
end = graph.search_node(points[maze_idx]["end"])
if start != None and end != None:
    search = Search_Algorithms(graph, start, end)
    
    if alg == "dfs":
        node_path = search.depth_first_search()
    if alg == "bfs":
        node_path = search.breadth_first_search()
    if alg == "gbfs":
        node_path = search.greedy_best_first_search()
    if alg == "a*":
        node_path = search.A_star()    
        
    graph.draw_solve(search.visited_nodes, node_path, solve_path + f"/{alg}.jpg", solve_path + f"/{alg}.csv")