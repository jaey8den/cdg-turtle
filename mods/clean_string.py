# Removing whitespace and indexing reps and patterns
def PrepareString(str):
    str = str.replace("SL ST", "SLST")
    str = str.replace(",", "")
    str = str.replace(" ", ",")
    return str

# Separate layers by ;
def SeparateLayers(str):
    return str.split(";")

# Group patterns enclosed by brackets
def GroupBrackets(arr):
    stk = [] # queue
    res = [] 
    bracketFlag = False # true if bracket is open

    for i, c in enumerate(arr):
        if c == "," and not bracketFlag:
            if stk:
                res.append("".join(stk))
                stk.clear()
        elif c == "(":
            bracketFlag = True
        elif c == ")":
            res.append("".join(stk))
            stk.clear()
            bracketFlag = False
        else:
            stk.append(c)

    # Append any remaining patterns in the stack
    if stk:
        res.append("".join(stk))

    return res

# Open brackets
def ExpandBrackets(arr):
    l = 0 # left pointer
    r = 1 # right pointer
    res = []

    while (l < len(arr)):
        # Non repeated pattern
        if not arr[l].isnumeric():
            res.append(arr[l])
            l += 1
            r += 1
        # Bracketed patterns
        elif (len(arr[r].split(",")) > 1):
            res.append("MT")            
            for i in range(int(arr[l])):                
                for j in arr[r].split(","):
                    res.append(j)
                res.append("MT")
            l += 2
            r += 2
        # Repeated patterns
        else:
            res.append(arr[l])
            res.append(arr[r])
            l += 2
            r += 2
    
    return res

# Open repetitions
def OpenReps(arr):
    l = 0
    r = 1
    res = []

    while (l < len(arr)):
        if not arr[l].isnumeric():
            res.append(arr[l])
            l += 1
            r += 1
        elif arr[r] == "CH":
            res.append(arr[l] + " " + arr[r])
            l += 2
            r += 2
        else:
            for i in range(int(arr[l])):
                res.append(arr[r])
            l += 2
            r += 2

    return res

# All together
def CleanString(str):
    str = PrepareString(str)
    arr = SeparateLayers(str)
    for i in range(len(arr)):
        arr[i] = GroupBrackets(arr[i])
        arr[i] = ExpandBrackets(arr[i])
        arr[i] = OpenReps(arr[i])
    return arr