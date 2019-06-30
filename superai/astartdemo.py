import queue
from typing import List


def hwToidx(i: int, j: int, weight: int):
    return i * weight + j


def idxTohw(idx, weight: int):
    return [idx // weight, idx % weight]


# 有向图
class Graph:
    V: int  # 顶点数量
    E: int  # 边数量
    # adj: None #: List[List]  # 邻接表

    W: int  # 宽度  (虽然是一维的但是表示是二维的)

    def __init__(self, V: int, W: int):
        self.V = V
        self.E = 0
        self.adj = []
        self.W = W

        for i in range(V):
            nears = []
            self.adj.append(nears)

    def AddEdge(self, v: int, w: int):
        self.adj[v].append(w)
        self.E += 1

    def __str__(self):
        str = ""
        for idx, nears in enumerate(self.adj):
            str += "idx: {} nears: {}\n".format(idx, nears)
        return str


# bfs
class BreadthFirstPaths:
    def __init__(self, g: Graph, s: int):
        self.marked = [False] * g.V
        self.edgeTo = [0] * g.V
        self.s = s

        self.bfs(g, self.s)

    def bfs(self, g: Graph, s: int):
        q = queue.Queue()
        q.put(s)
        while q.qsize() != 0:
            v = q.get()

            for w in g.adj[v]:
                # 这个路径没有经过
                if not self.marked[w]:
                    self.edgeTo[w] = v
                    self.marked[w] = True
                    q.put(w)

                    # print(w, idxTohw(w, 6))

    def HasPathTo(self, v: int):
        return self.marked[v]

    def PathTo(self, v: int) -> [int]:
        result = []
        if not self.HasPathTo(v):
            return result
        x = v
        while x != self.s:
            result.append(x)
            x = self.edgeTo[x]
        result.append(self.s)
        return result


def manhattanDistance(x, y):
    return sum(map(lambda i, j: abs(i - j), x, y))


# a*
class AStarPaths:
    def __init__(self, g: Graph, start: int, end: int):
        self.closedSet = []
        self.openSet = [start]

        self.start = start
        self.end = end

        self.edgeTo = [0] * g.V

        self.marked = [False] * g.V

        # 实际距离
        self.gScore = [0] * g.V
        self.gScore[start] = 0

        # 估算到终点的距离
        self.fScore = [0] * g.V
        self.fScore[start] = manhattanDistance(idxTohw(start, g.W), idxTohw(end, g.W))

        self.astar(g)

    def astar(self, g: Graph):
        while len(self.openSet) > 0:
            current = min(self.openSet, key=lambda s: self.fScore[s])
            if current == self.end:
                return
            self.openSet.remove(current)
            self.closedSet.append(current)
            for w in g.adj[current]:
                if w in self.closedSet:
                    continue
                # 实际距离
                tentativegScore = self.gScore[current] + manhattanDistance(idxTohw(current, g.W), idxTohw(w, g.W))

                if w not in self.openSet:
                    self.openSet.append(w)
                elif tentativegScore >= self.gScore[w]:  # 如果此次遍历距离大于其他点遍历过去的距离则抛弃
                    continue

                self.edgeTo[w] = current
                self.marked[w] = True

                print("edgeTo ({},{}) -> ({},{})".format(current // g.W, current % g.W, w // g.W, w % g.W))
                self.gScore[w] = tentativegScore
                self.fScore[w] = self.gScore[w] + manhattanDistance(idxTohw(w, g.W), idxTohw(self.end, g.W))

                print("fScore[%d] manhattan: %d" % (w, self.fScore[w]))

    def HasPathTo(self, v: int):
        return self.marked[v]

    def PathTo(self, v: int):
        result = []
        if not self.HasPathTo(v):
            return result

        x = v
        while x != self.start:
            result.append(x)
            x = self.edgeTo[x]
        result.append(self.start)
        return result


def main():
    # 0,1,2,3,4 ... 一共12个顶点. width=6,height=4
    graph = Graph(24, 6)

    graph.AddEdge(hwToidx(0, 2, 6), hwToidx(1, 2, 6))

    graph.AddEdge(hwToidx(1, 1, 6), hwToidx(2, 1, 6))

    graph.AddEdge(hwToidx(1, 2, 6), hwToidx(0, 2, 6))
    graph.AddEdge(hwToidx(1, 2, 6), hwToidx(1, 3, 6))

    graph.AddEdge(hwToidx(1, 3, 6), hwToidx(1, 2, 6))
    graph.AddEdge(hwToidx(1, 3, 6), hwToidx(1, 4, 6))

    graph.AddEdge(hwToidx(1, 4, 6), hwToidx(2, 4, 6))
    graph.AddEdge(hwToidx(1, 4, 6), hwToidx(1, 3, 6))

    graph.AddEdge(hwToidx(2, 0, 6), hwToidx(2, 1, 6))

    graph.AddEdge(hwToidx(2, 1, 6), hwToidx(3, 1, 6))
    graph.AddEdge(hwToidx(2, 1, 6), hwToidx(2, 0, 6))
    graph.AddEdge(hwToidx(2, 1, 6), hwToidx(1, 1, 6))
    graph.AddEdge(hwToidx(2, 1, 6), hwToidx(2, 2, 6))

    graph.AddEdge(hwToidx(2, 2, 6), hwToidx(3, 2, 6))
    graph.AddEdge(hwToidx(2, 2, 6), hwToidx(2, 1, 6))
    graph.AddEdge(hwToidx(2, 2, 6), hwToidx(2, 3, 6))

    graph.AddEdge(hwToidx(2, 3, 6), hwToidx(3, 3, 6))
    graph.AddEdge(hwToidx(2, 3, 6), hwToidx(2, 2, 6))
    graph.AddEdge(hwToidx(2, 3, 6), hwToidx(2, 4, 6))

    graph.AddEdge(hwToidx(2, 4, 6), hwToidx(3, 4, 6))
    graph.AddEdge(hwToidx(2, 4, 6), hwToidx(2, 3, 6))
    graph.AddEdge(hwToidx(2, 4, 6), hwToidx(1, 4, 6))
    graph.AddEdge(hwToidx(2, 4, 6), hwToidx(2, 5, 6))

    graph.AddEdge(hwToidx(2, 5, 6), hwToidx(3, 5, 6))
    graph.AddEdge(hwToidx(2, 5, 6), hwToidx(2, 4, 6))

    graph.AddEdge(hwToidx(3, 1, 6), hwToidx(2, 1, 6))

    graph.AddEdge(hwToidx(3, 2, 6), hwToidx(2, 2, 6))
    graph.AddEdge(hwToidx(3, 2, 6), hwToidx(3, 3, 6))

    graph.AddEdge(hwToidx(3, 3, 6), hwToidx(3, 2, 6))
    graph.AddEdge(hwToidx(3, 3, 6), hwToidx(2, 3, 6))

    graph.AddEdge(hwToidx(3, 4, 6), hwToidx(3, 5, 6))
    graph.AddEdge(hwToidx(3, 4, 6), hwToidx(2, 4, 6))

    graph.AddEdge(hwToidx(3, 5, 6), hwToidx(3, 4, 6))
    graph.AddEdge(hwToidx(3, 5, 6), hwToidx(2, 5, 6))

    print("图:")
    print(graph)

    print("广度优先:")
    bfs = BreadthFirstPaths(graph, 2)
    paths = bfs.PathTo(hwToidx(1, 1, 6))
    for v in reversed(paths):
        print(v, idxTohw(v, 6))

    # print(manhattanDistance([0, 2], [1, 2]))

    print("\na*寻径")
    astar = AStarPaths(graph, 2, 7)
    paths = astar.PathTo(hwToidx(1, 1, 6))
    for v in reversed(paths):
        print(v, idxTohw(v, 6))


if __name__ == "__main__":
    main()