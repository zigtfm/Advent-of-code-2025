
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
    dial = (dial + x) % 100
    if dial == 0:
        count += 1

print(count)

#endregion
