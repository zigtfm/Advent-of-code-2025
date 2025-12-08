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

def solution_1(input: list, display: bool=False) -> int:
    results = []
    #distances = []
    #pairs = []

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
                #[vec3_a, vec3_b]
            ))

    connected_indexes = {}
    for i in range(len(input)):
        connected_indexes[i] = False

    distance_sorted_result = [pairs for distances, pairs in sorted(results)]

    groups = []

    for pair in distance_sorted_result:
        a_connected = connected_indexes[pair[0]]
        b_connected = connected_indexes[pair[1]]

        if a_connected and b_connected:
            continue

        elif not a_connected and not b_connected:
            connected_indexes[pair[0]] = True
            connected_indexes[pair[1]] = True

            groups.append([pair])

        elif a_connected and not b_connected:
            connected_indexes[pair[1]] = True

            for i in range(len(groups)):
                for j in range(len(groups[i])):
                    if pair[0] in groups[i][j]:
                        groups[i].append(pair)
                        break

        elif not a_connected and b_connected:
            connected_indexes[pair[0]] = True

            for i in range(len(groups)):
                for j in range(len(groups[i])):
                    if pair[1] in groups[i][j]:
                        groups[i].append(pair)
                        break

    output = 1

    lengths = sorted([len(x) for x in groups], reverse=True)
    return lengths[0] * lengths[1] * lengths[2]

def solution_2(input: list, display: bool=False) -> int:
    return 0

_input = init_input("input.txt")

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
]))

#print(solution_1(_input))
#print(solution_2(_input))

#endregion