

def mutate_string(string, position, character):
    res = list(s) 
    i=int(position)
    res.insert(i, c) 
    res = ''.join(res) 
    res=list(res)
    del res[i+1]
    res = ''.join([element for element in res]) 
    return res

