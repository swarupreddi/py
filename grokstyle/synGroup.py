"""
a: b, c
d: e, f
c: e
u: v

(a, e): T
(a, u): F
"""


def add_arc(graph, n1, n2):
    if n1 in graph:
        graph[n1].add(n2)
    else:
        graph[n1] = set([n2])


def create_graph(nonDisjointGroups):
    """ create a graph from a list of non-disjoint synonym groups
    
        for the synonym group [s1, ..., sn] add n arcs to the graph
        s1->s2, s2->s1, ..., sn ->s1
        s2->s3, s3->s2

        The graph is a map from each from-node to its set of to-nodes
    """
    graph = {}
    for nodes in nonDisjointGroups:
        n = len(nodes)
        for i in range(n):
            add_arc(graph, nodes[i], nodes[(i + 1) % n])
    return graph


def reachable(graph, node0):
    """ return a set of all the nodes reachable from node0 """
    visited = set([])
    todo = [node0]
    while len(todo) > 0:
        node = todo.pop()
        if node not in visited:
            visited.add(node)
            todo.extend(graph.get(node, []))
    return visited


def create_lookup(nonDisjointGroups):
    graph = create_graph(nonDisjointGroups)
    node2Group = {} #map: phrase -> synonym group id
    synGroupId = 0
    for node in graph.keys():
        if node not in node2Group:
            disjointGroup = reachable(graph, node)
            for n in disjointGroup:
                node2Group[n] = synGroupId
            synGroupId += 1
    return node2Group


def is_synonym(x, y, t):
    return t[x] == t[y] if x in t and y in t else x == y


def test():
    g1 = [['a','b','c'], ['d', 'e', 'f'], ['c', 'e'], ['u', 'v']]
    thesaurus = create_lookup(g1)
    if (not is_synonym('a', 'e', thesaurus)) or is_synonym('a', 'u', thesaurus):
        print "!! failure"
    else:
        print "all good"


if __name__ == '__main__':
    test()
