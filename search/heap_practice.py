from frontier import PriorityFrontier
from graph import Node, Graph

# path = "./search/points2.csv"
# graph = Graph(path)
# graph.get_paths()
# goal = Node(19, 12)

# start = graph.search_node(0, 3)
# start.show_neighbors()
# distances = []
# for node in start.neighbors:
#     node.set_manhattan_distance(goal)
#     distances.append(node.distance)
    
# print(distances)

# # arr = PriorityFrontier([])

# # item = arr.add(node)
# # print(arr)

import pandas as pd

df = pd.read_csv("./search/maze-a-star.csv", header=None)
df[df.isna()] = " "
print(df)
df.to_csv("./search/maze-a-star.csv", index=None, header=None)