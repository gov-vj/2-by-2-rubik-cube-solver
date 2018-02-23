import rubik

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    
    """
    processed_f=set()
    processed_b=set()
    parent_f={start:None}
    parent_b={end:None}
    frontier_f=[start]
    frontier_b=[end]
    isforward=True
    for i in range(16):
        frontier=frontier_f if isforward else frontier_b
        parent=parent_f if isforward else parent_b
        processed=processed_f if isforward else processed_b
        next_=[]
        for u in frontier:
            process(u,parent,next_)
            processed.add(u)
            break_=(u in processed_b) if isforward else (u in processed_f)
            if break_:
                x=u
                break
        if break_: break
        if isforward: frontier_f=next_
        else: frontier_b=next_
        isforward= not isforward
    else:
        return None
    path=[]
    u=x
    while u != start:
        path.insert(0,parent_f[u][0])
        u=parent_f[u][1]
    u=x
    while u!=end:
        path.append(rubik.perm_inverse(parent_b[u][0]))
        u=parent_b[u][1]
    return path
    

def process(u,parent,next_):
    for move in rubik.quarter_twists:
        v=rubik.perm_apply(move,u)
        if v not in parent:
##            parent[v]=(rubik.perm_inverse(move),move,u) #u
            parent[v]=(move,u) #u
            next_.append(v)
