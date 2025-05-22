#Write a reverse complement function (and package it up as a program) as
#compactly as possible (1-2 lines), using the techniques introduced today.
#   Hint: Use a dictionary for complement, reversed on the sequence, list
#         comprehension to apply the get method of the dictionary, and the
#         join method for strings.

seq = "ATCGTACG"
# reverse = "GCATGCTA"
# rev comp = "CGTACGAT"

dna_comps = {"A": "T", "T": "A", "C": "G", "G": "C"}

def rev_comp(dna_string):
    return ''.join(dna_comps.get(i) for i in reversed(dna_string)) # reversed built in function
print('Reverse complement:',rev_comp(seq))
