def G(a,b) :
    if b==0:
        return 1
    else:  
        return b*G(a,b-1)
print(G(3,7))