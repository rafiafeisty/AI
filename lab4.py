class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def car_details(self):
        return f"Car: {self.year},{self.brand},{self.model}"
    def start(self):
        return f"{self.brand},{self.model} is starting"
    
car1=Car("Toyata","Corolla",2021)
car2=Car("Honda","Civic",2023)
print(car1.car_details())
print(car2.car_details())
print(car1.start())
print(car2.start())

#Task 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        temp = Node(data)
        if self.rear is None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return temp.data

class PriorityQueueNode:
    def __init__(self, data, prior):
        self.data = data
        self.prior = prior
        self.next = None 

class PriorityQueue:
    def __init__(self):
        self.front = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data, prior):
        temp = PriorityQueueNode(data, prior)
        if self.front is None or self.front.prior > prior:
            temp.next = self.front
            self.front = temp
        else:
            current = self.front
            while current.next is not None and current.next.prior <= prior:
                current = current.next
            temp.next = current.next
            current.next = temp

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            temp = self.front
            self.front = self.front.next
            return temp.data 

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue()) 
print(q.dequeue())
print(q.dequeue())

pq = PriorityQueue()
pq.enqueue("Task 1", 3)
pq.enqueue("Task 2", 1)
pq.enqueue("Task 3", 2)
print(pq.dequeue())  
print(pq.dequeue()) 
print(pq.dequeue())  

#Task 2

def graph():
    graph = {
        0:[1,4],
        1:[0,3,4,2],
        2:[1,3],
        3:[1,2,4],
        4:[0,1,3]
    }
    for i,j in graph.items():
        print(f"Vertex {i} is connected to {j}")

graph()

#Task 3
class tree:
    def __init__(self, data=None):
        self.data = data
        self.children = []
        self.parent=None
    def add_child(self,add_data):
        self.children.append(add_data)
        self.parent=self
    def root(self,add_data):
        self.data=add_data
        self.parent=None
    def display(self):
        if self.data is None:
            return
        else:
            print(self.data, end=" ")
            for child in self.children:
                child.display()  
    def BSF(self,var):
        visited = set()
        queue = []
        queue.append(self)
        while queue:
            s = queue.pop(0)
            print(s.data, end=" ")
            if s.data==var:
                return
            for child in s.children:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
                    




root = tree()  
root.root('A') 

node1 = tree('B')  
node2 = tree('C')
node3 = tree('C')
node4 = tree('D')
node5 = tree('E')
node6 = tree('F')
node7 = tree('G')
node8 = tree('H')
node9 = tree('I')
node10 = tree('J')
node11 = tree('K')
node12 = tree('L')
node13 = tree('M')
node14 = tree('N')

root.add_child(node1) 
root.add_child(node6)
root.add_child(node4)
root.add_child(node5)
node1.add_child(node11)  
node1.add_child(node10)
node11.add_child(node14)
node11.add_child(node13)
node4.add_child(node7) 
node5.add_child(node3) 
node5.add_child(node8) 
node5.add_child(node9) 
node9.add_child(node12) 

print("Breadth First Search")
root.BSF('G')

# Task 3
class binar_tree:
    def __init__(self,data=None):
        self.children = []
        self.data = data
    def root(self,add_data):
        self.data = add_data
        self.parent=None
    def add_child(self,add_data):
        if len(self.children)<=2:
            self.children.append(add_data)
            add_data.parent=self
        else:
            print("This node has already 2 children")
    def BSF(self):
        visited = set()
        queue = []
        queue.append(self)
        while queue:
            s = queue.pop(0)
            print(s.data, end=" ")
            for child in s.children:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
root = binar_tree()  
root.root(1)
node1=binar_tree(2) 
node3=binar_tree(3) 
node4=binar_tree(4) 
node5=binar_tree(5) 
root.add_child(node1)
root.add_child(node3)
node1.add_child(node4)
node1.add_child(node5)
print("\n")
root.BSF()

from collections import deque
def shortest_path(maze):
    n, m = len(maze), len(maze[0])
    if maze[0][0] == 1 or maze[n-1][m-1] == 1:
        return -1, []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0, [(0, 0)])])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True

    while queue:
        x, y, path = queue.popleft()
        if (x, y) == (n - 1, m - 1):
            return len(path), path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, path + [(nx, ny)]))
    return -1, []
maze = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 0]
]
steps, path = shortest_path(maze)
if steps == -1:
    print("No valid path exists.")
else:
    print(f"The shortest path length is {steps}.")
    print("The path is:")
    for p in path:
        print(f"({p[0]}, {p[1]})", end=" -> " if p != path[-1] else "")
    print()