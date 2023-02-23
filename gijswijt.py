import math

def hasjh(arr, index, length):
    return hash(tuple(arr[(index+1)-length:index+1]))

sequence = [1, 1, 2]
hashmap = [[(hasjh(sequence, 0, 1), 0)],
            [(hasjh(sequence, 1, 1), 1), (hasjh(sequence, 1, 2), 0)],
            [(hasjh(sequence, 2, 1), 0), (hasjh(sequence, 2, 2), 0), (hasjh(sequence, 2, 3), 0)]]

for _ in range(20):
    maxRepeats = 1

    # Check for each possible length the repeating sequence can be
    for repeatLength in range(1, math.floor(len(sequence)/2)+1):
        repeats = hashmap[len(sequence) - 1][repeatLength-1][1] + 1

        if repeats > maxRepeats:
            maxRepeats = repeats

    # Add the maximum number of repeats
    sequence.append(maxRepeats)

    # Generate the new hashes and add them to the hasmap
    l = []

    for x in range(1, len(sequence)+1):
        has = hasjh(sequence, len(sequence)-1, x)
        n = 0
        if x <= (math.floor(len(sequence)/2)) and has == hashmap[len(sequence)-1-x][x-1][0]:
                n = hashmap[len(sequence)-1-x][x-1][1] + 1            
        l.append((has, n))

    hashmap.append(l)

print(sequence)