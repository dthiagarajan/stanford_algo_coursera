from random import choice
from copy import deepcopy

def contract(v1, v2, G):
    G[v1].extend(G[v2])
    for v in G[v2]:
        l = G[v]
        for i in range(0, len(l)):
            if l[i] == v2:
                l[i] = v1
            
    while v1 in G[v1]: 
        G[v1].remove(v1)    
    del G[v2]

def random_contraction(G):
    while len(G) > 2: 
        a = choice(list(G.keys())) 
        b = choice(G[a]) 
        contract(a, b, G) 
    return len(G.popitem()[1]) 

def main():
    with open('graph.txt', 'r') as f:
	    G = {int(line.split()[0]): [int(val) for val in line.split()[1:] if val] for line in f.readlines() if line}
	    mincut = float("inf") 

    for i in range(1000): 
    	print 'Working on ' + str(i) + '-th iteration'
        curr = random_contraction(deepcopy(G))
        if curr < mincut:
            mincut = curr
    	print("The min cut is:", mincut)

if __name__ == '__main__':
    main()