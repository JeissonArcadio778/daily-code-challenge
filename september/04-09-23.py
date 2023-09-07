a = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



def getTotalX(a, b):
    
    a.sort()
    
    p_b = []
    finals = []
    
    for i in a:
        for j in range(a[0], a[-1] + 1):
            if i % j == 0 or j % i == 0:
                p_b.append(j)
    
    unique_p_b = list(set(p_b))
    unique_p_b.sort()
    print(unique_p_b)
    
    for i in b:
        for j in range(unique_p_b[0], unique_p_b[-1] + 1):
            if i % j == 0 or j % i == 0:
                finals.append(j)
    
    
    print(list(set(finals)))
    res = list(set(finals))
    print(res)

    real = []

    for i in a:
        for j in range(res[0], res[-1] + 1):
            if i % j == 0 or j % i == 0:
                real.append(j)
    

    print(real)
    return len(real)

getTotalX(a,b)



        
