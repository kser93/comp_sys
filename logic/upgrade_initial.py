def ids(length):
    return [x + 1 for x in range(length)]


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
    def outcoming(Id):
        return list(map(
            lambda x: dict(end=x['end'], cost=x['cost']),
            list(filter(
                lambda x: x['begin'] == Id,
                data['edges']
            ))
        ))

    return [
        [
            next(x for x in outcoming(Id) if x['end'] == i)['cost']
            if i in list(map(lambda x: x['end'], outcoming(Id)))
            else None
            for i in ids(len(data['vertices']))
        ]
        for Id in ids(len(data['vertices']))
    ]