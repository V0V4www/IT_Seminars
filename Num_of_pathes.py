edge_list = [
    [0, 1], [0, 3],
    [1, 3],
    [2, 3],
    [4, 0], [4, 3],
    [5, 0]
]

edge_list1 = [
    [0, 1], [0, 2], [0, 3],
    [1, 2], [1, 4],
    [2, 4],
    [4, 5],
    [5, 3]
]
vert_num = 6
adj_list = [[] for _ in range(vert_num)]
for edge in edge_list:
    u = edge[0]
    v = edge[1]
    adj_list[u].append(v)

g = adj_list

timer = 0
tin = [None for _ in range(vert_num)]
tout = [None for _ in range(vert_num)]

parents = [None for _ in range(vert_num)]
colors = ["w" for _ in range(vert_num)]


def dfs(v, p=-1):  # depth first search
    parents[v] = p
    global timer
    timer += 1
    tin[v] = timer
    colors[v] = "g"
    for u in g[v]:
        if colors[u] == "g":
            print(f"cycle been found {u} -> {v}")
            continue
        elif colors[u] == "b":
            continue
        elif colors[u] == "w":
            dfs(u, v)

    colors[v] = "b"
    timer += 1
    tout[v] = timer


def top_sort():
    for v in range(vert_num):
        if colors[v] == "w":
            dfs(v)

    vert_list = [i for i in range(vert_num)]
    ans = [
        x for y, x in sorted(zip(tout, vert_list), key=lambda pair: pair[0], reverse=True)
    ]
    return ans


ts = top_sort()
sa1d = [0 for _ in range(vert_num)]
for v in ts[::-1]:
    sa1d[v] += 1 + sum([sa1d[u] for u in range(vert_num) if u in adj_list[v]])

print(sa1d)

#  sa1d[v] = 1 + SIGMA_{(v, u) - ребро; u принадлежит adj_list[v]}
