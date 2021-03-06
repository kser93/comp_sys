def upgrade_vertices(data):
    def connections(vertex, target):
        if target not in ('incoming', 'outcoming'):
            raise ValueError("target must be incoming or outcoming connections")

        (first, last) = ('begin', 'end') if target is 'outcoming' else ('end', 'begin')
        edges = list(filter(
            lambda x: x[first] == vertex,
            data['edges']
        ))
        edges_id = list(map(lambda x: x[last], edges))
        if not edges_id:
            edges_id = None
            func = None
        elif len(edges_id) == 1:
            func = 'E'
        else:
            func = edges[0]['operator']
        return dict(
            target=edges_id,
            function=func
        )

    return [
        dict(
            id=V['id'],
            cost=V['cost'],
            incoming=connections(V['id'], 'incoming')['target'],
            outcoming=connections(V['id'], 'outcoming')['target'],
            function=dict(
                incoming=connections(V['id'], 'incoming')['function'],
                outcoming=connections(V['id'], 'outcoming')['function']
            )
        ) for V in data['vertices']
    ]


def upgrade_edges(data):
    def outcoming(v):
        return list(map(
            lambda x: dict(end=x['end'], cost=x['cost']),
            list(filter(
                lambda x: x['begin'] == v,
                data['edges']
            ))
        ))

    result = []
    for j in range(1, len(data['vertices'])+1):
        result.append([])
        for i in range(1, len(data['vertices'])+1):
            ends = list(map(lambda x: x['end'], outcoming(j)))
            if i in ends:
                result[j - 1].append(next(x for x in outcoming(j) if x['end'] == i)['cost'])
            else:
                result[j - 1].append(None)

    return result
