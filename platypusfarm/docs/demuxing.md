# Demultiplexing custom sample barcodes with PhyloSift

This tutorial assumes you have a GVL instance running already in the NeCTAR cloud.
See the "Initial setup" page for instructions on how to get that going.
We will further assume that you've logged in to the instance with ssh.

## Obtain the latest PhyloSift

     curl -O http://ehdar.genomecenter.ucdavis.edu/phylosift/release/phylosift_20141105.tar.gz
     tar -xzf phylosift_20141105.tar.gz
     export PATH="$PATH:`pwd`/phylosift_20141105/bin"

The first command downloads PhyloSift using curl, the second command unzips it, and the third command adds it to your executable binary program path.

## Obtain the example data
    
    curl -O http://darlinglab.org/data/Unassigned*.gz

The above command uses curl to download an Illumina dataset produced on the UTS MiSeq.


