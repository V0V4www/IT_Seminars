edge_list = [
    [0, 1], [0, 3],
    [1, 3],
    [2, 3],
    [4, 0], [4, 3],
    [5, 0]
]

edge_list = [
    [0,1], [0,2], [0,3],
    [1, 2], [1, 4],
    [2, 4],
    [3, 4],
    [4, 5],
    [5, 3]
]

edge_list = [
    [0, 1], [0, 6],
    [1, 2],
    [2, 4],
    [3, 2],
    [4, 5],
    [5, 6],
    [6, 3]
]

vert_num = 7
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
            cycle = cycle_display(v, u)
            assist_str = "◟" + (len(cycle))*'_' + '◞ '
            print(cycle, '\n', assist_str, sep='')
            continue
        elif colors[u] == "b":
            continue
        elif colors[u] == "w":
            dfs(u, v)

    colors[v] = "b"
    timer += 1
    tout[v] = timer


def cycle_display(v, u):
    cycle = [v]
    parent = parents[v]
    while parent != u:
        cycle.append(parent)
        parent = parents[parent]
    cycle.append(u)
    cycle = [str(i) for i in cycle[::-1]]
    cycle_str = '◜'+" 🢩 ".join(cycle)+'◝'
    return cycle_str


dfs(0)
