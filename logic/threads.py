from itertools import chain
from logic.execution_time import threads_time


def split_into_threads(vertices, edges):

    def create_thread(start, finish, elements):
        return dict(
            start=start,
            finish=finish,
            elements=sorted(elements)
        )

    def split_logical_branches():
        lb_sources = list(filter(lambda x: x['function']['outcoming'] is '+', vertices))
        result = []
        for vertex in lb_sources:
            children = list(filter(lambda x: x['id'] in vertex['outcoming'], vertices))
            thread_finishes = [child for child in children if child['function']['incoming'] is 'E']
            if len(thread_finishes) > 1:
                result += [
                    create_thread(
                        start=vertex['id'],
                        finish=finish['id'],
                        elements=[vertex['id'], finish['id']]
                    )
                    for finish in thread_finishes
                ]
        return result

    def merge_by_edge_cost():

        def sort_by_cost():
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

        edge_start = lambda: edge[0][0]
        edge_finish = lambda: edge[0][1]
        edge_ends = lambda: list(edge[0])

        threads_starts = lambda: [t['start'] for t in threads]
        threads_finishes = lambda: [t['finish'] for t in threads]

        prev_thread = lambda: next(t for t in threads if t['finish'] == edge_start())
        next_thread = lambda: next(t for t in threads if t['start'] == edge_finish())

        def append_to_thread():
            threads.append(
                create_thread(
                    start=edge_start(),
                    finish=edge_finish(),
                    elements=edge_ends()
                )
            )

        def insert_to_thread(end):
            if end is 'finish':
                threads[threads.index(prev_thread())] = create_thread(
                    start=prev_thread()['start'],
                    finish=edge_finish(),
                    elements=prev_thread()['elements'] + [edge_finish()]
                )
            elif end is 'start':
                threads[threads.index(next_thread())] = create_thread(
                    start=edge_start(),
                    finish=next_thread()['finish'],
                    elements=[edge_start()] + next_thread()['elements']
                )

        def merge_threads():
            threads.append(
                create_thread(
                    start=prev_thread()['start'],
                    finish=next_thread()['finish'],
                    elements=list(set(prev_thread()['elements']) | set(next_thread()['elements']))
                )
            )
            threads.remove(prev_thread())
            threads.remove(next_thread())

        appendable = lambda: len(set(edge_ends()) & set(visited)) is 0
        mergeable = lambda: edge_start() in threads_finishes() and edge_finish() in threads_starts()
        insertable_to_finish = lambda: edge_start() in threads_finishes() and edge_finish() not in visited
        insertable_to_start = lambda: edge_finish() in threads_starts() and edge_start() not in visited

        visited = set(chain(*[thread['elements'] for thread in threads]))
        for edge in sort_by_cost():
            if appendable():
                append_to_thread()
            elif mergeable():
                merge_threads()
            elif insertable_to_start():
                insert_to_thread('start')
            elif insertable_to_finish():
                insert_to_thread('finish')
            else:
                continue
            visited = visited | set(edge_ends())

        return threads + [
            create_thread(start=i, finish=i, elements=[i])
            for i in [v['id'] for v in vertices] if i not in visited
        ]

    def merge_logical_branches():
        is_intersects = lambda t1, t2: len(list(set(t1['elements']) & set(t2['elements']))) is not 0
        splitted = [
            (t1, t2) for t1 in threads for t2 in threads
            if t1 is not t2 and is_intersects(t1, t2)
        ]
        for (t1, t2) in splitted[:int(len(splitted) / 2)]:
            threads.append(
                create_thread(
                    start=min(t1['start'], t2['start']),
                    finish=max(t1['finish'], t2['finish']),
                    elements=list(set(t1['elements']) | set(t2['elements']))
                )
            )
            threads.remove(t1)
            threads.remove(t2)
        return threads

    def merge_by_time():

        def find_nearest_thread(min_time=0):
            candidates = list(filter(
                lambda x: x[0] >= min_time,
                sorted(list(threads.keys()))
            ))
            return (
                min(candidates),
                threads.pop(min(candidates))
            ) if len(candidates) > 0 else None

        result = []
        while len(threads) > 0:
            thread = []
            nearest_thread = find_nearest_thread()
            while nearest_thread:
                thread.append(nearest_thread)
                nearest_thread = find_nearest_thread(nearest_thread[0][1])
            result.append(thread)

        return [
            create_thread(
                start=min(part_thread['start'] for part_thread in thread),
                finish=max(part_thread['finish'] for part_thread in thread),
                elements=sorted(chain(*[part_thread["elements"] for part_thread in thread]))
            )
            for thread in [[x[1] for x in thread] for thread in result]
        ]

    threads = split_logical_branches()
    threads = merge_by_edge_cost()
    threads = merge_logical_branches()
    # threads = merge_logical_branches(merge_by_edge_cost(split_logical_branches()))
    threads = dict(zip(
        threads_time(vertices, threads),
        threads
    ))
    return merge_by_time()


def connections_between_threads(edges, threads):

    def connection_cost_between_two_threads(t1, t2):
        if t1 is t2:
            return 0
        costs = [edges[i-1][j-1] for i in t1['elements'] for j in t2['elements'] if edges[i-1][j-1]]
        return max(costs) if len(costs) else None

    return [
        [
            connection_cost_between_two_threads(t1, t2)
            for t2 in threads
        ]
        for t1 in threads
    ]