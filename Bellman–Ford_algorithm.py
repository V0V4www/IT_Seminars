edge_list = [
    [0, 1],
    [1, 3], [1, 6],
    [3, 2], [3, 7],
    [4, 2],
    [6, 3],
    [7, 4], [7, 5]
]

vert_num = 8
BIG_NUM = 10**6

weight_list = [
    5.0, 12.0, 3.8, 7.0, 1.0, 2.0, 4.0, 10.0, 3.0
]
'''
edge_list = [
    [0, 1], [0, 2],
    [1, 3],
    [2, 1]
]

vert_num = 4

weight_list = [
    1, -7, 5, 6
]
'''
dist = [BIG_NUM for _ in range(vert_num)]
parents = [None for _ in range(vert_num)]


def construct_adj_matrix(edge_list, weight_list, vert_num):
    adj_matrix = [[BIG_NUM for _ in range(vert_num)] for _ in range(vert_num)]
    for edge, weight in zip(edge_list, weight_list):
        src = edge[0]
        dest = edge[1]
        adj_matrix[src][dest] = weight
    return adj_matrix


def Bellman_Ford(edge_list, src):
    dist[src] = 0
    for i in range(vert_num - 1):
        for edge in edge_list:
            v, u = edge[0], edge[1]
            if dist[u] > dist[v] + adj_matrix[v][u]:
                dist[u] = dist[v] + adj_matrix[v][u]
                parents[u] = v
    return dist


adj_matrix = construct_adj_matrix(edge_list, weight_list, vert_num)
print(Bellman_Ford(edge_list, 0))
