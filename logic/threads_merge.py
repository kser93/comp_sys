from itertools import chain
from logic.threads_new import create_thread


def merge_by_time(threads):
    result = []
    while len(threads) > 0:
        thread = []
        nearest_thread = find_nearest_thread(threads)
        while nearest_thread:
            thread.append(nearest_thread)
            nearest_thread = find_nearest_thread(threads, nearest_thread[0][1])
        result.append(thread)

    return [
        create_thread(
            start=min(part_thread['start'] for part_thread in thread),
            finish=max(part_thread['finish'] for part_thread in thread),
            elements=sorted(chain(*[part_thread["elements"] for part_thread in thread]))
        )
        for thread in [[x[1] for x in thread] for thread in result]
    ]


def find_nearest_thread(threads, min_time=0):
    candidates = list(filter(
        lambda x: x[0] >= min_time,
        sorted(list(threads.keys()))
    ))
    return (
        min(candidates),
        threads.pop(min(candidates))
    ) if len(candidates) > 0 else None