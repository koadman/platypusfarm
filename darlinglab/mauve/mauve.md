---
layout: mauvepage
title: Mauve
---

![The Mauve logo](mauve_logo2.png)

### Mauve is no longer maintained

The software remains freely available, but is no longer under active development by the original authors. There is no guarantee of support or that any emails to the authors will be answered (not that there ever was such a guarantee!).

### About Mauve

Mauve is a system for constructing multiple genome alignments in the presence of large-scale evolutionary events such as rearrangement and inversion. Multiple genome alignments provide a basis for research into comparative genomics and the study of genome-wide evolutionary dynamics. 

Mauve has been developed with the idea that a multiple genome aligner should require only modest computational resources. It employs algorithmic techniques that scale well in the lengths of sequences being aligned. For example, a pair of _Y. pestis_ genomes can be aligned in under a minute, while a group of 9 divergent Enterobacterial genomes can be aligned in a few hours. However, the current algorithm's compute time (progressiveMauve) scales cubically in the number of genomes to align, making it unsuitable for datasets containing more than 50-100 bacterial genomes.

Mauve development began at the University of Wisconsin-Madison with a team including Aaron Darling, Bob Mau, and Nicole Perna. Several others have contributed development to aspects of the Mauve software in the time since.
