def elementary_threads(edges):
    """Returns threads of vertices with maximal edge cost
        thread: {
            start - id of start vertex;
            finish - id of finish(gosh!, obviously) vertex;
            elements - all vertices contained in thread
        }"""

    def sort_by_cost(edges):
        result = list()
        for i in range(len(edges)):
            for j in range(len(edges)):
                if edges[i][j]:
                    result.append(tuple([(i + 1, j + 1), edges[i][j]]))
        return sorted(result, key=lambda t: t[1], reverse=True)

    visited = list()