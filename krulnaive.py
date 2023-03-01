
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