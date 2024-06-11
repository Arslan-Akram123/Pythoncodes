graph={
    '9':['8','6'],
    '8':['4','2'],
    '6':['1'],
    '4':[],
    '2':['1'],
    '1':[]
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
bfs(visited,graph,'9');