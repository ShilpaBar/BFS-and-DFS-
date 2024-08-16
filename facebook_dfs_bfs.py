import networkx as nx
import matplotlib.pyplot as plt


def load_graph(file_path):
    G = nx.Graph()
    with open(file_path, 'r') as file:
        for line in file:
            node1, node2 = line.strip().split()
            G.add_edge(int(node1), int(node2))
    return G

def bfs(graph, start, goal):
    visited = set()
    queue = [[start]]
    
    if start == goal:
        return [start]
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visited:
            neighbors = graph[node]
            
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                if neighbor == goal:
                    return new_path
            
            visited.add(node)
    
    return []

def iterative_dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            stack.extend([neighbor for neighbor in graph[node] if neighbor not in visited])

    return visited

def visualize_graph(graph, path=None):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph)
    
    # Draw the graph
    nx.draw(graph, pos, with_labels=True, node_size=50, node_color='blue', edge_color='gray')
    
    if path:
        # Highlight the shortest path
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(graph, pos, nodelist=path, node_color='red', node_size=100)
        nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)
    
    plt.show()

# Visualize the graph with the shortest path highlighted



# Load the graph
file_path = "C:\\Users\\shilp\\facebook_combined.txt"  # Update this path
G = load_graph(file_path)

# Perform BFS
start_user = 10
end_user = 100
shortest_path = bfs(G, start_user, end_user)
print("Shortest path from {} to {}:".format(start_user, end_user), shortest_path)

# Perform DFS
start_user = 10
connections = iterative_dfs(G, start_user)
print("All connections starting from {}:".format(start_user), connections)

visualize_graph(G, shortest_path)