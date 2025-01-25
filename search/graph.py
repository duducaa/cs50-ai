from typing import List, Dict
import numpy as np
import pandas as pd
import cv2 as cv

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
    def __init__(self, csv_path: str, nodes: List[Node] = []):
        self.nodes: List[Node] = nodes
        self.solve_path = csv_path
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
    
    # for very large graphs
    def search_node(self, node: Node) -> Node:
        return list(filter(lambda n: n == node, self.nodes))[0]
    
    def draw_solve(self, visited_nodes: List[Node], solve_path: List[Node], solve_img: str, solve_csv: str):
        df = self.dataframe.copy()
        
        for node in visited_nodes:
            df.iloc[node.y, node.x] = "*"

        for node in solve_path:
            df.iloc[node.y, node.x] = "o"
            
        self.dataframe.to_csv(solve_csv, index=False, header=False)
        
        img = np.zeros_like(df.to_numpy(), shape=(df.shape[0], df.shape[1], 3), dtype=np.uint8)
        
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                pixels = {
                    "#": (0, 0, 0),
                    "*": (255, 255, 0),
                    "o": (255, 0, 0),
                    "": (255, 255, 255),
                    " ": (255, 255, 255)
                }
                img[i, j] = pixels[df.iloc[i, j]]
        
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = cv.resize(img, (10 * img.shape[0], 10 * img.shape[1]))
        cv.imwrite(solve_img, img)