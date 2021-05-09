def solution(n, k, cmd):
    original = ['O']*n
    delete = []
    new = 'O'*n
    
    for cd in cmd:
        if cd == 'C':
            if k == n-1 or 'O' not in original[k+1:]:
                original[k] = 'X'
                delete.append(k)
                steps = 1
                while steps > 0:
                    k -= 1
                    if original[k] == 'X':
                        continue
                    else:
                        steps -= 1
            
            else:
                try:
                    original[k] = 'X'
                    delete.append(k)
                    steps = 1
                    tmp_k = k
                    while steps > 0:
                        tmp_k += 1
                        if original[tmp_k] == 'X':
                            continue
                        else:
                            steps -= 1
                    k = tmp_k
                    
                except:
                    original[k] = 'X'
                    delete.append(k)
                    steps = 1
                    while steps > 0:
                        k -= 1
                        if original[k] == 'X':
                            continue
                        else:
                            steps -= 1
                            
        elif cd == 'Z':
            a = delete.pop()
            original[a] = 'O'
                
        else:
            to, steps = cd.split()
            steps = int(steps)
            if to == 'D':
                while steps > 0:
                    k += 1
                    if original[k] == 'X':
                        continue
                    else:
                        steps -= 1
                        
            elif to == 'U':
                while steps > 0:
                    k -= 1
                    if original[k] == 'X':
                        continue
                    else:
                        steps -= 1
    
    new = ''.join(original)
    return new