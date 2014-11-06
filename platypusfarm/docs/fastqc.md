# Using FastQC for basic run quality metrics

This tutorial assumes you have a GVL instance running already in the NeCTAR cloud.
See the "[Initial setup](gvlsetup)" page for instructions on how to get that going.

## Obtain the example data

Download the example datasets:

* [MiSeq Nano Read 1](http://darlinglab.org/data/demux/Undetermined_S0_L001_R1_001.fastq.gz)
* [MiSeq Nano Index Read 1](http://darlinglab.org/data/demux/Undetermined_S0_L001_I1_001.fastq.gz)

These files contain the first reads and the first index reads from a run generated on the UTS MiSeq in gzip compressed FastQ format.

Just save them wherever is convenient.

## Upload the files to the GVL Galaxy system

1. Click the "Get Data" -> "Upload File From Your Computer" links at the left side of the page
2. Click the "Choose File" button and select one of the sequence files
3. Click the "Execute" button
4. Repeat for the other file

## Carry out a FastQC analysis

1. Click the "NGS: QC and manipulation" link at left
2. Scroll down and select "FastQC:Read QC" in the left side drop down menu
3. Select the file to analyze in the main panel
4. Click the "Execute" button
5. Upon completion, click the "View Data" icon (looks like an eye)
6. Repeat for the other file



