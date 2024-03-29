#find s where is_path(s, A, B) and no_nodes(s, t) and total_weight(s, u) and t=C and u<D

def get_current_weight(path):
    current_weight = 0
    for edge in path:
        current_weight += edge[2]
    return current_weight

def get_path_nodes(path):
    path_nodes = []
    if(len(path) == 1):
        path_nodes.append(path[0][0])
        path_nodes.append(path[0][1])
    elif(len(path) > 1):
        path_nodes.append(path[0][0])
        for edge in path:
            path_nodes.append(edge[1])
    return path_nodes


def find_next(path, all_edges, A, B, C, D):
    possible_next = []
    last_node = path[-1][1]
    nodes_in_path = get_path_nodes(path)
    for edge in all_edges:
        if(edge[1] in nodes_in_path):
            continue
        if(edge[0] == last_node):
            possible_next.append(edge)
    return possible_next

def prune_paths(paths, C, D):
    results = paths.copy()
    for path in paths:
        if(len(path) + 1 != C or get_current_weight(path) >= D):
            results.remove(path)
    return results

def fits_condition(path, A, B, C, D):
    if(path[0][0] == A and path[-1][1] == B and len(path) + 1 == C and get_current_weight(path) < D):
        return True
    return False

def get_all(paths, all_edges, A, B, C, D):
    all_possible_paths = []
    for path in paths:
        if(fits_condition(path, A, B, C, D)):
            all_possible_paths.append(path)
            continue
        if(len(path) + 2 > C):
            continue
        next_edges = find_next(path, all_edges, A, B, C, D)
        possible_paths = []
        for edge in next_edges:
            path_copy = path.copy()
            path_copy.append(edge)
            possible_paths.append(path_copy)
        current_paths = get_all(possible_paths,all_edges, A, B, C, D)
        for current in current_paths:
            all_possible_paths.append(current)
    return all_possible_paths


def find_paths(all_edges, A, B, C, D):
    if(C < 2):
        return []

    result_paths = []
    possible_starts = []
    for edge in all_edges:
        if(edge[0] == A):
            possible_starts.append([edge])
    
    if(len(possible_starts) == 0):
        return []

    result_paths = get_all(possible_starts, all_edges, A, B, C, D)

    return prune_paths(result_paths, C, D)
