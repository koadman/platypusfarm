# Exercise: sequence alignment algorithms

This exercise explores the use of dynamic programming for sequence alignment.

## Obtain the dynamic programming framework script

A python script containing a partial implementation of dynamic programming for global sequence alignment can be found here:

* [alignment.py](alignment.py)

This script can either be saved and edited from a text editor, or, if you have a Jupyter notebook available it can be copied into the notebook and run from there.

Google offers a free Jupyter notebook service for anyone with a google account: [https://colab.research.google.com](https://colab.research.google.com)

## Implement the computation of scores in the script

This requires the score calculation to be implemented for each of the three predecessor cells in the matrix -- the cell above, to the left, and diagonal.
To do so, edit lines 35-51 of the script to implement the scoring function described in the lecture notes.

```
        # 
        # YOUR TASK: 'scores' must be filled in here
        #
        scores = [-999,-999,-999]
        if( i>0 and j>0 ):  
            # score diagonal
            #scores[1] = 
            pass
        if( i>0 ): 
            # score up: gap in sequence 2
            #scores[2] = 
            pass
        if( j>0 ): 
            # score left: gap in sequence 1
            #scores[0] = 
            pass
```

## Run the script

This can be done on the command-line by running:

```
python alignment.py
```

Or run from within the notebook.


If the score function has been implemented correctly, you should see the following values reported in the dynamic programming table:

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

## The effect of changing the substitution scoring matrix

As described in the lecture notes, the substitution scores are transformed probabilities that each type of mutation has taken place.
Usually some types of mutations are more common than others, and this can be modeled by unequal substitution penalties.

How can the substitution matrix be changed so that the following alignment is reported?

```
Alignment:
TACG
T-GG
```

Can you change the scoring system to achieve this alignment?

```
Alignment:
T-ACG
TG--G
```



## Investigating an unknown protein

Imagine you are working with a forensic laboratory on a sample from a criminal investigation. Liquid was found inside a vial at a suspect's garage laboratory, but the contents of the liquid are unknown. Analysis of the sample has so far determined that it contains a high concentration of a protein with the following sequence:

```
CAKKRNWCGKNEDCCCPMKCIYAWYNQQGSCQTTITGLFKKC
```

You have been asked to determine what this protein is, and whether it has any relevance to the investigation.

How would you do this?

[hint](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Proteins)




