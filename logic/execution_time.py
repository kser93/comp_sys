def execution_time(vertices):
    before = [None]
    after = [None]
    precs = lambda vertex: list(after[i] for i in vertex['incoming'])
    functor = {
        None: lambda vertex: 0,
        'E': lambda vertex: precs(vertex)[0],
        '&': lambda vertex: max(precs(vertex)),
        '+': lambda vertex: min(precs(vertex))
    }
    operator = lambda vertex: vertex['function']['incoming']
    for vertex in vertices:
        before.append(functor[operator(vertex)](vertex))
        after.append(before[-1] + vertex['cost'])
    return dict(before=before, after=after)