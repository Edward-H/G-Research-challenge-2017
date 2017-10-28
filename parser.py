"""Parse string"""

def parse(s,wrds=[],mis=False):
    result=[]
    while len(s)>0:
        if s.startswith(" "):
            s=s[1:]
            continue
        for w in wrds:
            if s.startswith(w):
                result.append(w)
                s=s[len(w):]
                break
        else:
            k=s.find(" ")
            if k==-1:
                result.append(s)
                return result
            else:
                result.append(s[:k])
                s=s[k:]
    return result
