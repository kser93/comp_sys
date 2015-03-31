__author__ = 'artemlobachev'


def merge(el_threads):
    result = []
    while len(el_threads) > 0:
        tmp_result = []
        next_tuple = find_min_key(el_threads)
        while not (next_tuple is None):
            tmp_result.append(next_tuple)
            min_key = next_tuple[0][1]
            next_tuple = find_min_key(el_threads, min_key)
        result += [tmp_result]
    print(find_min_key(el_threads))
    result_treads = []
    for item in result:
        result_treads += [merge_list(item)]
    return result_treads


def find_min_key(dictionary, min_key=0):
    for item in sorted(list(dictionary.keys())):
        if item[0] >= min_key:
            return item, dictionary.pop(item)
    return None


def merge_list(list_threads):
    result_time = list_threads[0][0][0], list_threads[len(list_threads) - 1][0][1]
    result_vertexes = []
    for item in list_threads:
        result_vertexes += item[1]["elements"]
    return result_time, result_vertexes
