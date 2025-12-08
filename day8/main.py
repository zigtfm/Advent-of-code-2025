#region Input

def init_input(path: str) -> dict:
    input = open(path)

    output = [[int(y) for y in x.split(",")] for x in input.readlines()]

    input.close()

    return output

#endregion


#region Solution

def vec3_distance(x1, y1, z1, x2, y2, z2):
    return ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**.5


def solution_1(input: list, count=1) -> int:
    results = []

    for i in range(len(input)):
        vec3_a = input[i]
        for j in range(i+1, len(input)):
            vec3_b = input[j]

            results.append((
                vec3_distance(
                    vec3_a[0], vec3_a[1], vec3_a[2],
                    vec3_b[0], vec3_b[1], vec3_b[2]
                ),
                [i, j]
            ))

    connected_indexes_group = {}
    for i in range(len(input)):
        connected_indexes_group[i] = -1

    distance_sorted_result = [pairs for distances, pairs in sorted(results)]

    groups = []

    for pair in distance_sorted_result[:count]:
        a_group = connected_indexes_group[pair[0]]
        b_group = connected_indexes_group[pair[1]]
        a_connected = a_group != -1
        b_connected = b_group != -1
        same_group = a_group == b_group


        if a_connected and b_connected and same_group:
            continue

        elif a_connected and b_connected and not same_group:
            for n in groups[b_group]:
                connected_indexes_group[n] = a_group

            groups[a_group].extend(groups[b_group])
            groups[b_group] = []

        elif not a_connected and not b_connected:
            connected_indexes_group[pair[0]] = len(groups)
            connected_indexes_group[pair[1]] = len(groups)

            groups.append(pair[:])

        elif a_connected and not b_connected:
            connected_indexes_group[pair[1]] = connected_indexes_group[pair[0]]

            groups[connected_indexes_group[pair[1]]].append(pair[1])

        elif not a_connected and b_connected:
            connected_indexes_group[pair[0]] = connected_indexes_group[pair[1]]

            groups[connected_indexes_group[pair[0]]].append(pair[0])


    lengths = sorted([len(x) for x in groups], reverse=True)
    return lengths[0] * lengths[1] * lengths[2]


def solution_2(input: list) -> int:
    results = []

    for i in range(len(input)):
        vec3_a = input[i]
        for j in range(i+1, len(input)):
            vec3_b = input[j]

            results.append((
                vec3_distance(
                    vec3_a[0], vec3_a[1], vec3_a[2],
                    vec3_b[0], vec3_b[1], vec3_b[2]
                ),
                [i, j]
            ))

    connections_count = 0
    connections_max = len(input)-1

    connected_indexes_group = {}
    for i in range(len(input)):
        connected_indexes_group[i] = -1

    distance_sorted_result = [pairs for distances, pairs in sorted(results)]

    groups = []

    for pair in distance_sorted_result:
        a_group = connected_indexes_group[pair[0]]
        b_group = connected_indexes_group[pair[1]]
        a_connected = a_group != -1
        b_connected = b_group != -1
        same_group = a_group == b_group


        if a_connected and b_connected and same_group:
            continue

        elif a_connected and b_connected and not same_group:
            for n in groups[b_group]:
                connected_indexes_group[n] = a_group

            groups[a_group].extend(groups[b_group])
            groups[b_group] = []

            connections_count += 1

        elif not a_connected and not b_connected:
            connected_indexes_group[pair[0]] = len(groups)
            connected_indexes_group[pair[1]] = len(groups)

            groups.append(pair[:])

            connections_count += 1

        elif a_connected and not b_connected:
            connected_indexes_group[pair[1]] = connected_indexes_group[pair[0]]

            groups[connected_indexes_group[pair[1]]].append(pair[1])
            connections_count += 1

        elif not a_connected and b_connected:
            connected_indexes_group[pair[0]] = connected_indexes_group[pair[1]]

            groups[connected_indexes_group[pair[0]]].append(pair[0])
            connections_count += 1

        if connections_count == connections_max:
            return input[pair[0]][0] * input[pair[1]][0]

    return "problem"

_input = init_input("input.txt")

"""
print(solution_1([
    [162,817,812],
    [57,618,57],
    [906,360,560],
    [592,479,940],
    [352,342,300],
    [466,668,158],
    [542,29,236],
    [431,825,988],
    [739,650,466],
    [52,470,668],
    [216,146,977],
    [819,987,18],
    [117,168,530],
    [805,96,715],
    [346,949,466],
    [970,615,88],
    [941,993,340],
    [862,61,35],
    [984,92,344],
    [425,690,689]
], count=10))

"""
#print(solution_1(_input, count = 1000))
#print(solution_2(_input))

import timeit
import statistics

def perf_test():
    print("Part 1")

    _input = init_input("input.txt")
    result = timeit.repeat((lambda:solution_1(_input, count = 1000)),number=1, repeat=10)
    print(f"Results: {statistics.mean(result):.9f}s +- {statistics.stdev(result):.9f}s")

    print("Part 2")

    _input = init_input("input.txt")
    result = timeit.repeat((lambda:solution_1(_input, count = 1000)),number=1, repeat=10)
    print(f"Results: {statistics.mean(result):.9f}s +- {statistics.stdev(result):.9f}s")


perf_test()

#endregion