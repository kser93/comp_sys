from functools import partial
from itertools import chain


def elementary_threads(edges):
    """Returns threads of vertices with maximal edge cost"""

    def edges_sorted_by_cost():
        result = [
            [
                (
                    (edges.index(line) + 1, line.index(el) + 1),
                    el
                ) for el in line if el
            ]
            for line in edges
        ]
        return sorted(chain(*result), key=lambda t: t[1], reverse=True)

    def create_thread(start, finish, elements):
        return dict(
            start=start,
            finish=finish,
            elements=sorted(elements)
        )

    def insert_to_thread(end):
        (first, last, thread) = \
            ('start', 'finish', prev_thread) if end is 'finish' else\
            ('finish', 'start', next_thread) if end is 'start' else tuple([None]*3)
        (start, finish) = \
            (thread()[first], edge_end(last)) if end is 'finish' else\
            (edge_end(last), thread()[first]) if end is 'start' else tuple([None]*2)
        elements = \
            thread()['elements'] + [edge_end(last)] if end is 'finish' else\
            [edge_end(last)] + thread()['elements']
        threads[threads.index(thread())] = create_thread(
            start=start,
            finish=finish,
            elements=elements
        )

    def merge_threads():
        threads.append(
            create_thread(
                start=prev_thread()['start'],
                finish=next_thread()['finish'],
                elements=list(set(prev_thread()['elements'] + next_thread()['elements']))
            )
        )
        threads.remove(prev_thread())
        threads.remove(next_thread())

    def is_insert_to_thread():
        insertable = lambda x, y: edge_end(x) in threads_points(y) and edge_end(y) not in visited
        return \
            'finish' if insertable('start', 'finish') else \
            'start' if insertable('finish', 'start', ) else None

    threads_points = lambda point: list(map(lambda t: t[point], threads))
    threads_starts = partial(threads_points, 'start')
    threads_finishes = partial(threads_points, 'finish')

    edge_end = lambda x: edge[0][0] if x is 'start' else edge[0][1] if x is 'finish' else None

    is_new_thread = lambda: len(set(edge[0]) & set(visited)) is 0
    is_merge_threads = lambda: edge_end('start') in threads_finishes() and edge_end('finish') in threads_starts()

    connected_thread = lambda x, y: next(t for t in threads if t[x] == edge_end(y))
    prev_thread = partial(connected_thread, 'finish', 'start')
    next_thread = partial(connected_thread, 'start', 'finish')

    visited = set()
    threads = list()
    for edge in edges_sorted_by_cost():
        if is_new_thread():
            threads.append(
                create_thread(
                    start=edge_end('start'),
                    finish=edge_end('finish'),
                    elements=list(edge[0])
                )
            )
        elif is_merge_threads():
            merge_threads()
        elif is_insert_to_thread():
            try:
                insert_to_thread(is_insert_to_thread())
            except StopIteration:
                pass
        else:
            continue
        visited = visited | set(edge[0])
    return threads + [
        create_thread(start=i, finish=i, elements=[i])
        for i in range(1, len(edges) + 1) if i not in visited
    ]