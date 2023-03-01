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
    maxRepeats = 1

    # Check for each possible length the repeating sequence can be
    for repeatLength in range(1, (len(sequence)//2)+1):

        # Select the number of repeats from the last row and add one
        # '+ 1' should only be done when the hashes match, but it doesn't really matter
        repeats = hashmap[-1][-repeatLength][1] + 1

        maxRepeats = max(maxRepeats, repeats)

    return maxRepeats

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
        n = 0
        if x <= (len(sequence)//2) and has == hashmap[-x][-x][0]:
                n = hashmap[-x][-x][1] + 1            
        l.append((has, n))

    return l

def cleanupHashmap(sequence : List[int], hashmap : List[List[int]]) -> List[List[Tuple[int, int]]]:

    if (len(sequence)//2) % 2 == 0:
        hashmap.pop(0)

    return hashmap