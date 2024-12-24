from itertools import permutations

def solve(filename):
    with open(filename, 'r') as f:
        G = {i+j*1j: c for i,r in enumerate(f) for j,c in enumerate(r.strip())}
    for r in [1], range(50):
        anti = []
        for freq in {*G.values()} - {'.'}:
            ants = [p for p in G if G[p] == freq]
          
            pairs = permutations(ants, 2)
            print(pairs)
            anti += [a+n*(a-b) for a,b in pairs for n in r]
        result = len(set(anti) & set(G))
        print(result)

solve('/Users/.../2024/input.txt')