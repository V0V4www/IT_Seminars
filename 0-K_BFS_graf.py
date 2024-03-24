BIG_NUM = 10**6
edge_list = [
    [0,1],
    [1, 2],
    [2,3]
]

edge_list = [
    [0,1],
    [1,3], [1,6],
    [3, 2], [3,7],
    [4,2],
    [6,3],
    [7, 4], [7, 5]
]

vert_num = 8

weight_list = [
    5, 12, 3, 7, 1, 2, 4, 10, 3
]

def construct_adj_matrix(edge_list, weight_list, vert_num):
    adj_matrix = [[BIG_NUM for _ in range(vert_num)] for _ in range(vert_num)]
    for edge, weight in zip(edge_list, weight_list):
        src = edge[0]
        dest = edge[1]
        adj_matrix[src][dest] = weight
    return adj_matrix

def construct_adj_list(edge_list, vert_num):
    adj_list = [[] for _ in range(vert_num)]
    for edge in edge_list:
        src = edge[0]
        dest = edge[1]
        adj_list[src].append(dest)
    return adj_list



def bfs_zero_k(K, adj_list, adj_matrix, src):
    vert_num = len(adj_list)
    dist = [BIG_NUM for i in range(vert_num)]  # dist[i] = Σ_{ребра в пути от src до i} (1), i in [0, vert_num]

    used = [False for i in range(vert_num)]

    dist[src] = 0

    queues = [[] for _ in range(vert_num * K)]
    queues[dist[src]].append(src)

    for k in range(vert_num * K):
        while queues[k]:
            u = queues[k].pop(0)
            if used[u]:
                continue
            else:
                used[u] = True

            for v in adj_list[u]:
                weight = adj_matrix[u][v]
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    queues[dist[v]].append(v)

    return dist


#  если нет циклов, то макс кол-во ребер в пути = (кол-во вершин - 1)
adj_list = construct_adj_list(edge_list, vert_num)
adj_matrix = construct_adj_matrix(edge_list, weight_list, vert_num)
print(bfs_zero_k(max(weight_list), adj_list, adj_matrix, 0))