#region Input

def compress_ranges(ranges: list[list[int]]) -> list[list[int]]:
    # Sort by left index
    ranges.sort(key=lambda a: a[0])

    delete_indexes = []
    for i in range(1, len(ranges)):
        range_current = ranges[i]
        range_previous = ranges[i-1]

        if (range_current[0] <= range_previous[1]):
            range_current[0] = range_previous[0]
            range_current[1] = max(range_current[1], range_previous[1])
            delete_indexes.append(i-1)

    delete_indexes.reverse()
    for i in delete_indexes:
        del ranges[i]

    return ranges


def init_input(path: str) -> dict:
    input = open(path)

    output: dict = {
        "valid_id_ranges" : [],
        "available_ids" : []
    }

    while True:
        line = input.readline()
        if line == "\n": break
        output["valid_id_ranges"].append(
            [int(x) for x in line.split("-")]
        )


    output["available_ids"] = [int(x) for x in input.read().split("\n")]


    output["valid_id_ranges"] = compress_ranges(output["valid_id_ranges"])

    input.close()

    return output

#endregion


#region Solution


def solution(input: dict) -> int:
    count = 0

    """
    output: dict = {
        "valid_id_ranges" : [],
        "available_ids" : []
    }
    """

    for id in input["available_ids"]:
        exit_loop = False
        for _range in input["valid_id_ranges"]:
            if id >= _range[0] and id <= _range[1]:
                exit_loop = True
                count += 1
                break
            if exit_loop: break

    return count


def solution_2(input: dict) -> int:
    count = 0

    for _range in input["valid_id_ranges"]:
        count += _range[1] - _range[0] + 1

    return count


print(solution(init_input("input_example.txt")))
print(solution_2(init_input("input_example.txt")))

print(solution(init_input("input.txt")))
print(solution_2(init_input("input.txt")))

#endregion


#region Performance

import timeit

def perf_test(func: callable):
    print(f"{timeit.timeit(func,number=5)/5}s")

print("Part 1")
perf_test(lambda:solution(init_input("input.txt")))
print("Part 2")
perf_test(lambda:solution_2(init_input("input.txt")))

#endregion