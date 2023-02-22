import math

def hasjh(arr, index, length):
    i = index - length - 1
    return hash(tuple(arr[(index+1)-length:index+1]))

sequence = [1, 1, 2]
hasjmap = [[hasjh(sequence, 0, 1)],
            [hasjh(sequence, 1, 1), hasjh(sequence, 1, 2)],
            [hasjh(sequence, 2, 1), hasjh(sequence, 2, 2), hasjh(sequence, 2, 3)]]

for _ in range(10):
    biggest = 0
    for variationLength in range(1, math.floor(len(sequence)/2)+1):
        same = True

        varToCheck = sequence[len(sequence)-variationLength:]
        checkHash = hasjh(sequence, len(sequence)-1, variationLength)

        maxNumberOfRepeats = math.floor(len(sequence)/len(varToCheck))

        allGood = True
        i = 1
        repeats = 1
        while i < maxNumberOfRepeats and allGood:
            endIndex = len(sequence) - i * len(varToCheck) - 1
            i += 1

            if hasjmap[endIndex][variationLength-1] != checkHash:
                allGood = False
            else:
                repeats += 1


        if repeats > biggest:
            biggest = repeats

    if biggest == 0:
        sequence.append(1)
    else: 
        sequence.append(biggest)

    hasjes = []
    for i in range(1, len(sequence)+1):
        hasjes.append(hasjh(sequence, len(sequence)-1, i))

    hasjmap.append(hasjes)

print(sequence)