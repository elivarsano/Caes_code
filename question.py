def is_samePatterns(colors, patterns):    
    if len(colors) != len(patterns):
        return False    
    sdict = {}
    pset = set()
    sset = set()    
    for i in range(len(patterns)):
        pset.add(patterns[i])
        sset.add(colors[i])
        if patterns[i] not in sdict.keys():
            sdict[patterns[i]] = []

        keys = sdict[patterns[i]]
        keys.append(colors[i])
        sdict[patterns[i]] = keys
    print(sdict)
    if len(pset) != len(sset):
        return False   

    for values in sdict.values():

        for i in range(len(values) - 1):
            if values[i] != values[i+1]:
                return False

    return True

print(is_samePatterns(["red", 
 "green", 
 "green"], ["a", 
 "b", 
 "b"])) 

print(is_samePatterns(["red", 
 "green", 
 "greenn"], ["a", 
 "b", 
 "b"])) 