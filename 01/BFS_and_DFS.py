#BFS and DFS
graph_long = {
    '1': '2 7',
    '2': '3',
    '3': '4',
    '4': '5',
    '5': '6 10',
    '7': '8',
    '6': '5',
    '8': '9',
    '9': '10',
    '10': '5 11',
    '11': '12',
    '12': '11',
}

for n in graph_long:
    graph_long[n] = graph_long[n].split()
    
def search(graph, call_back):
    found = set()
    search_list = ['1']
    while search_list:
        node = search_list.pop(0)
        if node in found:
            continue
        print ('i am looking at :{}'.format(node))
        found.add(node)
        new_node = graph[node]
        search_list = call_back(new_node, search_list)
   
        
def DFS(new_node, search_list):
    return new_node + search_list

def BFS(new_node, search_list):
    return search_list + new_node

def print_test():
    print ("DFS")
    search(graph_long, DFS)
    print ("BFS")
    search(graph_long, BFS)

    
print_test()