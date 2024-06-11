graph={
    '7':['11','15'],
    '11':['3'],
    '15':['19','21'],
    '3':[],
    '19':['4'],
    '21':[],
    '4':[]
}
visited=[];
queue=[];
def bfs(visited,graph,node):
    visited.append(node);
    queue.append(node);
    
    while queue:
        m=queue.pop(0);
        print(m,end=" ");
        
    
        for i in graph[m]:
            if i not in visited:
              visited.append(i);
              queue.append(i);
            

print("Following is the Breath-First Search");
bfs(visited,graph,'7');   