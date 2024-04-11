import sys

def parse_network(input_network: str):
    # Convert the input string into a matrix of integers
    lines = input_network.strip().split('\n')
    matrix = []
    for line in lines:
        row = []
        elements = line.split(',')
        for element in elements:
            if element == '-':
                row.append(sys.maxsize)  # Use a large value to represent 'infinity'
            else:
                try:
                    # Attempt to convert the element to an integer
                    row.append(int(element))
                except ValueError:
                    # If conversion fails, print an error message and use 'infinity'
                    print(f"Error converting '{element}' to an integer. Using 'infinity' instead.")
                    row.append(sys.maxsize)
        matrix.append(row)
    return matrix

def min_key(keys, mstSet):
    # Find the vertex with the minimum key value
    min_val = sys.maxsize
    min_index = -1
    for v in range(len(keys)):
        if keys[v] < min_val and not mstSet[v]:
            min_val = keys[v]
            min_index = v
    return min_index

def prim_mst(matrix):
    num_vertices = len(matrix)

    # Array to store constructed MST
    parent = [-1] * num_vertices
   
    # Key values used to pick minimum weight edge in cut
    key = [sys.maxsize] * num_vertices
    
    # To represent set of vertices included in MST
    mstSet = [False] * num_vertices
    
    # Make key 0 so that this vertex is picked as first vertex
    key[0] = 0
    
    for _ in range(num_vertices):
        # Pick the minimum key vertex not yet included in MST
        u = min_key(key, mstSet)
        
        # Put the minimum key vertex in the MST set
        mstSet[u] = True
        
        # Update key value and parent index of the adjacent vertices
        for v in range(num_vertices):
            if matrix[u][v] != sys.maxsize and not mstSet[v] and matrix[u][v] < key[v]:
                key[v] = matrix[u][v]
                parent[v] = u
    
    return parent

def calculate_saving(matrix, parent):
    # Calculate the total weight of the MST
    mst_weight = sum(matrix[i][parent[i]] for i in range(1, len(matrix)) if parent[i] != -1 and matrix[i][parent[i]] != sys.maxsize)

    # Calculate the original total weight
    original_weight = sum(matrix[i][j] if matrix[i][j] != sys.maxsize else 0 for i in range(len(matrix)) for j in range(len(matrix[i]))) // 2

    # Calculate the saving
    return original_weight - mst_weight

def maximum_saving(input_network: str) -> int:
    matrix = parse_network(input_network)
    parent = prim_mst(matrix)
    saving = calculate_saving(matrix, parent)
    return saving

# Example usage:
input_network = '''-,14,10,19,-,-,-
14,-,-,15,18,-,-
10,-,-,26,-,29,-
19,15,26,-,16,17,21
-,18,-,16,-,-,9
-,-,29,17,-,-,25
-,-,-,21,9,25,-
'''

# 
max_saving = maximum_saving(input_network)

# Expected result 138
print(max_saving)