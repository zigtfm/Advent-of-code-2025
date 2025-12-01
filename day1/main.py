
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

for x in instructions:
    dial_pre = dial

    count += abs(x) // 100
    if x > 0:
        x = x % 100
    else:
        x = x % -100

    dial += x

    if dial_pre != 0 and ((dial >= 100) or (dial <= 0)):
        count += 1

    dial %= 100

print(count)

#endregion