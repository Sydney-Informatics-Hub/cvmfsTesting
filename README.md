# cvmfsTesting

Documentation for testing unpacked containers on CVMFS on Nimbus for BYOD-CLI project.

## Configure CVMFS 

### **Install cvmfs on Nimbus**

Following [documentation](https://github.com/PawseySC/Pawsey-CernVM-FS). Installed with: 
```bash
git clone https://github.com/PawseySC/Pawsey-CernVM-FS.git
cd Pawsey-CernVM-FS
sudo ./install-cvmfs.sh install
```

Refreshed repositories by re-installing:
```bash
sudo ./install-cvmfs.sh uninstall
sudo ./install-cvmfs.sh install
```

Tested with: 

```bash
ls /cvmfs/singularity.galaxyproject.org
```

### **Reconfigure to access unpacked container repository**

Install did not provide access to aarnet repos, so needed to reconfigure install. 

First, added [pub key for repo](https://github.com/PawseySC/Pawsey-CernVM-FS/blob/main/pubkeys/unpacked.containers.biocommons.aarnet.edu.au.pub) to `/etc/cvmfs/keys/biocommons.aarnet.edu.au/unpacked.containers.biocommons.aarnet.edu.au.pub`. Made key directory for the repo: 
```bash
sudo mkdir /etc/cvmfs/keys/biocommons.aarnet.edu.au/
```
Then copied pub key over: 
```bash
sudo cp pubkeys/unpacked.containers.biocommons.aarnet.edu.au.pub /etc/cvmfs/keys/biocommons.aarnet.edu.au/unpacked.containers.biocommons.aarnet.edu.au.pub
```

Then created config file for the repo and saved the following to `/etc/cvmfs/config.d/unpacked.containers.biocommons.aarnet.edu.au.conf`:
```bash
CVMFS_SERVER_URL="http://bcws.test.aarnet.edu.au/cvmfs/@fqrn@"
CVMFS_PUBLIC_KEY="/etc/cvmfs/keys/biocommons.aarnet.edu.au/unpacked.containers.biocommons.aarnet.edu.au.pub"
```

Tested with:
```bash
ls /cvmfs/unpacked.containers.biocommons.aarnet.edu.au
```

### **Reconfigure to access rnaseq workshop resources**

First, added [pub key for repo](https://github.com/PawseySC/Pawsey-CernVM-FS/blob/main/pubkeys/data.biocommons.aarnet.edu.au.pub) to `/etc/cvmfs/keys/data.biocommons.aarnet.edu.au/data.biocommons.aarnet.edu.au.pub`. Made key directory for the repo: 

```bash
sudo mkdir /etc/cvmfs/keys/data.biocommons.aarnet.edu.au/
```

Then copied pub key over: 
```bash
sudo cp pubkeys/data.biocommons.aarnet.edu.au.pub /etc/cvmfs/keys/data.biocommons.aarnet.edu.au/data.biocommons.aarnet.edu.au.pub
```

Then created config file for the repo and saved the following to `/etc/cvmfs/config.d/data.biocommons.aarnet.edu.au.conf`:
```
CVMFS_SERVER_URL="http://bcws.test.aarnet.edu.au/cvmfs/@fqrn@"
CVMFS_PUBLIC_KEY="/etc/cvmfs/keys/data.biocommons.aarnet.edu.au/data.biocommons.aarnet.edu.au.pub"
```

## Updated paths for unpacked containers 

Data directories of interest: 
```bash
ubuntu@georgie-nimbus:/data/testCVMFS$ find /cvmfs/unpacked.containers.biocommons.aarnet.edu.au/ -mindepth 3 -maxdepth 3 -type d | sort

/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/b/b/bbmap-38.93--he522d1c_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/b/e/bedtools-2.30.0--hc088bd4_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/b/i/bioconductor-biostrings-2.58.0--r40h037d062_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/b/i/bioconductor-dada2-1.20.0--r41h399db7b_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/b/i/bioconductor-dupradar-1.18.0--r40_1
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/b/i/bioconductor-summarizedexperiment-1.20.0--r40_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/b/i/bioconductor-tximeta-1.8.0--r40_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/c/o/containers.biocontainers.pro-s3-SingImgsRepo-biocontainers-v1.2.0_cv1-biocontainers_v1.2.0_cv1.img
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/c/u/cutadapt-3.2--py38h0213d0e_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/f/a/fastqc-0.11.9--0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/I/A/IARCbioinfo-alignment-nf-v1.3
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/m/u/mulled-v2-1fa26d1ce03c295fe2fdcf85831a92fbcbd7e8c2-afaaa4c6f5b308b4b6aa2dd8e99e1466b2a6b0cd-0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/m/u/mulled-v2-8849acf39a43cdd6c839a369a74c0adc823e2f91-ab110436faf952a33575c64dd74615a84011450b-0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/m/u/mulled-v2-cf0123ef83b3c38c13e3b0696a3f285d3f20f15b-606b713ec440e799d53a2b51a6e79dbfd28ecf3e-0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/m/u/multiqc-1.10.1--py_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/m/u/multiqc-1.10.1--pyhdfd78af_1
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/m/u/multiqc-1.11--pyhdfd78af_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/n/f/nfcore-sarek-2.7.1
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/p/a/pandas-1.1.5
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/p/e/perl-5.26.2
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/p/i/picard-2.25.7--hdfd78af_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/p/i/picard-2.26.7--hdfd78af_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/p/r/preseq-3.1.2--h06ef8b0_1
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/p/y/python-3.8.3
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/p/y/python-3.9--1
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/q/u/qualimap-2.2.2d--1
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/q/u/quay.io-qiime2-core-2021.2
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/r/n/rnaseq_4.1.0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/r/n/rnaseq_rstudio
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/r/-/r-tidyverse-1.2.1
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/r/s/rseqc-3.0.1--py37h516909a_1
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/r/s/rstudio_4.1.0_V4.0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/s/a/salmon-1.5.2--h84f40af_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/s/a/samtools-1.10--h9402c20_2
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/s/a/samtools-1.13--h8c37831_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/s/a/samtools-1.14--hb421002_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/s/a/samtools-1.15.1--h1170115_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/s/t/star-2.6.1d--0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/s/t/stringtie-2.1.7--h978d192_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/s/u/subread-2.0.1--hed695b0_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/t/r/trim-galore-0.6.7--hdfd78af_0
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/u/c/ucsc-bedclip-377--h0b8a92a_2
/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/u/c/ucsc-bedgraphtobigwig-377--h446ed27_1
```

## Edited nf-core/rnasq nextflow.config 

Downloaded Nandan's materials from RNAseq 2022 workshop: 
```bash
wget -O working_directory.tar.gz https://cloudstor.aarnet.edu.au/plus/s/xveu7WCIdj7bk6c/download
tar -zxvf working_directory.tar.gz
cd working_directory 
```

Updated `nextflow.config` paths with the following script (run with python3 updateContainerPaths.py)
```python
import re 

containers = {}
with open('working_directory/nextflow.config', 'r') as f:
    for line in f:
        match = re.search(r'container = ([\'"])(.*?)\1', line)
        if match:
            old_path = match.group(2)
            # Add the container path and its new path to the dictionary
            new_path = '/cvmfs/unpacked.containers.biocommons.aarnet.edu.au/' + '/'.join(old_path.split('/')[5:]).rstrip('.img')
            containers[old_path] = new_path

with open('working_directory/nextflow.config', 'r') as f:
    file_str = f.read()

# Replace old paths with new paths
for old_path, new_path in containers.items():
    # Use regex to find and replace the container paths
    file_str = file_str.replace(old_path, new_path)

# Open the fnew config for writing
with open('working_directory/nextflowNew.config', 'w') as f:
    # Write the updated config string
    f.write(file_str)
```

## Rerun nf-core/rnaseq with updated config

Replaced `nextflow.config` file with `nextflowUnpacked.config` in the working_directory and ran the pipeline with: 

```bash
cvmfs_path=/cvmfs/data.biocommons.aarnet.edu.au/Final_resources_250722

nextflow run $cvmfs_path/nfcore_pipeline/rnaseq/ \
                -config nextflowUnpacked.config \
                --input samplesheet.csv \
                -profile singularity \
                --fasta $cvmfs_path/Mouse_chr18_reference/chr18.fa \
                --gtf $cvmfs_path/Mouse_chr18_reference/chr_18_startOfLine.gtf \
                --star_index $cvmfs_path/Mouse_chr18_reference/chr18_STAR_singularity_index/ \
                --outdir results \
                -with-report excecution_report.html \
                -with-timeline timeline_report.html \
                -with-dag flowchart.png
```

Pipeline ran to completion 
```
-[nf-core/rnaseq] Pipeline completed successfully-
Completed at: 09-Feb-2023 06:12:16
Duration    : 4m 39s
CPU hours   : 1.9
Succeeded   : 207
```

## Runtime comparison with packed containers 

Configured the packed containers repository, same as above:

```bash
sudo mkdir /etc/cvmfs/keys/containers.biocommons.aarnet.edu.au
sudo cp pubkeys/containers.biocommons.aarnet.edu.au.pub /etc/cvmfs/keys/containers.biocommons.aarnet.edu.au/containers.biocommons.aarnet.edu.au.pub
```

`/etc/cvmfs/config.d/containers.biocommons.aarnet.edu.au.conf` contained:
```
CVMFS_SERVER_URL="http://bcws.test.aarnet.edu.au/cvmfs/@fqrn@"
CVMFS_PUBLIC_KEY="/etc/cvmfs/keys/containers.biocommons.aarnet.edu.au/containers.biocommons.aarnet.edu.au.pub"
``` 

Reran the pipeline:
```
nextflow run $cvmfs_path/nfcore_pipeline/rnaseq/ \
                -config nextflow.config \
                --input samplesheet.csv \
                -profile singularity \
                --fasta $cvmfs_path/Mouse_chr18_reference/chr18.fa \
                --gtf $cvmfs_path/Mouse_chr18_reference/chr_18_startOfLine.gtf \
                --star_index $cvmfs_path/Mouse_chr18_reference/chr18_STAR_singularity_index/ \
                --outdir results \
                -with-report excecution_report.html \
                -with-timeline timeline_report.html \
                -with-dag flowchart.png
```

```
-[nf-core/rnaseq] Pipeline completed successfully-
Completed at: 20-Jan-2023 05:44:20
Duration    : 4m 34s
CPU hours   : 1.9
Succeeded   : 207
```

TODO: follow up how caching affects runtime differences. First run with unpacked containers was ~7 min, second run 4.5 min. 


## Materials
- [RNAseq workshop materials](https://sydney-informatics-hub.github.io/rna-seq-pt1-quarto/notebooks/1.1_Download_data.html)
- [CVMFS materials](https://github.com/PawseySC/Pawsey-CernVM-FS)
