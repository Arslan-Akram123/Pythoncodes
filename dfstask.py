graph={
    '7':['11','15'],
    '11':['3'],
    '15':['19','21'],
    '3':[],
    '19':['4'],
    '21':[],
    '4':[]
}
visited=set();
def dfs(visited,graph,node):
    if node not in visited:
        print(node);
    # visited.add(node);
    for neighbour in graph[node]:
        dfs(visited,graph,neighbour);
print("following is the depth-first Search");
dfs(visited,graph,'7');