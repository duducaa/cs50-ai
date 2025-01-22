from typing import List, Dict
import pandas as pd

class Node:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.neighbors: List[Node] = []

    def show_neighbors(self):
        print(f"[{', '.join([neighbor.__str__() for neighbor in self.neighbors])}]")
        
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, value):
        if isinstance(value, Node):
            return self.x == value.x and self.y == value.y
        
class Graph:
    def __init__(self, csv_path: str):
        self.nodes: List[Node] = []
        self.dataframe: pd.DataFrame = pd.read_csv(csv_path, header=None)
                
    def __str__(self):
        result = ""
        for node in self.nodes:
            result += node.__str__() + "".join([edge.__str__() for edge in node.edges]) + "\n"
        
        return result
    
    def show_nodes(self):
        for node in self.nodes:
            print(node)
    
    def get_paths(self):
        
        nodes: Dict[str, Node] = {}
        self.nrows, self.ncols = self.dataframe.shape
        caracteres = self.dataframe.values.tolist()
        for i, line in enumerate(caracteres):
            for j in range(self.ncols):
                if line[j] == "#" or i == self.nrows or j == self.ncols:
                    continue
                                    
                node = Node(j, i)
                nodes[(j, i)] = node
                
                if i != 0 and nodes.get((j, i - 1)):
                    nodes[(j, i)].neighbors.append(nodes[(j, i - 1)])
                    nodes[(j, i - 1)].neighbors.append(nodes[(j, i)])
                
                if j != 0 and nodes.get((j - 1, i)):
                    nodes[(j, i)].neighbors.append(nodes[(j - 1, i)])
                    nodes[(j - 1, i)].neighbors.append(nodes[(j, i)])
                
        self.nodes: List[Node] = list(nodes.values())

        with open("./search/nodes.txt", "w") as f:
            for node in self.nodes:
                f.write(f"{node}\n")
    
    # for very large graphs
    def search_node(self, node: Node) -> Node:
        return list(filter(lambda n: n == node, self.nodes))[0]
    
    def draw_solve(self, visited_nodes: List[Node], solve_path: List[Node], solve_csv: str):
        for node in visited_nodes:
            self.dataframe.iloc[node.y, node.x] = "*"

        for node in solve_path:
            self.dataframe.iloc[node.y, node.x] = "o"
            
        self.dataframe.to_csv(solve_csv, index=False, header=False)