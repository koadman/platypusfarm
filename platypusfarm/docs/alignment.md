# Exercise: sequence alignment algorithms

This exercise explores the use of dynamic programming for sequence alignment.

## Obtain the dynamic programming framework script

A python script containing a partial implementation of dynamic programming for global sequence alignment can be found here:

* [alignment.py]()

Just save this script wherever is convenient and open it with a text editor.

## Implement the computation of scores in the script

This requires the score calculation to be implemented for each of the three predecessor cells in the matrix -- the cell above, to the left, and diagonal.
To do so, edit lines 33-49 of the script to implement the scoring function described in the lecture notes.

```
        # 
        # 'scores' must be filled in here
        #
        scores = [-999,-999,-999]
        if( i>0 and j>0 ):  
            # score diagonal
            # scores[1] = 
            pass
        if( i>0 ): 
            # score up: gap in sequence 2
            # scores[2] = 
            pass
        if( j>0 ): 
            # score left: gap in sequence 1
            # scores[0] = 
            pass
```

## Run the script

This can be done by running:

```
python alignment.py
```

If the score function has been implemented correctly, you should see the following values in the dynamic programming table:

```
Dynamic programming matrix:
[[  0  -4  -8 -12]
 [ -4   1  -3  -7]
 [ -8  -3   0  -4]
 [-12  -7  -4  -1]
 [-16 -11  -6  -3]]
```

And the following sequence alignment should be reported:

```
Alignment:
TACG
TG-G
```

If your results don't look like this, go back and carefully check how you've implemented the score calculation.

## Investigating an unknown protein

Imagine you are working with a forensic laboratory on a sample from a criminal investigation. Liquid was found inside a vial at a suspect's garage laboratory, but the contents of the liquid are unknown. Analysis of the sample has so far determined that it contains a high concentration of a protein with the following sequence:

```
CAKKRNWCGKNEDCCCPMKCIYAWYNQQGSCQTTITGLFKKC
```

You have been asked to determine what this protein is, and whether it has any relevance to the investigation.

How would you do this?

[hint](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins)

