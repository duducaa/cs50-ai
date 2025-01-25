from frontier import QueueFrontier, StackFrontier, PriorityFrontier
from graph import Graph, Node

from collections import Counter

from typing import List, Union

FrontierType = Union[
    QueueFrontier,
    StackFrontier,
    PriorityFrontier
]

class Search_Algorithms:
    def __init__(self, graph: Graph, start: Node, goal: Node):
        self.graph = graph
        self.start = start
        self.goal = goal
        
    def search_loop(self, frontier: FrontierType):
        self.visited_nodes: List[Node] = []

        if self.start == None or self.goal == None:
            print("Both the nodes must exists")
            return None
        
        node = self.start
        node.parent = None
        node.steps = 0
        frontier.add(node)
        while True:
            node: Node = frontier.remove()
            self.visited_nodes.append(node)
            df = self.graph.dataframe
            df.iloc[node.y, node.x] = "o"
            df.to_csv(self.graph.solve_path, header=None, index=None)
            
            if len(node.neighbors) > 0:
                for neighbor in node.neighbors:
                    if neighbor not in self.visited_nodes:
                        neighbor.steps = node.steps + 1
                        neighbor.parent = node
                        frontier.add(neighbor)

            if node == self.goal:
                break

            if len(frontier.items) == 0:
                return []
        
        path = [node]
        while node.parent != None:
            node = node.parent
            path.append(node)

        return reversed(path)

    def depth_first_search(self) -> List[Node]:
        frontier = StackFrontier()
        return self.search_loop(frontier)
        self.visited_nodes: List[Node] = []
        
        if self.start == None or self.goal == None:
            print("Both the nodes must exists")
            return None
        
        node = self.start
        node.parent = None
        frontier.add(node)

        while True:
            node: Node = frontier.remove()
            self.visited_nodes.append(node)
            
            if len(node.neighbors) > 0:
                for neighbor in node.neighbors:
                    if neighbor not in self.visited_nodes:
                        neighbor.parent = node
                        frontier.add(neighbor)

            if node == self.goal:
                break

            if len(frontier.items) == 0:
                raise Exception("no solution")
        
        path = [node]
        while node.parent != None:
            node = node.parent
            path.append(node)

        return reversed(path)
    
    def breadth_first_search(self) -> List[Node]:
        frontier = QueueFrontier()
        return self.search_loop(frontier)
        self.visited_nodes: List[Node] = []
        
        if self.start == None or self.goal == None:
            print("Both the nodes must exists")
            return None
        
        node = self.start
        node.parent = None
        frontier.add(node)

        while True:
            node: Node = frontier.remove()
            self.visited_nodes.append(node)
            
            if len(node.neighbors) > 0:
                for neighbor in node.neighbors:
                    if neighbor not in self.visited_nodes:
                        neighbor.parent = node
                        frontier.add(neighbor)

            if node == self.goal:
                break

            if len(frontier.items) == 0:
                raise Exception("no solution")
        
        path = [node]
        while node.parent != None:
            node = node.parent
            path.append(node)

        return reversed(path)
    
    def greedy_best_first_search(self):
        
        def h(n: Node) -> int:
            return abs(self.goal.x - n.x) + abs(self.goal.y - n.y)
        
        frontier = PriorityFrontier(h)
        return self.search_loop(frontier)
        self.visited_nodes: List[Node] = []

        if self.start == None or self.goal == None:
            print("Both the nodes must exists")
            return None
        
        node = self.start
        node.parent = None
        frontier.add(node)
        
        while True:
            node: Node = frontier.remove()
            self.visited_nodes.append(node)
            
            if len(node.neighbors) > 0:
                for neighbor in node.neighbors:
                    if neighbor not in self.visited_nodes:
                        neighbor.parent = node
                        frontier.add(neighbor)

            if node == self.goal:
                break

            if len(frontier.items) == 0:
                print(self.goal in self.visited_nodes)
                raise Exception("no solution")
        
        path = [node]
        while node.parent != None:
            node = node.parent
            path.append(node)

        return reversed(path)
    
    def A_star(self):
            
        def g_h(n: Node) -> List[int]:
            if not hasattr(n, "steps"):
                n.steps = 0
            
            g = n.steps
            
            h = abs(self.goal.x - n.x) + abs(self.goal.y - n.y)
            return g + h
        
        frontier = PriorityFrontier(g_h)
        return self.search_loop(frontier)
        
        self.visited_nodes: List[Node] = []

        if self.start == None or self.goal == None:
            print("Both the nodes must exists")
            return None
        
        node = self.start
        node.parent = None
        frontier.add(node)
        while True:
            node: Node = frontier.remove()
            self.visited_nodes.append(node)
            
            if len(node.neighbors) > 0:
                for neighbor in node.neighbors:
                    if neighbor not in self.visited_nodes:
                        neighbor.steps = node.steps + 1
                        neighbor.parent = node
                        frontier.add(neighbor)

            if node == self.goal:
                break

            if len(frontier.items) == 0:
                raise Exception("no solution")
        
        path = [node]
        while node.parent != None:
            node = node.parent
            path.append(node)

        return reversed(path)