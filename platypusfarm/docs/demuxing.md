# Demultiplexing custom sample barcodes with PhyloSift

This tutorial assumes you have a GVL instance running already in the NeCTAR cloud.
See the "[Initial setup](gvlsetup)" page for instructions on how to get that going.
We will further assume that you've logged in to the instance with ssh.

Alternatively, it should be possible to run the tutorial locally in the terminal on a Mac or Linux machine.

## Obtain the latest PhyloSift

     curl -O http://edhar.genomecenter.ucdavis.edu/~koadman/phylosift/devel/phylosift_20141105.tar.bz2
     tar -xjf phylosift_20141105.tar.bz2
     export PATH="$PATH:`pwd`/phylosift_20141105/bin"

The first command downloads PhyloSift using curl, the second command unzips it, and the third command adds it to your executable binary program path.

## Obtain the example data
    
    curl -O http://darlinglab.org/data/demux/Undetermined_S0_L001_I1_001.fastq.gz
    curl -O http://darlinglab.org/data/demux/Undetermined_S0_L001_I2_001.fastq.gz
    curl -O http://darlinglab.org/data/demux/Undetermined_S0_L001_R1_001.fastq.gz
    curl -O http://darlinglab.org/data/demux/Undetermined_S0_L001_R2_001.fastq.gz

The above commands use curl to download an Illumina dataset produced on the UTS MiSeq.

## Create a PhyloSift barcode table file

The barcode table file records all of the possible barcodes that could be used and their features.
It does not record which samples have which barcodes.
The barcode table file is a tab-separated values file (sometimes called .tsv or .csv) and can be created in LibreOffice or Excel or another spreadsheet program or text editor.
For the tutorial dataset we will download and use a barcode set as follows:

    curl -O http://darlinglab.org/data/demux/barcodes.csv

The first few lines of that file look like this:

    #barcode	bc_name	read_id	trim_len	random_pos	random_len	linker_seq
    AACCAT	1	2	0	6	6	
    AAGTTC	2	2	0	6	6	
    AATACG	3	2	0	6	6	
    

The above barcode set is one that we have been using at UTS with custom synthesized Nextera oligos from IDT.
In Nextera and current TruSeq libraries the barcodes are read as separate reads, the 2nd and 3rd to be primed on the sequencer.
Our custom oligos contain a randomly synthesized region of 6 bases, starting after the sample barcode, this is indicated in the `random_pos` and `random_len` columns. Some library designs put the barcode at the start of the first read and occasionally follow it with a linker sequence.
For such libraries, the amount of sequence to trim from the start of the read can be indicated in the `trim_len` column and the linker sequence itself indicated in the `linker_seq` column.

## Create a sample table file

The next ingredient in the recipe is a file describing the correspondence between samples and barcodes.
For the example files we will use the following map:

    #Sample_Name    Barcode1     Barcode2
    S1	AATACG	ACGGTT
    S2	AATACG	TAGCGC
    S3	AATACG	GGTTCT
    S4	AATACG	CTTGCC
    S5	ATACTC	GGTTCT
    S6	ATACTC	AGGCCT
    S7	ATACTC	TCATAC
    S8	AGGAGC	AGGCCT
    S9	AGGAGC	CTTGCC
    S10	AGGAGC	TCATAC
    S11	AAGTTC	ACGGTT
    S12	AAGTTC	CTTGCC
    S13	AAGTTC	CTACCT
    S14	AAGTTC	TCATAC
    S15	TATAGT	ACGGTT
    S16	TATAGT	CTTGCC
    S17	TATAGT	CTACCT
    S18	TATAGT	TCATAC
    S19	CGGAAT	ACGGTT

Rather than copying that into a text file, it will be easier to just download it:

    curl -O http://darlinglab.org/data/demux/samples.csv



## Run phylosift to demultiplex the samples

    phylosift demux --disable_updates --output=platypi --sample-map=samples.csv \
    --barcode-table=barcodes.csv --rev-barcode=2 --swap-barcodes .

This will run for a while, producing lines of output like this:

    ...
    Mapping barcode CTTGCC:ACTATA to S16
    Mapping barcode CTACCT:ACTATA to S17
    Mapping barcode TCATAC:ACTATA to S18
    Mapping barcode ACGGTT:ATTCCG to S19
    Barcode length is 6
    Processing ./Undetermined_S0_L001_R1_001.fastq.gz
    i1_file ./Undetermined_S0_L001_I1_001.fastq.gz
    i2_file ./Undetermined_S0_L001_I2_001.fastq.gz
    r2_file ./Undetermined_S0_L001_R2_001.fastq.gz
    
    207 / 924 / 1000 reads: matching samples / matching barcodes / total
    427 / 1848 / 2000 reads: matching samples / matching barcodes / total
    640 / 2760 / 3000 reads: matching samples / matching barcodes / total
    873 / 3676 / 4000 reads: matching samples / matching barcodes / total
    1101 / 4613 / 5000 reads: matching samples / matching barcodes / total
    1332 / 5547 / 6000 reads: matching samples / matching barcodes / total
    ...

And eventually finishing with a report of how many reads were assigned to each barcode.
Note that phylosift allows each barcode to contain up to one mismatch; a pair of barcodes could have a mismatch in each barcode in the pair.
The above command produces a demultiplexed file called `platypi.fastq.gz` with the following contents:

    @S11_1 M00607:72:000000000-D0B10:1:1101:15662:1335 1:N:0:0 barcode=ACGGTT:GAACTT random=::GGACTA:ACGATG:
    CTATTTCATCGTCAATCGCTGGCTGCGCGTCGCGACGTTCGTGGTGGCCGTGCTGGTGGTGATGCCGCTGTGGCAGGCCGGCAGCGGGCTGATGGCGCGCGTCGTCGCGCCGGCCCAGTCGCAGGCGAACGTGGCGGGCGCCACGCGCGT
    +
    BCBBBFFFFFFCGGGGGGGGGGGHGGGGGGGGGGGGGEGHGGGGHGGHHGGGGGHHHHGFGHHHHHGGGGFHHHHGGGGGGGGGGGGGGGGGHHHHGGGGGGGGGGGCGGGG?DGGGGGGGFFFFFFFFFFEEEFFFB;BCADDAAAB=C
    @S11_1 M00607:72:000000000-D0B10:1:1101:15662:1335 2:N:0:0 barcode=ACGGTT:GAACTT random=::GGACTA:ACGATG:
    GTTCAGCAACGACTGGACCGTGTAGCCGGCGCCCGCCAGTTGCGAGAACAGGTGGCACTGCTGCGGTGCGGGCTTGTACAGGTCCGCATGCGCCTCCTGCCCGCAGCTCGCGCGCAGCACGCGGATCGCGGCCGGGCCGCTGTAGCTCGCG
    +
    AAABCFFFFFDBGGGGGGGGEGHHHHHGGGGCGGGGGGGHGFGGGGGGHHHHHHEHHHGHHHHHGEEGGGGEEGHGGHHHGFHGHGGGGGHGGGFCFHGGHHGGGGGEHDGFGGGGGGGHGGGGGGGGGGAFFFFFFFFFFFFFFFFFFF@
    @M00607:72:000000000-D0B10:1:1101:16052:1335 1:N:0:0 barcode=CTTGCC:CGTTCC random=::GGCCTC:GCTTGG:
    GCCACCACAGCGCGATGCCGGTGCCGATCATCACGAAGGTCCAGCAGGCGGCGAGCTCCATCAGCCACTCGCCGGTCTTGCCGAGCAGCAGCTTGCGATGCAGCATCCGGTCGACCTGCATGAAGCGGTTCTCGACGCTCAGCGTGCCGAG
    +
    >AAABFBBBFBBGGGGGGGGGGGGHGGGGGHHHHGGGGGHHHHGHHHHGGGGGGGGGHHHHHHHHHHHHHGGGGGGGGHHHHGGGGGHHHHHHHHHGGHGGHHHHHHHGGGGGGGGGHHHHHHHHHGGGGGGGGGGGGGGGGGGFFFFFFF
    ....

In this file, reads that were assigned to a sample have been labeled with the sample and an index starting with 1. For example the first read in the dataset comes from sample S11 and so gets labeled as S11_1. The second read did not map to a sample and therefore was not renamed.

So...what are the phylosift command-line options and why do we need them?

* `--output=platypi` is giving a base name for the output file.
* `--sample-map=samples.csv` indicates where the sample map file is found
* `--sample-map=barcodes.csv` indicates where the barcode table can be found
* `--rev-barcode=2` tells phylosift that barcode 2 is actually read in the reverse complement direction relative to how it was given in the table. This is a common issue for the i7 Illumina adapter oligos, wherein the strand that is sequenced is complementary to the strand synthesized when ordering the adapters. 
* `--swap-barcodes` tells phylosift that the sample map has the barcode pair swapped relative to the order they are read on the instrument
* `--disable_updates` indicates that phylosift should skip looking for updates to its marker gene database on the server

The very last argument `.` simply tells phylosift to look in the current directory for Illumina files. If your Illumina data is elsewhere then this argument can be replaced with the corresponding filesystem path.

## Other useful options for demultiplexing

The above command produces a single interleaved FastQ file with reads labeled according to sample ID.
While this is an ideal format for certain analyses, such as microbial community profiling with QIIME, for other analyses it is preferable to get each sample stored in a separate file. The following options are relevant:

* `--samplefiles` separate the samples into individual files
* `--no-interleaving` create separate files for the forward and reverse reads from paired-end sequencing
* `--flash` merge overlapping read pairs with the [FLASH software](http://ccb.jhu.edu/software/FLASH/). FLASH must be installed separately. This is useful for amplicon sequencing where the insert is known to be shorter than the sum of paired-end read lengths.


