#!/usr/bin/env python
import numpy as np

subst_matrix = [
# A  C  G  T
[+1,-1,-1,-1],  # A
[-1,+1,-1,-1],  # C
[-1,-1,+1,-1],  # G
[-1,-1,-1,+1]   # T
]
gap_penalty = -4

seq_1 = "TACG"
seq_2 = "TGG"

# maps between chars and indices
ch = {"A":0,"C":1,"G":2,"T":3}
rch = {0:"A",1:"C",2:"G",3:"T"}

# this will store our dynamic programming matrix
dp_matrix = np.ndarray(shape=(len(seq_1)+1,len(seq_2)+1), dtype=int)
dp_matrix.fill(0)

# storage for back pointers
# 0 for up, 1 for diag, 2 for left
back_ptr = np.ndarray(shape=(len(seq_1)+1,len(seq_2)+1), dtype=int)
back_ptr.fill(-9)

# fill the DP matrix
for i in range(len(seq_1)+1):
    for j in range(len(seq_2)+1):
        if i==0 and j==0: continue # skip the first cell

        # 
        # students must fill in 'scores' here
        scores = [-999,-999,-999]
        if( i>0 ):
            scores[2] = dp_matrix[i-1,j] + gap_penalty
        if( j>0 ):
            scores[0] = dp_matrix[i,j-1] + gap_penalty
        if( i>0 and j>0 ):
            scores[1] = dp_matrix[i-1,j-1] + subst_matrix[ ch[seq_1[i-1]] ][ ch[seq_2[j-1]] ]

        # select the best previous cell
        best = max(scores)
        dp_matrix[i,j]=best
        for k in range(3):
            if scores[k] == best:
                back_ptr[i,j] = k

print "Dynamic programming matrix:"
print dp_matrix
print "\nBack pointers:"
print back_ptr

# read out the backtrace
aln_1 = ""
aln_2 = ""
i=len(seq_1)
j=len(seq_2)

while i>0 or j>0:
    if back_ptr[i,j] == 0: # left
        aln_1 += "-"
        aln_2 += seq_2[j-1]
        j -= 1
    if back_ptr[i,j] == 1: # diag
        aln_1 += seq_1[i-1]
        aln_2 += seq_2[j-1]
        i -= 1
        j -= 1
    if back_ptr[i,j] == 2: # up
        aln_1 += seq_1[i-1]
        aln_2 += "-"
        i -= 1

aln_1 = aln_1[::-1] # reverses the string
aln_2 = aln_2[::-1]

print "\nAlignment:"
print(aln_1)
print(aln_2)

