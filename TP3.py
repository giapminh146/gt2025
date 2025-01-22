def create_adjacency_matrix(edges, num_nodes):
    matrix = [[0] * num_nodes for _ in range(num_nodes)]
    
    for start, end in edges:
        matrix[start - 1][end - 1] = 1
    
    return matrix

def perform_inorder_traversal(tree_structure, current_node):
    if current_node not in tree_structure:
        return []
    
    left_subtree = perform_inorder_traversal(tree_structure, tree_structure[current_node][0]) if len(tree_structure[current_node]) > 0 else []
    right_subtree = perform_inorder_traversal(tree_structure, tree_structure[current_node][1]) if len(tree_structure[current_node]) > 1 else []
    
    return left_subtree + [current_node] + right_subtree

edge_list = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]
num_nodes = 8

adjacency_matrix = create_adjacency_matrix(edge_list, num_nodes)
print("Adjacency Matrix of Graph G:")
for line in adjacency_matrix:
    print(line)

tree_structure = {
    1: [3, 2], 
    2: [6, 5], 
    3: [4], 
    4: [8], 
    5: [7],          
    6: [],       
    7: [],           
    8: []    
}

node_label = int(input("\nEnter the node label (x) for inorder traversal: "))

inorder_output = perform_inorder_traversal(tree_structure, node_label)
print(f"Inorder traversal of subtree rooted at node {node_label}: {inorder_output}")
