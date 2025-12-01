
#region Input

input = open("input.txt")

instructions = []

for line in input:
    if line[0] == "L":
        instructions.append(-1 * int(line[1:]))
    else:
        instructions.append(int(line[1:]))

input.close()

#endregion


#region Solution

dial = 50
count = 0

debug_dial = 50
debug_count = 0

for x in instructions:
    #region Check
    debug_x = x
    debug_dial_pre = dial

    sign = 1 if x > 0 else -1

    for i in range(0, x, sign):
        debug_dial = (debug_dial + sign) % 100

        if debug_dial == 0:
            debug_count += 1

    #endregion
    debug_add_count_a = 0

    abs_x = abs(x)
    if abs_x >= 100:
        count += abs_x // 100

        debug_add_count_a = abs_x // 100

        if x > 0:
            x = x % 100
        else:
            x = x % -100

    dial += x
    debug_add_count_b = 0


    if debug_dial_pre != 0:
        if (dial >= 100) or (dial <= 0):
            count += 1
            debug_add_count_b = 1

    dial = dial % 100


    #region Check

    if debug_count != count:
        print("breakpoint")

    #endregion

print(count)

#6858

#endregion