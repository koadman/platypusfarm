# Annotate an assembled genome with Prokka

This tutorial assumes you have already assembled a genome with SPAdes inside the Microbial GVL.
See the "[Genome assembly with SPAdes](assembly)" page for instructions on how to do that.

## Launch the Prokka annotation

1. Click the "NGS: Annotation" link at left
2. Scroll down and select "Prokka" in the left side drop down menu
3. Set the "Locus tag prefix" to a single letter, e.g. N
4. Select "Yes" for "Force GenBank/ENA/DDJB compliance (--compliant)". This is essential in order to visualize annotations in the [Mauve software](http://darlinglab.org/mauve).
5. Set the sequencing centre name to a single letter, e.g. Z. It is necessary to set this and the locus tag prefix to a single letter so that Prokka can create contig names that are short enough to be GenBank compliant (as selected in step 4). If you will not be viewing genomes in Mauve then any locus tag prefix and sequencing centre name can be given.
6. Optionally enter in any other relevant parameters
7. Click the "Execute" button
8. Upon completion, the status tabs in the right sidebar will turn green and results can be viewed by clicking the eye icon.


Once this is done, it is possible to download the annotated genome in GenBank format by clicking the "Prokka on data N: gbk" link in the right sidebar, then clicking the floppy disk icon.

**Important**: Galaxy sets the GenBank file format extension to ".txt" instead of ".gbk" when it is downloaded. This can cause problems with other software, such as Mauve, which depends on the file extension to indicate the file format. Therefore it may be necessary to rename downloaded file to set the extension to .gbk. Instructions on how to do this in Windows [can be found via google](http://lmgtfy.com/?q=changing+a+file+extension+in+windows)
