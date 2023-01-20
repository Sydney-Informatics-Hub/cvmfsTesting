cvmfs_path=/cvmfs/data.biocommons.aarnet.edu.au/Final_resources_250722

nextflow run $cvmfs_path/nfcore_pipeline/rnaseq/ \
                --input samplesheet.csv \
                -profile singularity \
                --fasta $cvmfs_path/Mouse_chr18_reference/chr18.fa \
                --gtf $cvmfs_path/Mouse_chr18_reference/chr_18_startOfLine.gtf \
                --star_index $cvmfs_path/Mouse_chr18_reference/chr18_STAR_singularity_index/ \
                --outdir results \
                -with-report excecution_report.html \
                -with-timeline timeline_report.html \
                -with-dag flowchart.png