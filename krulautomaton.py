
def krul(arr): 
    states = {1 : "0"}      # holds all possible states (valid patterns)    
    freqs = {0 : 1}         # holds all encountered frequencies (at least 1)    
    l = len(arr)
    for i in range(1, l + 1):   # look at each entry in the array once        
        for length, state in states.copy().items(): # loop through all possible states (with its length)            
            mod = i % length    # figure out which index of the state we need to compare to            
            if mod: 
                cmp = state[length - mod] 
            else: 
                cmp = state[0] 
                
            if cmp == arr[l - i]:   # compare the current element with the relevant index in a state                
                freqs[length] = i // length # save the frequency if the pattern aligns            
            else:   
                del(states[length]) # if it did not match, delete the state        
                
        if i <= l//2: 
            states[i] = arr[l - i : l]  # this new state is also a possible state    
            
    return max(freqs.values()) # return maximum encountered frequency
