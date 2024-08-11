with open("rosalind_dna.txt") as f:
    N = {'A': 0, 'G': 0, 'T': 0, 'C':0}
    content = f.read().strip()
    for i in content:
        N[i] += 1
    print(N['A'], N['C'], N['G'], N['T'])



