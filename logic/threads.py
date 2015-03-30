from itertools import chain


def elementary_threads(edges):
    """Returns threads of vertices with maximal edge cost"""
    def create_thread(start, finish, elements):
        return dict(
            start=start,
            finish=finish,
            elements=sorted(elements)
        )

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

    visited = set()
    threads = list()
    for edge in edges_sorted_by_cost():
        is_added = True
        starts = list(map(lambda t: t['start'], threads))
        finishes = list(map(lambda t: t['finish'], threads))

        if len(set(edge[0]) & set(visited)) is 0:
            threads.append(
                create_thread(start=edge[0][0], finish=edge[0][1], elements=list(edge[0]))
            )
        elif edge[0][0] in finishes and edge[0][1] in starts:
            thread_a = next(t for t in threads if t['finish'] == edge[0][0])
            thread_b = next(t for t in threads if t['start'] == edge[0][1])
            threads.append(
                create_thread(
                    start=thread_a['start'],
                    finish=thread_b['finish'],
                    elements=list(set(thread_a['elements'] + thread_b['elements']))
                )
            )
            threads.remove(thread_a)
            threads.remove(thread_b)
        else:
            if edge[0][0] in finishes and edge[0][1] not in visited:
                thread = next(t for t in threads if t['finish'] == edge[0][0])
                threads[threads.index(thread)] = create_thread(
                    start=thread['start'],
                    finish=edge[0][1],
                    elements=thread['elements'] + [edge[0][1]]
                )
            elif edge[0][1] in starts and edge[0][0] not in visited:
                thread = next(t for t in threads if t['start'] == edge[0][1])
                threads[threads.index(thread)] = create_thread(
                    start=edge[0][0],
                    finish=thread['finish'],
                    elements=[edge[0][0]]+thread['elements']
                )
            else:
                is_added = False
        if is_added:
            visited = visited | set(edge[0])
    for i in range(1, len(edges)+1):
        if i not in sorted(list(chain(*list(map(lambda x: x['elements'], threads))))):
            threads.append(
                create_thread(start=i, finish=i, elements=[i])
            )
    return threads