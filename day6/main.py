#region Input

def init_input_1(path: str) -> dict:
    input = open(path)

    output = [x.split() for x in input.readlines()]
    output[0:-1] = [[int(y) for y in x] for x in output[0:-1]]

    input.close()

    return output

def init_input_2(path: str) -> dict:
    input = open(path)

    output = [list(x.replace('\n', '')) for x in  input.readlines()]

    # Equalize list lengths
    line_lengths = [len(x) for x in output]
    max_len = max(line_lengths)

    for i in range(len(output)):
        output[i].extend([' ']*(max_len-line_lengths[i]))


    input.close()

    return output

#endregion


#region Solution

def solution_1(input: dict) -> int:
    task_len = len(input[0:-1])

    sum = 0
    for i in range(len(input[0])):
        match input[-1][i]:
            case "+":
                for x in range(task_len):
                    sum += input[x][i]
            case "*":
                product = 1
                for x in range(task_len):
                    product *= input[x][i]

                sum += product

    return sum

def solution_2(input: dict) -> int:
    sum = 0
    product = 1
    action = ''

    for i in range(len(input[0])):
        new_action = input[-1][i]
        if new_action != ' ':
            action = new_action

        str_value = ''
        for j in range(len(input) - 1):
            if input[j][i] != ' ':
                str_value += input[j][i]

        if str_value == '':
            if action == "*":
                sum += product
                #print(f"Adding product: {product}")
                product = 1
            continue

        match action:
            case "+":
                sum += int(str_value)
                #print(f"Adding +: {str_value}")
            case "*":
                product *= int(str_value)

    return sum


print(solution_1(init_input_1("input_example.txt")))
print(solution_2(init_input_2("input_example.txt")))

print(solution_1(init_input_1("input.txt")))
print(solution_2(init_input_2("input.txt")))

#endregion


#region Performance

import timeit

def perf_test():
    print("Part 1")

    input_1 = init_input_1("input.txt")
    print(f"Parse input\t{timeit.timeit((lambda:init_input_1("input.txt")),number=3)/3:9f}s")
    print(f"Solve\t\t{timeit.timeit((lambda:solution_1(input_1)),number=3)/3:9f}s")

    print("Part 2")

    input_2 = init_input_2("input.txt")
    print(f"Parse input\t{timeit.timeit((lambda:init_input_2("input.txt")),number=3)/3:9f}s")
    print(f"Solve\t\t{timeit.timeit((lambda:solution_2(input_2)),number=3)/3:9f}s")


perf_test()

#endregion