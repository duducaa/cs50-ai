from frontier import QueueFrontier, StackFrontier, PriorityFrontier
from graph import Graph, Node

import pandas as pd

from typing import List

class Search_Algorithms:
    def __init__(self, graph: Graph, start: Node, goal: Node):
        self.graph = graph
        self.start = start
        self.goal = goal

    def depth_first_search(self) -> List[Node]:
        frontier = StackFrontier()
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
    
    def A_star(self):
            
        def g_h(n: Node) -> List[int]:
            g = n.steps
            
            h = abs(self.goal.x - n.x) + abs(self.goal.y - n.y)
            return g + h
        
        frontier = PriorityFrontier(g_h)
        
        self.visited_nodes: List[Node] = []

        if self.start == None or self.goal == None:
            print("Both the nodes must exists")
            return None
        
        node = self.start
        node.steps = 0
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