from graph import Graph, Node
from search_algorithms import Search_Algorithms

path = "./search/points.csv"
graph = Graph(path)
graph.get_paths()
start = graph.search_node(Node(6, 19))
end = graph.search_node(Node(19, 2))
search = Search_Algorithms(graph, start, end)
node_path = search.A_star()
graph.draw_solve(search.visited_nodes, node_path, "./search/points-a_star.csv")
