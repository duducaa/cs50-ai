from graph import Node
from typing import List, Callable

class Frontier:
    def __init__(self, items: List[Node] = []):
        self.items = items
        
    def add(self, item: Node):
        self.items.append(item)
        
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def __len__(self):
        return self.items.__len__()
    
    def __str__(self):
        return f"[{', '.join([item.__str__() for item in self.items])}]"

class StackFrontier(Frontier):
    def top(self) -> Node:
        return self.items[-1]

    def remove(self) -> Node:
        if self.is_empty():
            return None
        
        item = self.items[-1]
        self.items = self.items[:-1]
        return item
    
class QueueFrontier(Frontier):
    def remove(self) -> Node:
        if self.is_empty():
            return None
        
        item = self.items[0]
        self.items = self.items[1:]
        return item
    
class PriorityFrontier(Frontier):   
    def __init__(self, metric: Callable[[Node], int], items = []):
        super().__init__(items)
        self.metric = metric
     
    def add(self, item: Node):
        super().add(item)
        idx = len(self.items) - 1
        parent_idx = (idx - 1) // 2
        
        
        distance = self.metric(self.items[idx])
        parent_distance = self.metric(self.items[parent_idx])

        while distance < parent_distance and idx > 0:
            self.items[idx], self.items[parent_idx] = self.items[parent_idx], self.items[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2
            
            distance = self.metric(self.items[idx])
            parent_distance = self.metric(self.items[parent_idx])

    def remove(self) -> Node:
        if self.is_empty():
            return None
        
        if self.items.__len__() > 1:
            self.items[0], self.items[-1] = self.items[-1], self.items[0]
            
        item = self.items[-1]
        self.items = self.items[:-1]
        
        idx = 0
        min_idx = 0
        while idx * 4 + 1 < self.__len__():
            min_distance = self.metric(self.items[min_idx])
            for j in range(idx * 4 + 1, min(idx * 4 + 5, self.__len__())):
                distance = self.metric(self.items[j])
                if distance < min_distance:
                    min_idx = j
            
            self.items[idx], self.items[min_idx] = self.items[min_idx], self.items[idx]
            idx = min_idx
            if idx == min_idx:
                break
                
        return item