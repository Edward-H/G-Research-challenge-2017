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
            query = s[:len(w)]
            if mis and l_dist(query,w)<len(w)/4+1:
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


def l_dist(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]
