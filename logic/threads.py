from functools import partial
from itertools import chain

import logic.execution_time


def create_thread(start, finish, elements):
    return dict(
        start=start,
        finish=finish,
        elements=sorted(elements)
    )


def split_into_threads(vertices, edges):

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

    def merge_by_edge_cost(threads):

        def sort_by_cost():
            result = []
            for line_index in range(len(edges)):
                for el_index in range(line_index, len(edges)):
                    if edges[line_index][el_index]:
                        result.append(
                            (
                                (line_index + 1, el_index + 1),
                                edges[line_index][el_index]
                            )
                        )
            return sorted(result, key=lambda t: t[1], reverse=True)

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

        appendable = lambda: not set(edge_ends()) & set(visited)
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

    def merge_logical_branches(threads):
        for thread in threads:
            for merge_candidate in threads:
                if thread["start"] == merge_candidate["start"] and thread["finish"] != merge_candidate["finish"]:
                    i = 1
                    while i < len(merge_candidate["elements"]):
                        thread["elements"].append(merge_candidate["elements"][i])
                        i += 1
                    threads.remove(merge_candidate)
        return threads

    def merge_by_time(threads):

        def find_nearest_thread(min_time=0):
            candidates = list(filter(
                lambda x: x[0] >= min_time,
                sorted_src_keys
            ))
            return (
                sorted_src_keys.pop(sorted_src_keys.index(min(candidates))),
                source.pop(min(candidates))
            ) if candidates else None

        threads_time = partial(logic.execution_time.threads_time, vertices)

        source = dict(zip(
            threads_time(threads),
            threads
        ))
        sorted_src_keys = sorted(threads_time(threads))

        result = []
        while source:
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

    return merge_by_time(merge_logical_branches(merge_by_edge_cost(split_logical_branches())))


def balance(vertices, threads):

    time_of_thread = partial(logic.execution_time.thread_time, vertices)
    duration_of_thread = partial(logic.execution_time.thread_duration, vertices)

    def sort_by_time(threads):
        return sorted(
            threads,
            key=lambda t: time_of_thread(t)[1],
            reverse=True
        )

    source = sort_by_time(threads)
    critical_thread = source.pop(0)
    critical_time = time_of_thread(critical_thread)[1]
    candidates_starts = [vertex['id'] for vertex in vertices if not vertex['incoming']]
    candidates_finishes = [vertex['id'] for vertex in vertices if not vertex['outcoming']]
    candidates = sorted(
        list(filter(
            lambda t: t['finish'] in candidates_finishes and t['start'] not in candidates_starts,
            source
        )),
        key=lambda thread: duration_of_thread(thread)
    )
    [source.remove(candidate) for candidate in candidates]
    for candidate in candidates:
        possible_merged = list(filter(
            lambda thread: duration_of_thread(candidate) <= (critical_time - time_of_thread(thread)[1]),
            source
        ))
        if possible_merged:
            merged = sort_by_time(possible_merged)[0]
            thread = create_thread(
                start=min(candidate['start'], merged['start']),
                finish=max(candidate['finish'], merged['finish']),
                elements=list(set(candidate['elements']) | set(merged['elements']))
            )
            thread['time'] = (
                time_of_thread(merged)[0],
                time_of_thread(merged)[1] + duration_of_thread(candidate)
            )
            source[source.index(merged)] = thread
    return [critical_thread] + source


def connections_between_threads(edges, threads):

    def connection_cost_between_two_threads(t1, t2):
        return 0 if t1 is t2 else max(
            [edges[i-1][j-1] for i in t1['elements'] for j in t2['elements'] if edges[i-1][j-1]],
            default=None
        )

    return [
        [
            connection_cost_between_two_threads(t1, t2)
            for t2 in threads
        ]
        for t1 in threads
    ]