def is_path_exist(graph, start, end, visited=None):
    if visited == None:
        visited = set()
        
    if start == end:
        return True
    
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if is_path_exist(graph, neighbor, end, visited):
                return True
            
    return False

graph = {
    1: [2],
    2: [1, 5],
    3: [6],
    4: [6, 7],
    5: [2],
    6: [3, 4, 7],
    7: [4, 6]
}

start_node = int(input("Enter the start node: "))
while start_node not in graph:
    start_node = int(input("Start node not exist, please enter the start node again: "))
    
end_node = int(input("Enter the end node: "))
while end_node not in graph:
    end_node = int(input("End node not exist, please enter the end node again: "))


if is_path_exist(graph, start_node, end_node):
    print("True")
else:
    print("False")