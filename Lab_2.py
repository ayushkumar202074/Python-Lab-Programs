def toString(List):
    return ''.join(List)

def Permute(s, i, size): 
    if i==size: 
        print(toString(s))
    else: 
        for j in range(i, size): 
            # Swaping
            s[i], s[j] = s[j], s[i] 
            Permute(s, i+1, size) 
            s[i], s[j] = s[j], s[i]  
  

string = "CUH"

Permute(list(string), 0, len(string))
