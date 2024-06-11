graph={
    'A':['B','C','D'],
    'B':['E','F'],
    'C':['G','H'],
    'D':['I','J'],
    'E':['K'],
    'F':[],
    'G':[],
    'H':[],
    'I':[],
    'J':[],
    'K':[]
}
visited=set();
def dfs(visited,graph,node):
    if node not in visited:
        print(node);
    visited.add(node);
    for neighbour in graph[node]:
        dfs(visited,graph,neighbour);
print("following is the depth-first Search");
dfs(visited,graph,'A');