from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    queue = Queue()
    cur = starting_node
    parent_child = {}

    for node in ancestors:
        if node[1] not in parent_child:
            parent_child[node[1]] = set()
        parent_child[node[1]].add(node[0])
    
    if starting_node in parent_child:
        queue.enqueue(parent_child[cur])
    else:
        return -1
    
    while queue.size() > 0:
        connection = queue.dequeue()
        cur = min(connection)
        if cur not in parent_child:
            return cur
        else:
            queue.enqueue(parent_child[cur])
    
