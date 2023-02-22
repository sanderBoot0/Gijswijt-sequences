import math

def hasjh(arr, index, length):
    return hash(tuple(arr[(index+1)-length:index+1]))

sequence = [1, 1, 2]
hashmap = [[hasjh(sequence, 0, 1)],
            [hasjh(sequence, 1, 1), hasjh(sequence, 1, 2)],
            [hasjh(sequence, 2, 1), hasjh(sequence, 2, 2), hasjh(sequence, 2, 3)]]

for _ in range(10):
    maxRepeats = 1

    # Check for each possible length the repeating sequence can be
    for repeatLength in range(1, math.floor(len(sequence)/2)+1):

        # The hash of the subsequence we are going to check
        checkHash = hasjh(sequence, len(sequence)-1, repeatLength)

        # The maximal number of repeats
        maxNumberOfRepeats = math.floor(len(sequence)/repeatLength)

        repeats = 1
        endIndex = len(sequence) - repeatLength - 1
        while endIndex > repeatLength:
            if hashmap[endIndex][repeatLength-1] != checkHash:
                break
            
            repeats += 1
            endIndex -= repeatLength

        if repeats > maxRepeats:
            maxRepeats = repeats

    # Add the maximum number of repeats
    sequence.append(maxRepeats)

    # Generate the new hashes and add them to the hasmap
    hashmap.append(list(map(lambda x: hasjh(sequence, len(sequence)-1, x), range(1, len(sequence)+1))))

print(sequence)