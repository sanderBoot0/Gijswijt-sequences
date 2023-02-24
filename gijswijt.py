import math
from typing import List, Tuple
import time

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
        return hash((hashmap[index-1][length-2][0], arr[index]))

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
        repeats = hashmap[-1][repeatLength-1][1] + 1

        maxRepeats = max(maxRepeats, repeats)

    return maxRepeats

def generateHashmapNumbers(sequence : List[int], hashmap : List[List[int]]) -> List[List[int]]:
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

    for x in range(1, len(sequence)+1):
        has = hashList(sequence, hashmap, len(sequence)-1, x)
        n = 0
        if x <= (len(sequence)//2) and has == hashmap[-x][x-1][0]:
                n = hashmap[-x][x-1][1] + 1            
        l.append((has, n))

    return l

def krul(arr):
    l = len(arr)
    k = 1 # k in XY^k (curling number)    
    
    for i in range(1, l//2 + 1):
        pattern = arr[l - i : l] 
        j = 1   # frequency of this pattern        
        while arr[l - (j+1) * i : l - j * i] == pattern:
            j += 1
            k = max(k, j) # select highest frequency    
            
    return k
    
def compare(length):
    print(f"length: {length}")

    sequence = [1, 1, 2]

    # The hasmap object is an 2D array
    # Each row indicates a index in the sequence array. r=0 refers to sequence[0], r=2 refers to sequence[2]
    # Each column indicates the length of the sequence. i=2, c=0 refers to sequence[2], c=2 refers to sequence[0:3]
    hashmap = [[(hashList(sequence, [], 0, 1), 0)]]
    hashmap.append([(hashList(sequence, hashmap, 1, 1), 1), (hashList(sequence, hashmap, 1, 2), 0)])
    hashmap.append([(hashList(sequence, hashmap, 2, 1), 0), (hashList(sequence, hashmap, 2, 2), 0), (hashList(sequence, hashmap, 2, 3), 0)])

    t1 = time.time()
    for _ in range(length):
        # Add the maximum number of repeats
        sequence.append(getNextNumber(sequence, hashmap))

        # Generate the new hashes and add them to the hasmap
        hashmap.append(generateHashmapNumbers(sequence, hashmap))
    t2 = time.time()

    # print(sequence)
    print(f"Elapsed: {round((t2 - t1) * 1000)} ms hashmap")

    sequence2 = [1, 1, 2]
        
    t3 = time.time()
    for _ in range(length):
        sequence2.append(krul(sequence2))
    t4 = time.time()
    print(f"Elapsed: {round((t4 - t3) * 1000)} ms (n^3)")
    print(f"Equal: {sequence == sequence2}")

compare(10)
# compare(20)
# compare(40)
# compare(80)
# compare(160)
# compare(320)
# compare(640)
# compare(1280)
# compare(2560)
# compare(5120)
# compare(10240)
# compare(20480)
# compare(40960)
