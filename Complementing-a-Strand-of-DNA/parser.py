with open('./rosalind_revc.txt') as f:
    content = f.read().strip()
    content = content[::-1]
    new_strand = ""
    for n in content:
        if n == 'A':
            new_strand += 'T'
        elif n == 'T':
            new_strand += 'A'
        elif n == 'G':
            new_strand += 'C'
        elif n == 'C':
            new_strand += 'G'

    print(new_strand)

