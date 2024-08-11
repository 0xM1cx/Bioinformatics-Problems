'''
PROBLEM:
    An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
'''
with open('./rosalind_rna.txt') as f:
    content = f.read().strip()
    new = []
    for i in content:
        if i == 'T':
            i = 'U'

        new.append(i)

    print(''.join(new))

