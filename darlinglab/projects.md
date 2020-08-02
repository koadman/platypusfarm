---
layout: page
title: Projects
permalink: /projects/
---

Our group has several ongoing research projects that roughly fall into the following themes.


- <h4>Algorithms for metagenome analysis</h4> Our work in this space includes the development of new analysis methods as well as contributing to community-driven efforts to evaluate the performance of publicly available metagenome data analysis methods. Examples of our work in this space include:
  * Contributions to the [Critical Assessment of Metagenome Interpretation](https://data.cami-challenge.org/). This is an ongoing community-driven effort to evaluate metagenome data analysis tools. Our first publication appeared in [Nature Methods](https://www.nature.com/articles/nmeth.4458) in 2017.
  * Methods to analyse metagenome Hi-C data. This stream of work includes the [bin3C tool](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-019-1643-1) for reconstructing individual genomes from a community sequenced with metagenomic Hi-C, and the related data analysis tools [sim3C](https://academic.oup.com/gigascience/article/7/2/gix103/4628124), and [qc3C](https://github.com/cerebis/qc3C).
  * Methods to resolve the genomes of strains from metagenomic assemblies. Together with Dr. Chris Quince and other international collaborators we have been developing statistical methods for strain genome resolution using time-series sampled data, Hi-C data, and long read data. We published a method, [DESMAN](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-017-1309-9), for this task and continue to work on [new methods](https://github.com/koadman/graphdeconvolution).
  * New methods to estimate the rates of recombination for microbial populations from metagenomic data.
 <br/> <br/>
- <h4>Development of advanced DNA sequencing technologies</h4> We are developing advanced DNA sequencing technologies via tightly coupled development of computational inference methods and next-generation sequencing techniques. Two examples of our work in this area are the development of [metagenomic Hi-C](https://peerj.com/articles/415/) and a technique for [full length 16S ribosomal gene sequencing](http://biorxiv.org/content/early/2014/11/06/010967) on the Illumina MiSeq in collaboration with Dr. Catherine Burke. That work led to a spin-out company to commercialize a new long read sequencing technology, which in 2019 emerged from stealth mode with the announcement of [Morphoseq](https://longastech.com).

- <h4>Understanding the development of the infant gut microbiome</h4> We are working to understand how the infant's microbiome develops, in humans and in animals, and its relationship with maternal microbiota and infant health status.
  * In collaboration with the NSW Department of Primary Industries, we are participating in a large project to evaluate the effect of probiotics and antibiotics on postweaning piglets. This work has yielded a very large metagenomic timeseries dataset and has revealed that microbial community development in piglets [appears to be tightly structured](https://www.biorxiv.org/content/10.1101/2020.07.20.211326v1). 
  * In collaboration with a large team led by [Prof. Shyamali Dharmage](https://findanexpert.unimelb.edu.au/display/person3474) and with support of the National Health and Medical Research Council, we are studying the microbiota found in the breast milk of families that are at risk for atopy.
 <br/> <br/>
- <h4>Bayesian phylogenomic inference</h4> We are developing new, scalable phylogenetic analysis methods using Monte Carlo methods, including Variational Inference, Sequential Monte Carlo, MCMC, and approximate Bayesian computation. We have a particular interest in the application of these methods to bacteria, and the analysis challenges introduced by bacterial recombination and horizontal gene transfer. Some examples of our work in this space include:
  * The [PhyloStan software](https://github.com/4ment/phylostan) which implements a research prototype for the application of probabilistic programming and variational inference to phylogenetic models. This software provides a means to carry out Bayesian inference on continuous phylogenetic model parameters such as branch lengths, and historical population sizes. A peer reviewed manuscript describing the [design and evaluation of PhyloStan](https://peerj.com/articles/8272/) is available.
  * The [STS software](https://github.com/OnlinePhylo/sts) is a prototype for online phylogenetic inference via Sequential Monte Carlo. The work behind STS is described in two corresponding manuscripts: [one on the underlying theory](https://academic.oup.com/sysbio/article/67/3/503/4735261), and another describing [the STS algorithm and its performance](https://academic.oup.com/sysbio/article/67/3/490/4665707).
  * The [beagle library](https://github.com/beagle-dev/beagle-lib). BEAGLE is a library that provides a single uniform programming interface for high performance implementations of phylogenetic likelihood and gradient calculations across a variety of compute architectures. The library currently contains specialized likelihood calculators for SSE, OpenMP, and GPU-enabled computation via CUDA and OpenCL kernels.
  * New methods to identify the recombinant parts of a genome and to improve the estimation of the clonal genealogy for bacteria.


