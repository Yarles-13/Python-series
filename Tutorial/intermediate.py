# ==========================
# 1. Recursion
# ==========================
def factorial (number):
    if number == 1:
        return 1
    return number * factorial(number-1)

#Fibonacci

def fibonacci (number):
    if number <= 1:
        return  number
    return fibonacci(number - 1) + fibonacci(number - 2)

# ==========================
# 2. Sorting
# ==========================

numbers = [1,6,3,8,2]
#basic sort
print(sorted(numbers))

#custom sort using a lambda
sorted(numbers, key=lambda num : -num) #prints [8, 6, 3, 2, 1]

# ==========================
# 3. Graph and Tree Traversal (DFS & BFS)
# ==========================

from collections import deque

#Depth-First Search (DFS)
def DFS (graph, node, visited = set()):
    # using set() to create a set obj {n1, n2, n++}
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            DFS(graph, neighbor, visited)

#Breadth First Search (BFS)
def BFS (graph, start):
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("DFS Traversal:")
DFS(graph, 'A')

print("BFS Traversal:")
BFS(graph, 'A')