from typing import List, Tuple

def hashList(arr : List[int], hashmap : List[List[int]], index : int, length : int) -> int:
    """This function turns part of an array into a hash

    The function creates a new hash based on the hash with lenght-1 combined with the integer at {index}

    2 cases:
    length == 1: hash <- the hash of sequence[index]
    length  > 1: hash <- hashmap{hash of sequence with length -1} combined with sequence[index]

    Args:
        arr (List[int]): The entire sequence array
        index (int): The index of the last element
        length (int): The length of the sequence that needs to be sliced

    Returns:
        int: The hash of the subsequence
    """

    if length == 1:
        return hash(arr[index])
    else:
        return hash((hashmap[-1][-(length-1)][0], arr[index]))

def getNextNumber(sequence : List[int], hashmap : List[List[int]]):
    """This function finds the next number in the Gijswijt sequence

    Args:
        sequence (List[int]): The current sequence
        hashmap (List[List[int]]): The hashmap filled with hashes for each variation of subsequences

    Returns:
        int: Returns the next gijswijt number
    """
    return max(map(lambda x: x[1], hashmap[-1]))

def generateHashmapNumbers(sequence : List[int], hashmap : List[List[Tuple[int, int]]]) -> List[Tuple[int, int]]:
    """This function generates the new row of hash numbers.

    The function will check if the hash of the subsequence equal is to the hash of the previous occurance with that length.
    If so, add 1 to the repeat integer

    Args:
        sequence (List[int]): The sequence list
        hashmap (List[List[int]]): The current hashmap

    Returns:
        List[List[int]]: Returns the new row for the hashmap
    """
    l = []

    for x in range(len(sequence), 0, -1):
        has = hashList(sequence, hashmap, len(sequence)-1, x)
        n = 1
        if x <= (len(sequence)//2) and has == hashmap[-x][-x][0]:
                n = hashmap[-x][-x][1] + 1            
        l.append((has, n))

    return l

def cleanupHashmap(sequence : List[int], hashmap : List[List[int]]) -> List[List[Tuple[int, int]]]:

    if (len(sequence)//2) % 2 == 0:
        hashmap.pop(0)

    return hashmap


if __name__ == "__main__": 
    
    length = 10
    sequence = [1, 1, 2]

    hashmap = [[(hashList(sequence, [1], 0, 1), 1)]]
    hashmap.append([(hashList([1, 1], hashmap, 1, 2), 1), (hashList([1, 1], hashmap, 1, 1), 2)])
    hashmap.append([(hashList([1, 1, 2], hashmap, 2, 3), 1), (hashList([1, 1, 2], hashmap, 2, 2), 1), (hashList([1, 1, 2], hashmap, 2, 1), 1)])

    for _ in range(length):
        # Add the maximum number of repeats
        sequence.append(getNextNumber(sequence, hashmap))

        # Generate the new hashes and add them to the hasmap
        hashmap.append(generateHashmapNumbers(sequence, hashmap))

        # clean up hashmap
        hashmap = cleanupHashmap(sequence, hashmap)

    print(sequence)
