---
layout: post
title:  "An open peer review of NxRepair"
date:   2015-01-07 07:19:50
category: reviews
---

I was recently asked to carry out a peer review for a manuscript discussing a topic which I have previously worked & published on.
The manuscript describes an algorithm to detect misassembled genome sequences, and the manuscript draft is available as a preprint on PeerJ:
[NxRepair: Error correction in de novo sequence assembly using Nextera mate pairs](https://peerj.com/preprints/747/). I have to applaud the authors of the work for aggressively pursuing the path open science, not only by publishing their code and putting a preprint online, but also by choosing to work with a venue that facilitates open peer review. I'm already a fan.

But wait, there's a flipside. As you'll discover in the review below, I am concerned that the work may need some pretty heavy duty revision. Since the preprint is available to the general public I would like to communicate my thoughts about the manuscript to the same audience. Of course the manuscript's authors will undoubtedly see these comments too, possibly from this blog post even before the journal sends them. I sincerely hope that my comments can be taken constructively, viewed in a positive light, and used to help improve the science. Candid communication and critical thinking are going to be foundational elements that help us to advance the open science movement.

Review in PeerJ format follows.

### Basic reporting


The manuscript describes an algorithm and corresponding software implementation to detect misassemblies in de novo genome assemblies using mate pair sequence data. de novo genome assembly is a highly active area of research, driven by ongoing advances in sequencing technologies. Many of the current generation of assemblers are prone to misassembling regions of genomes that contain high identity repetitive elements, especially those that are at or above the read length or in some cases the size of k-mers used for de bruijn graph-based algorithms. It is exciting to see new efforts to solve these problems.
The context in which a tool such as this would be used could be better introduced. One case is when the initial draft assembly algorithm is unable to incorporate mate-pair information, and a subsequent scaffolding step is to be carried out. In this situation, if the initial assembly contains errors, the scaffolder will be unable to accurately scaffold the assembly with mate-pair data unless the errors are detected and corrected prior to scaffolding. This approach is used for example in the A5 and A5-miseq pipelines. However, it is possible in principle to construct an assembler which leverages the mate pair information directly during the contigging process to avoid such errors in the first place. For such assemblers, a tool like this may not provide any added utility. This kind of information on the scope of applicability could be better introduced.


### Experimental Design

Overall I think enough of the algorithm was described to understand how it works, however I have a number of questions about the rationale for the design of the method which I have detailed below in the General Comments section. Unfortunately I'm afraid that the design of the accuracy evaluation experiment leaves us with little idea of the method's expected behavior on real datasets. This is because the method appears to have been tuned (T parameter, ROC curves) on the same data for which accuracy is reported. If this is not the case, then the manuscript text needs to be revised to clarify the issue. I am also concerned that no effort has been made to compare the method's performance to previous work to solve the same problem, for example the A5qc module used by the A5 pipeline to detect and correct misassemblies. It is erroneously stated in the introduction that no other software is optimized to work with mate-pair data, yet A5qc does and in fact the use of mate-pairs to detect misassembled contigs was the main motivating use case in its development. The A5 manuscript ([Tritt et al 2012 PLoS ONE](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0042304)) discusses its use with mate pair datasets explicitly. A5qc is by no means perfect and is likely to be a bit challenging to use independently of the rest of the pipeline, but that is no excuse for inaccurately representing its application scope and neglecting to benchmark it. Indeed, I suspect A5qc may be able to detect some misassemblies that the present method can not, because the present method is limited to identifying misassemblies where read pairs map entirely within a single contig, whereas A5qc can identify misassemblies involving read pairs that map to different contigs. I would also guess that the present method may be more sensitive than A5qc for the within-contig misassemblies. There could be other tools that are relevant for comparative benchmarking; I have not kept up with the literature in this area.




### Validity of the findings

The main issue potentially impacting the validity of the findings is whether the test data were also used for selection of the T parameter. The test datasets are relatively limited, comprising less than 10 genomes, which leaves a non-negligible potential for parameter overfitting.

Note that I did not (yet) evaluate the software itself by running it on my own datasets, in light of the other issues that I think should be addressed first.




### General comments for the author

The following are specific notes that I made while reading the manuscript:

+ Abstract: de bruijn assemblers are clearly the most prevalent for Illumina data, but is the scope of applicability really limited to de bruijn assemblers?

+ Introduction, paragraph 2: The [Tritt et al 2012](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0042304) citation is much more appropriate for A5 in this context, as it describes a technique to use mate pair reads to detect and correct assembly errors. The [Coil et al 2014](http://arxiv.org/abs/1401.5130) paper does not include details of that technique, nor does it contain any revisions of that technique.

+ "Statistical analysis of mate pair insert sizes" paragraph 1: The use of a uniform to model the mate-pair noise makes sense, but it's not clear how appropriate the normal would be for nextera, unless a tight fragment size range has been gel extracted. If data from gel extraction is expected it should be mentioned, and some further discussion is warranted in either case.

+ same section, paragraph 2: the definition of spanning is somewhat ambiguous. do the read pairs spanning site i include only read pairs with one read entirely before i and the other entirely after? or are pairs where one or both reads actually include i considered 'spanning'? and for a region to be spanned, which of these definitions is correct?

+ same section, eqn 1: an extra set of P's in the second terms of the numerator & denom would help improve clarity, also there's no need for the first equation -- why not just define the notation for the prior \pi_x up-front and give eqn 2?

+ same section, eqn 2: The same insert size on a contig of different lengths would give different values for this expression, because the uniform distribution has been defined only over the contig length. Is that intentional? Desirable? The rationale for this decision is not obvious and some explanation is in order.

+ same section, paragraph 3: It seems like the same process used to estimate the insert size distribution parameters would naturally also yield an estimate of \pi_0. Is that used? I have seen mate pair error levels as high as 20% in some libraries. It's highly sensitive to the lab conditions, so would be ideal to estimate from the data rather than use a fixed value.

+ same section, eqn 4: what about circular molecules, e.g. plasmids? a large number of pairs near the contig ends will appear to be in the wrong orientation...

+ same section, eqn 5: why do we need to calculate these contig-specific distributions? is it to deal with local deviation in coverage? or is it because the distributions used in eqn. 1 have a contig-local domain? or something else? some explanation is needed.

+ same section, eqn 6: it's a bit strange that this approach starts out with the Bayesian framework (e.g. the use of a prior probability) then goes into a frequentist framework for the hypothesis test. One way to keep it Bayesian would be to set up a Bayes factor of the competing hypotheses of no misassembly vs. one or more misassemblies in the target window. then the threshold T could be applied to the Bayes factors instead of the standard deviation.

+ section "Global Assembly Parameters", eqn 7: the notation for MAD is not quite right, as it suggests taking the median of a single data point in Y.

+ same section, eqn 7: at high enough levels of noise in the mate pair library, this approach is likely to overestimate the true insert size to some extent. The 30kbp threshold will help mitigate the problem, and the later steps to identify extreme divergence from a contig's background will also reduce the noise, but this likely comes with a cost in sensitivity for misassembly detection.

+ same section eqn 8: why use this approach instead of one of the other common approaches to calculate standard deviation?

+ section "Interval Sequence Tree construction": How is the interval sequence tree used in this algorithm? it's not clear at what step in the breakpoint detection the IST gets queried. This should either be explained or the whole section omitted.

+ section "ROC plots" eqn 10: The FPR here is sensitive to how finely the contigs are sliced into windows because it includes true negatives. 

+ section "Workflow pipeline": nice to see the precision here: exact version & command line

+ same section: what version of QUAST? they do change a little from one release to the next.

+ same section, bwa commands: again, versions would be good, even better would be a script that reproduces all the results!

+ same section nxrepair.py commands: you might want to indicate which version of NxRepair produced the results described here in case you ever fix bugs or make improvements...


