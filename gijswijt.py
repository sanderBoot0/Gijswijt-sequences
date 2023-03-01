import time
import krulnaive
import krulautomaton
import krulhashmap as hm

def compare(length):
    print(f"length: {length}")

    sequence = [1, 1, 2]

    # The hasmap object is an 2D array
    # Each row indicates a index in the sequence array. r=0 refers to sequence[0], r=2 refers to sequence[2]
    # Each column indicates the length of the sequence. i=2, c=0 refers to sequence[2], c=2 refers to sequence[0:3]
    hashmap = [[(hm.hashList(sequence, [1], 0, 1), 0)]]
    hashmap.append([(hm.hashList([1, 1], hashmap, 1, 2), 1), (hm.hashList([1, 1], hashmap, 1, 1), 1)])
    hashmap.append([(hm.hashList([1, 1, 2], hashmap, 2, 3), 0), (hm.hashList([1, 1, 2], hashmap, 2, 2), 0), (hm.hashList([1, 1, 2], hashmap, 2, 1), 0)])

    t1 = time.time()
    for _ in range(length):
        # Add the maximum number of repeats
        sequence.append(hm.getNextNumber(sequence, hashmap))

        # Generate the new hashes and add them to the hasmap
        hashmap.append(hm.generateHashmapNumbers(sequence, hashmap))

        # clean up hashmap
        hashmap = hm.cleanupHashmap(sequence, hashmap)

    t2 = time.time()

    # print(sequence)
    print(f"Elapsed: {round((t2 - t1) * 1000)} ms hashmap")

    sequence2 = [1, 1, 2]
        
    t3 = time.time()
    for _ in range(length):
        sequence2.append(krulnaive.krul(sequence2))
    t4 = time.time()
    print(f"Elapsed: {round((t4 - t3) * 1000)} ms (n^3)")

    sequence3 = [1, 1, 2]

    t5 = time.time()
    for _ in range(length):
        sequence3.append(krulautomaton.krul(sequence3))
    t6 = time.time()
    print(f"Elapsed: {round((t6 - t5) * 1000)} ms automaton")

# compare(100)
# compare(200)
# compare(500)
# compare(1000)
# compare(2000)
compare(5000)
# compare(6000)
# compare(7000)
# compare(8000)
# compare(9000)
# compare(10000)
# compare(20000)
# compare(50000)
# compare(100000)
