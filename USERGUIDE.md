# User guide: end user/researcher

Notes/summary for user guide documentation development. 

## What repositories are available and what is in them?

Currently, can access the following repositories via CVMFS:
```
ls /cvmfs/containers.pawsey.org.au
ls /cvmfs/containers.biocommons.aarnet.edu.au
ls /cvmfs/data.biocommons.aarnet.edu.au
ls /cvmfs/tools.biocommons.aarnet.edu.au
ls /cvmfs/data.galaxyproject.org
ls /cvmfs/main.galaxyproject.org
ls /cvmfs/cvmfs-config.galaxyproject.org
```

### **containers.pawsey.org.au**

This repository had to be cached 

1. Made key directory
```
sudo mkdir /etc/cvmfs/keys/containers.pawsey.org.au
```

2. Copy key from CVMFS repo
```
sudo cp containers.pawsey.org.au.pub /etc/cvmfs/keys/containers.pawsey.org.au/containers.pawsey.org.au.pub
```

3. Create config file for repo
```
sudo nano /etc/cvmfs/config.d/containers.pawsey.org.au.conf
```
Pasted in the following:
```
CVMFS_SERVER_URL="http://bcws.test.aarnet.edu.au/cvmfs/@fqrn@"
CVMFS_PUBLIC_KEY="/etc/cvmfs/keys/containers.pawsey.org.au/containers.pawsey.org.au.pub"
```

4. Could not view contents with
```
ls /cvmfs/containers.pawsey.org.au
```

### **main.galaxyproject.org**

This repository had to be cached 

1. Made key directory
```
sudo mkdir /etc/cvmfs/keys/main.galaxyproject.org
```

2. Copy key from CVMFS repo
```
sudo cp main.galaxyproject.org.pub /etc/cvmfs/keys/main.galaxyproject.org/main.galaxyproject.org.pub
```

3. Create config file for repo
```
sudo nano /etc/cvmfs/config.d/main.galaxyproject.org.conf
```
Pasted in the following:
```
CVMFS_SERVER_URL="http://bcws.test.aarnet.edu.au/cvmfs/@fqrn@"
CVMFS_PUBLIC_KEY="/etc/cvmfs/keys/main.galaxyproject.org/main.galaxyproject.org.pub"
```

4. Could not view contents with 
```
ls /cvmfs/main.galaxyproject.org
```

### **data.galaxyproject.org**

[This repository](https://galaxyproject.org/admin/reference-data-repo/) houses containers reference data provided by Galaxy. The data cache can be browsed via HTTP [here](http://datacache.galaxyproject.org/) and was available without needing to reconfigure cvmfs installation. 

```
ls /cvmfs/data.galaxyproject.org
```

Gives two primary directories: 

* `/managed`: organised with Galaxy's data managers by index format and then by genome build
* `/byhand`: generated prior to use of Galaxy's data managers, organised by genome build and then index format 

```
ll /cvmfs/data.galaxyproject.org/managed/
```
```
total 82
drwxr-xr-x 18 cvmfs cvmfs 4096 Nov 24  2020 ./
drwxr-xr-x  4 cvmfs cvmfs 4096 Mar 31  2016 ../
drwxr-xr-x  3 cvmfs cvmfs 4096 Jul 20  2020 align/
drwxr-xr-x  2 cvmfs cvmfs 4096 Aug 27  2021 bin/
drwxr-xr-x 37 cvmfs cvmfs 4096 Mar 31  2016 bowtie2_index/
drwxr-xr-x 48 cvmfs cvmfs 4096 Mar 30  2016 bwa_mem_index/
lrwxrwxrwx  1 cvmfs cvmfs    1 Jul 10  2020 hg19 -> ./
drwxr-xr-x 60 cvmfs cvmfs 4096 Apr  6  2022 hisat2_index/
drwxr-xr-x 20 cvmfs cvmfs 4096 Dec  9 16:25 kraken2_databases/
drwxr-xr-x  5 cvmfs cvmfs 4096 Oct 24  2018 kraken_database/
drwxr-xr-x  3 cvmfs cvmfs 4096 May 18  2018 len/
drwxr-xr-x  2 cvmfs cvmfs 4096 Dec  9 16:34 location/
drwxr-xr-x  3 cvmfs cvmfs 4096 Oct 24  2018 ncbi_taxonomy/
drwxr-xr-x 21 cvmfs cvmfs 4096 Mar 29  2016 picard_index/
drwxr-xr-x  3 cvmfs cvmfs 4096 Feb 15  2018 plant_tribes/
drwxr-xr-x  3 cvmfs cvmfs 4096 Aug 11  2020 rnastar/
drwxr-xr-x 16 cvmfs cvmfs 4096 May 19  2018 rnastar_index2/
drwxr-xr-x 22 cvmfs cvmfs 4096 Mar 29  2016 sam_indexes/
drwxr-xr-x  2 cvmfs cvmfs 4096 Mar 29  2016 seq/
```

```
ll /cvmfs/data.galaxyproject.org/byhand/
```
```
total 948
drwxr-xr-x 210 cvmfs cvmfs 4096 Apr 21  2022 ./
drwxr-xr-x   4 cvmfs cvmfs 4096 Mar 31  2016 ../
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 AaegL1/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 AgamP3/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 Arabidopsis_thaliana_TAIR10/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 Arabidopsis_thaliana_TAIR9/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 Araly1/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 Bombyx_mori_p50T_2.0/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr  6  2022 CHM13_T2T_v2.0/
drwxr-xr-x   7 cvmfs cvmfs 4096 Apr 22  2016 CpipJ1/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 Homo_sapiens_AK1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 Homo_sapiens_nuHg19_mtrCRS/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 Hydra_JCVI/
drwxr-xr-x   7 cvmfs cvmfs 4096 Apr 22  2016 IscaW1/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 PhumU1/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 Ptrichocarpa_156/
drwxr-xr-x   3 cvmfs cvmfs 4096 Apr 22  2016 Saccharomyces_cerevisiae_S288C_SGD2010/
drwxr-xr-x   7 cvmfs cvmfs 4096 Apr 22  2016 Schizosaccharomyces_pombe_1.1/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 Spur_v2.6/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 Sscrofa9.58/
drwxr-xr-x   6 cvmfs cvmfs 4096 Apr 22  2016 Tcacao_1.0/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 Tcas_3.0/
drwxr-xr-x   7 cvmfs cvmfs 4096 Apr 22  2016 Zea_mays_B73_RefGen_v2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 ailMel1/
drwxr-xr-x  11 cvmfs cvmfs 4096 Apr 21  2022 annotation_profiler/
drwxr-xr-x  11 cvmfs cvmfs 4096 Apr 22  2016 anoCar1/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 anoCar2/
drwxr-xr-x  12 cvmfs cvmfs 4096 Apr 22  2016 anoGam1/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 apiMel1/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 apiMel2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 apiMel3/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 aplCal1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Feb 16  2021 blastdb/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 borEut13/
drwxrwxr-x   3 cvmfs cvmfs 4096 Apr 22  2016 bosTau1/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 bosTau2/
drwxr-xr-x  11 cvmfs cvmfs 4096 Apr 22  2016 bosTau3/
drwxr-xr-x  11 cvmfs cvmfs 4096 Apr 22  2016 bosTau4/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 bosTau5/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 bosTau6/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 bosTau7/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 bosTauMd3/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 braFlo1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 caeJap1/
drwxrwxr-x   9 cvmfs cvmfs 4096 Apr 22  2016 caeJap2/
drwxrwxr-x   9 cvmfs cvmfs 4096 Apr 22  2016 caeJap3/
drwxrwxr-x   9 cvmfs cvmfs 4096 Apr 22  2016 caeJap4/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 caePb1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 caePb2/
drwxrwxr-x   9 cvmfs cvmfs 4096 Apr 22  2016 caePb3/
drwxrwxr-x   8 cvmfs cvmfs 4096 Apr 22  2016 caeRem1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 caeRem2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 caeRem3/
drwxrwxr-x   8 cvmfs cvmfs 4096 Apr 22  2016 caeRem4/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 calJac1/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 calJac3/
drwxr-xr-x  11 cvmfs cvmfs 4096 Apr 22  2016 canFam1/
drwxr-xr-x  12 cvmfs cvmfs 4096 Apr 22  2016 canFam2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 canFam3/
drwxrwxr-x   3 cvmfs cvmfs 4096 Apr 22  2016 cavPor2/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 cavPor3/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 cb3/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 ce10/
drwxr-xr-x  12 cvmfs cvmfs 4096 Apr 22  2016 ce2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 ce3/
drwxr-xr-x  13 cvmfs cvmfs 4096 Apr 22  2016 ce4/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 ce5/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 ce6/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 ce7/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 ce8/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 ce9/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 choHof1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 chrPic1/
drwxr-xr-x   7 cvmfs cvmfs 4096 Apr 22  2016 ci2/
drwxrwxr-x   3 cvmfs cvmfs 4096 Feb 14  2021 customProDB/
drwxrwxr-x   3 cvmfs cvmfs 4096 Apr 22  2016 danRer1/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 danRer2/
drwxr-xr-x   7 cvmfs cvmfs 4096 Apr 22  2016 danRer3/
drwxr-xr-x   6 cvmfs cvmfs 4096 Apr 22  2016 danRer4/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 danRer5/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 danRer6/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 danRer7/
drwxr-xr-x   7 cvmfs cvmfs 4096 Apr 22  2016 dasNov1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 dipOrd1/
drwxr-xr-x   7 cvmfs cvmfs 4096 Apr 22  2016 dm2/
drwxr-xr-x  12 cvmfs cvmfs 4096 Apr 22  2016 dm3/
drwxr-sr-x   2 cvmfs cvmfs 4096 Apr 22  2016 dm4/
drwxr-xr-x   7 cvmfs cvmfs 4096 Apr 22  2016 dp3/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 dp4/
drwxr-xr-x   4 cvmfs cvmfs 4096 Apr 22  2016 droAna1/
drwxr-xr-x   4 cvmfs cvmfs 4096 Apr 22  2016 droAna2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 droAna3/
drwxr-xr-x   5 cvmfs cvmfs 4096 Apr 22  2016 droEre1/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 droEre2/
drwxr-xr-x   5 cvmfs cvmfs 4096 Apr 22  2016 droGri1/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 droGri2/
drwxr-xr-x   6 cvmfs cvmfs 4096 Apr 22  2016 droMoj1/
drwxr-xr-x   5 cvmfs cvmfs 4096 Apr 22  2016 droMoj2/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 droMoj3/
drwxr-xr-x  11 cvmfs cvmfs 4096 Apr 22  2016 droPer1/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 droSec1/
drwxr-xr-x  12 cvmfs cvmfs 4096 Apr 22  2016 droSim1/
drwxr-xr-x   6 cvmfs cvmfs 4096 Apr 22  2016 droVir1/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 droVir2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 droVir3/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 droWil1/
drwxr-xr-x   6 cvmfs cvmfs 4096 Apr 22  2016 droYak1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 droYak2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 echTel1/
drwxr-xr-x  12 cvmfs cvmfs 4096 Apr 22  2016 equCab1/
drwxr-xr-x  12 cvmfs cvmfs 4096 Apr 22  2016 equCab2/
drwxr-xr-x   5 cvmfs cvmfs 4096 Apr 22  2016 equCab2_chrM/
drwxr-xr-x   5 cvmfs cvmfs 4096 Apr 22  2016 eriEur1/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 felCat3/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 felCat4/
drwxrwxr-x   9 cvmfs cvmfs 4096 Apr 22  2016 felCat5/
drwxr-xr-x   6 cvmfs cvmfs 4096 Apr 22  2016 fr1/
drwxr-xr-x   7 cvmfs cvmfs 4096 Apr 22  2016 fr2/
drwxr-xr-x   6 cvmfs cvmfs 4096 Apr 22  2016 fr3/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 galGal2/
drwxr-xr-x  12 cvmfs cvmfs 4096 Apr 22  2016 galGal3/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 galGal4/
drwxr-xr-x  12 cvmfs cvmfs 4096 Apr 22  2016 gasAcu1/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 geoFor1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 gorGor3/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 hetGla1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 hetGla2/
drwxr-xr-x   6 cvmfs cvmfs 4096 Apr 22  2016 hg16/
drwxr-xr-x   7 cvmfs cvmfs 4096 Apr 22  2016 hg17/
drwxr-sr-x  17 cvmfs cvmfs 4096 Apr 22  2016 hg18/
drwxr-sr-x  19 cvmfs cvmfs 4096 Apr 22  2016 hg19/
drwxrwxr-x   2 cvmfs cvmfs 4096 Apr 22  2016 hg20/
drwxrwxr-x  10 cvmfs cvmfs 4096 Apr 22  2016 hg38/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 hg_g1k_v37/
drwxr-xr-x   2 cvmfs cvmfs 4096 Apr 22  2016 jacJac1/
drwxr-xr-x   3 cvmfs cvmfs 4096 Apr 22  2016 lMaj5/
drwxr-xr-x   2 cvmfs cvmfs 4096 Apr 22  2016 lengths/
drwxr-xr-x   2 cvmfs cvmfs 4096 Apr  6  2022 location/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 loxAfr1/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 loxAfr3/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 melGal1/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 melUnd1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 micMur1/
drwxr-xr-x 672 cvmfs cvmfs 4096 Apr 22  2016 microbes/
drwxr-xr-x  11 cvmfs cvmfs 4096 Apr 22  2016 mm10/
drwxrwxr-x   2 cvmfs cvmfs 4096 Apr 22  2016 mm2/
drwxrwxr-x   2 cvmfs cvmfs 4096 Apr 22  2016 mm3/
drwxrwxr-x   2 cvmfs cvmfs 4096 Apr 22  2016 mm4/
drwxr-xr-x   6 cvmfs cvmfs 4096 Apr 22  2016 mm5/
drwxr-xr-x   6 cvmfs cvmfs 4096 Apr 22  2016 mm6/
drwxr-xr-x   6 cvmfs cvmfs 4096 Apr 22  2016 mm7/
drwxr-sr-x  12 cvmfs cvmfs 4096 Apr 22  2016 mm8/
drwxr-sr-x  15 cvmfs cvmfs 4096 Apr 22  2016 mm9/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 monDom1/
drwxr-xr-x   3 cvmfs cvmfs 4096 Apr 22  2016 monDom2/
drwxr-xr-x  11 cvmfs cvmfs 4096 Apr 22  2016 monDom4/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 monDom5/
lrwxrwxrwx   1 cvmfs cvmfs    4 May 16  2014 musMus10 -> mm10/
lrwxrwxrwx   1 cvmfs cvmfs    3 May 16  2014 musMus5 -> mm5/
lrwxrwxrwx   1 cvmfs cvmfs    3 May 16  2014 musMus6 -> mm6/
lrwxrwxrwx   1 cvmfs cvmfs    3 May 16  2014 musMus7 -> mm7/
lrwxrwxrwx   1 cvmfs cvmfs    3 May 16  2014 musMus8 -> mm8/
lrwxrwxrwx   1 cvmfs cvmfs    3 May 16  2014 musMus9 -> mm9/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 myoLuc2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 nomLeu1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 nomLeu2/
drwxr-xr-x   3 cvmfs cvmfs 4096 Apr 22  2016 nomLeu3/
drwxr-xr-x  11 cvmfs cvmfs 4096 Apr 22  2016 ornAna1/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 oryCun1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 oryCun2/
drwxr-xr-x   6 cvmfs cvmfs 4096 Apr 22  2016 oryLat1/
drwxr-xr-x  11 cvmfs cvmfs 4096 Apr 22  2016 oryLat2/
drwxr-xr-x   7 cvmfs cvmfs 4096 Apr 22  2016 oryza_sativa_japonica_nipponbare_IRGSP4.0/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 otoGar1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 otoGar3/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 oviAri1/
drwxr-xr-x   3 cvmfs cvmfs 4096 Apr 22  2016 pUC18/
drwxr-xr-x  11 cvmfs cvmfs 4096 Apr 22  2016 panTro1/
drwxr-xr-x  11 cvmfs cvmfs 4096 Apr 22  2016 panTro2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 panTro3/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 panTro4/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 papHam1/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 petMar1/
drwxr-xr-x  13 cvmfs cvmfs 4096 Apr 22  2016 phiX/
drwxr-xr-x  13 cvmfs cvmfs 4096 Apr 22  2016 ponAbe2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 priPac1/
drwxr-sr-x   2 cvmfs cvmfs 4096 Apr 22  2016 regions/
drwxrwxr-x   3 cvmfs cvmfs 4096 Apr 22  2016 rheMac1/
drwxr-xr-x  12 cvmfs cvmfs 4096 Apr 22  2016 rheMac2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 rheMac3/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 rn3/
drwxr-xr-x  12 cvmfs cvmfs 4096 Apr 22  2016 rn4/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 rn5/
drwxr-xr-x   7 cvmfs cvmfs 4096 Apr 22  2016 sacCer1/
drwxr-xr-x  12 cvmfs cvmfs 4096 Apr 22  2016 sacCer2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 sacCer3/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 saiBol1/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 sarHar1/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 sorAra1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 speTri2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 strPur2/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 strPur3/
drwxrwxr-x   9 cvmfs cvmfs 4096 Apr 22  2016 susScr1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 susScr2/
drwxr-xr-x  13 cvmfs cvmfs 4096 Apr 22  2016 susScr3/
drwxr-xr-x  15 cvmfs cvmfs 4096 Apr 22  2016 taeGut1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 tarSyr1/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 tetNig1/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 tetNig2/
drwxr-xr-x   8 cvmfs cvmfs 4096 Apr 22  2016 triCas2/
drwxr-xr-x  10 cvmfs cvmfs 4096 Apr 22  2016 tupBel1/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 turTru2/
drwxr-xr-x   7 cvmfs cvmfs 4096 Apr 22  2016 venter1/
drwxrwxr-x   9 cvmfs cvmfs 4096 Apr 22  2016 xenTro1/
drwxr-sr-x  10 cvmfs cvmfs 4096 Apr 22  2016 xenTro2/
drwxr-xr-x   9 cvmfs cvmfs 4096 Apr 22  2016 xenTro3/
```


### **containers.biocommons.aarnet.edu.au**

This repository only houses containers run by the nf-core/rnaseq pipeline, used in the 2022 rnaseq workshop. Reconfigured install for access, before viewing (see README.md).

<details>
<summary>

```
tree /cvmfs/containers.biocommons.aarnet.edu.au
```

</summary>

```
/cvmfs/containers.biocommons.aarnet.edu.au
├── I
│   └── A
│       └── IARCbioinfo-alignment-nf-v1.3.img
├── b
│   ├── b
│   │   └── bbmap-38.93--he522d1c_0.img
│   ├── e
│   │   └── bedtools-2.30.0--hc088bd4_0.img
│   └── i
│       ├── bioconductor-biostrings-2.58.0--r40h037d062_0.img
│       ├── bioconductor-dada2-1.20.0--r41h399db7b_0.img
│       ├── bioconductor-dupradar-1.18.0--r40_1.img
│       ├── bioconductor-summarizedexperiment-1.20.0--r40_0.img
│       └── bioconductor-tximeta-1.8.0--r40_0.img
├── c
│   ├── o
│   │   └── containers.biocontainers.pro-s3-SingImgsRepo-biocontainers-v1.2.0_cv1-biocontainers_v1.2.0_cv1.img.img
│   └── u
│       └── cutadapt-3.2--py38h0213d0e_0.img
├── f
│   └── a
│       └── fastqc-0.11.9--0.img
├── m
│   └── u
│       ├── mulled-v2-1fa26d1ce03c295fe2fdcf85831a92fbcbd7e8c2-afaaa4c6f5b308b4b6aa2dd8e99e1466b2a6b0cd-0.img
│       ├── mulled-v2-8849acf39a43cdd6c839a369a74c0adc823e2f91-ab110436faf952a33575c64dd74615a84011450b-0.img
│       ├── mulled-v2-cf0123ef83b3c38c13e3b0696a3f285d3f20f15b-606b713ec440e799d53a2b51a6e79dbfd28ecf3e-0.img
│       ├── mulled-v2-cf0123ef83b3c38c13e3b0696a3f285d3f20f15b-64aad4a4e144878400649e71f42105311be7ed87-0.img.pulling.1651622650896
│       ├── multiqc-1.10.1--py_0.img
│       ├── multiqc-1.10.1--pyhdfd78af_1.img
│       └── multiqc-1.11--pyhdfd78af_0.img
├── n
│   └── f
│       └── nfcore-sarek-2.7.1.img
├── p
│   ├── a
│   │   └── pandas-1.1.5.img
│   ├── e
│   │   └── perl-5.26.2.img
│   ├── i
│   │   ├── picard-2.25.7--hdfd78af_0.img
│   │   └── picard-2.26.7--hdfd78af_0.img
│   ├── r
│   │   └── preseq-3.1.2--h06ef8b0_1.img
│   └── y
│       ├── python-3.8.3.img
│       └── python-3.9--1.img
├── q
│   └── u
│       ├── qualimap-2.2.2d--1.img
│       └── quay.io-qiime2-core-2021.2.img
├── r
│   ├── -
│   │   └── r-tidyverse-1.2.1.img
│   ├── n
│   │   ├── rnaseq_4.1.0.sif
│   │   └── rnaseq_rstudio.sif
│   └── s
│       ├── rseqc-3.0.1--py37h516909a_1.img
│       └── rstudio_4.1.0_V4.0.sif
├── s
│   ├── a
│   │   ├── salmon-1.5.2--h84f40af_0.img
│   │   ├── samtools-1.10--h9402c20_2.img
│   │   ├── samtools-1.13--h8c37831_0.img
│   │   ├── samtools-1.14--hb421002_0.img
│   │   └── samtools-1.15.1--h1170115_0.img
│   ├── t
│   │   ├── star-2.6.1d--0.img
│   │   └── stringtie-2.1.7--h978d192_0.img
│   └── u
│       └── subread-2.0.1--hed695b0_0.img
├── t
│   └── r
│       └── trim-galore-0.6.7--hdfd78af_0.img
└── u
    └── c
        ├── ucsc-bedclip-377--h0b8a92a_2.img
        └── ucsc-bedgraphtobigwig-377--h446ed27_1.img

35 directories, 44 files
```

</details>

### **data.biocommons.aarnet.edu.au**

This repository only houses code for the nf-core/rnaseq pipeline and materials used in the 2022 rnaseq workshop.

<details>
<summary>

```
tree /cvmfs/data.biocommons.aarnet.edu.au
```

</summary>

```
/cvmfs/data.biocommons.aarnet.edu.au
└── Final_resources_250722
    ├── Mouse_chr18_reference
    │   ├── chr18.fa
    │   ├── chr18_STAR_singularity_index
    │   │   ├── Genome
    │   │   ├── SA
    │   │   ├── SAindex
    │   │   ├── chrLength.txt
    │   │   ├── chrName.txt
    │   │   ├── chrNameLength.txt
    │   │   ├── chrStart.txt
    │   │   ├── exonGeTrInfo.tab
    │   │   ├── exonInfo.tab
    │   │   ├── geneInfo.tab
    │   │   ├── genomeParameters.txt
    │   │   ├── sjdbInfo.txt
    │   │   ├── sjdbList.fromGTF.out.tab
    │   │   ├── sjdbList.out.tab
    │   │   └── transcriptInfo.tab
    │   └── chr_18_startOfLine.gtf
    ├── Mouse_references
    │   ├── Log.out
    │   ├── Mmus.gtf
    │   ├── STARIndex_sarekGenome
    │   │   ├── Genome
    │   │   ├── SA
    │   │   ├── SAindex
    │   │   ├── chrLength.txt
    │   │   ├── chrName.txt
    │   │   ├── chrNameLength.txt
    │   │   ├── chrStart.txt
    │   │   ├── exonGeTrInfo.tab
    │   │   ├── exonInfo.tab
    │   │   ├── geneInfo.tab
    │   │   ├── genomeParameters.txt
    │   │   ├── sjdbInfo.txt
    │   │   ├── sjdbList.fromGTF.out.tab
    │   │   ├── sjdbList.out.tab
    │   │   └── transcriptInfo.tab
    │   ├── genome
    │   │   ├── README.txt
    │   │   ├── genome_genes.gtf
    │   │   └── rsem
    │   │       ├── genome.chrlist
    │   │       ├── genome.grp
    │   │       ├── genome.idx.fa
    │   │       ├── genome.n2g.idx.fa
    │   │       ├── genome.seq
    │   │       ├── genome.ti
    │   │       └── genome.transcripts.fa
    │   ├── genome.fa
    │   ├── genome.fa.fai
    │   └── genome.fa.sizes
    └── nfcore_pipeline
        └── rnaseq
            ├── CHANGELOG.md
            ├── CITATIONS.md
            ├── CODE_OF_CONDUCT.md
            ├── LICENSE
            ├── README.md
            ├── assets
            │   ├── dummy_file.txt
            │   ├── email_template.html
            │   ├── email_template.txt
            │   ├── multiqc
            │   │   ├── biotypes_header.txt
            │   │   ├── deseq2_clustering_header.txt
            │   │   └── deseq2_pca_header.txt
            │   ├── multiqc_config.yaml
            │   ├── nf-core-rnaseq_logo.png
            │   ├── rrna-db-defaults.txt
            │   ├── samplesheet.csv
            │   ├── schema_input.json
            │   └── sendmail_template.txt
            ├── bin
            │   ├── check_samplesheet.py
            │   ├── deseq2_qc.r
            │   ├── dupradar.r
            │   ├── fasta2gtf.py
            │   ├── fastq_dir_to_samplesheet.py
            │   ├── filter_gtf_for_genes_in_genome.py
            │   ├── gtf2bed
            │   ├── mqc_features_stat.py
            │   ├── salmon_summarizedexperiment.r
            │   ├── salmon_tx2gene.py
            │   └── salmon_tximport.r
            ├── conf
            │   ├── base.config
            │   ├── igenomes.config
            │   ├── modules.config
            │   ├── test.config
            │   └── test_full.config
            ├── docs
            │   ├── README.md
            │   ├── images
            │   │   ├── deseq2_qc_plots.png
            │   │   ├── dupradar_example_plot.png
            │   │   ├── mqc_alignment_check.png
            │   │   ├── mqc_cutadapt_trimmed.png
            │   │   ├── mqc_deseq2_clustering.png
            │   │   ├── mqc_deseq2_pca.png
            │   │   ├── mqc_dupradar.png
            │   │   ├── mqc_fastqc_adapter.png
            │   │   ├── mqc_fastqc_counts.png
            │   │   ├── mqc_fastqc_quality.png
            │   │   ├── mqc_featurecounts_biotype.png
            │   │   ├── mqc_hisat2.png
            │   │   ├── mqc_picard_markduplicates.png
            │   │   ├── mqc_preseq_plot.png
            │   │   ├── mqc_qualimap_coverage.png
            │   │   ├── mqc_qualimap_features.png
            │   │   ├── mqc_rsem_mapped.png
            │   │   ├── mqc_rsem_multimapped.png
            │   │   ├── mqc_rseqc_inferexperiment.png
            │   │   ├── mqc_rseqc_innerdistance.png
            │   │   ├── mqc_rseqc_junctionannotation.png
            │   │   ├── mqc_rseqc_junctionsaturation.png
            │   │   ├── mqc_rseqc_readdistribution.png
            │   │   ├── mqc_rseqc_readduplication.png
            │   │   ├── mqc_salmon.png
            │   │   ├── mqc_samtools_idxstats.png
            │   │   ├── mqc_samtools_mapped.png
            │   │   ├── mqc_sortmerna.png
            │   │   ├── mqc_star.png
            │   │   ├── mqc_strand_check.png
            │   │   ├── nf-core-rnaseq_logo.png
            │   │   └── nfcore-rnaseq_logo.ai
            │   ├── output.md
            │   └── usage.md
            ├── lib
            │   ├── NfcoreSchema.groovy
            │   ├── NfcoreTemplate.groovy
            │   ├── Utils.groovy
            │   ├── WorkflowMain.groovy
            │   ├── WorkflowRnaseq.groovy
            │   └── nfcore_external_java_deps.jar
            ├── main.nf
            ├── modules
            │   ├── local
            │   │   ├── bedtools_genomecov.nf
            │   │   ├── cat_additional_fasta.nf
            │   │   ├── deseq2_qc.nf
            │   │   ├── dupradar.nf
            │   │   ├── functions.nf
            │   │   ├── get_chrom_sizes.nf
            │   │   ├── gtf2bed.nf
            │   │   ├── gtf_gene_filter.nf
            │   │   ├── multiqc.nf
            │   │   ├── multiqc_custom_biotype.nf
            │   │   ├── multiqc_tsv_from_list.nf
            │   │   ├── rsem_merge_counts.nf
            │   │   ├── salmon_merge_counts.nf
            │   │   ├── salmon_summarizedexperiment.nf
            │   │   ├── salmon_tx2gene.nf
            │   │   ├── salmon_tximport.nf
            │   │   ├── samplesheet_check.nf
            │   │   ├── star_align.nf
            │   │   └── star_genomegenerate.nf
            │   └── nf-core
            │       └── modules
            │           ├── bbmap
            │           │   └── bbsplit
            │           │       ├── functions.nf
            │           │       ├── main.nf
            │           │       └── meta.yml
            │           ├── cat
            │           │   └── fastq
            │           │       ├── functions.nf
            │           │       ├── main.nf
            │           │       └── meta.yml
            │           ├── custom
            │           │   └── dumpsoftwareversions
            │           │       ├── functions.nf
            │           │       ├── main.nf
            │           │       └── meta.yml
            │           ├── fastqc
            │           │   ├── functions.nf
            │           │   ├── main.nf
            │           │   └── meta.yml
            │           ├── gffread
            │           │   ├── functions.nf
            │           │   ├── main.nf
            │           │   └── meta.yml
            │           ├── gunzip
            │           │   ├── functions.nf
            │           │   ├── main.nf
            │           │   └── meta.yml
            │           ├── hisat2
            │           │   ├── align
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   ├── build
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   └── extractsplicesites
            │           │       ├── functions.nf
            │           │       ├── main.nf
            │           │       └── meta.yml
            │           ├── picard
            │           │   └── markduplicates
            │           │       ├── functions.nf
            │           │       ├── main.nf
            │           │       └── meta.yml
            │           ├── preseq
            │           │   └── lcextrap
            │           │       ├── functions.nf
            │           │       ├── main.nf
            │           │       └── meta.yml
            │           ├── qualimap
            │           │   └── rnaseq
            │           │       ├── functions.nf
            │           │       └── main.nf
            │           ├── rsem
            │           │   ├── calculateexpression
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   └── preparereference
            │           │       ├── functions.nf
            │           │       ├── main.nf
            │           │       └── meta.yml
            │           ├── rseqc
            │           │   ├── bamstat
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   ├── inferexperiment
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   ├── innerdistance
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   ├── junctionannotation
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   ├── junctionsaturation
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   ├── readdistribution
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   └── readduplication
            │           │       ├── functions.nf
            │           │       ├── main.nf
            │           │       └── meta.yml
            │           ├── salmon
            │           │   ├── index
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   └── quant
            │           │       ├── functions.nf
            │           │       ├── main.nf
            │           │       └── meta.yml
            │           ├── samtools
            │           │   ├── flagstat
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   ├── idxstats
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   ├── index
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   ├── sort
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   └── stats
            │           │       ├── functions.nf
            │           │       ├── main.nf
            │           │       └── meta.yml
            │           ├── sortmerna
            │           │   ├── functions.nf
            │           │   └── main.nf
            │           ├── stringtie
            │           │   └── stringtie
            │           │       ├── functions.nf
            │           │       ├── main.nf
            │           │       └── meta.yml
            │           ├── subread
            │           │   └── featurecounts
            │           │       ├── functions.nf
            │           │       ├── main.nf
            │           │       └── meta.yml
            │           ├── trimgalore
            │           │   ├── functions.nf
            │           │   ├── main.nf
            │           │   └── meta.yml
            │           ├── ucsc
            │           │   ├── bedclip
            │           │   │   ├── functions.nf
            │           │   │   ├── main.nf
            │           │   │   └── meta.yml
            │           │   └── bedgraphtobigwig
            │           │       ├── functions.nf
            │           │       ├── main.nf
            │           │       └── meta.yml
            │           ├── umitools
            │           │   ├── dedup
            │           │   │   ├── functions.nf
            │           │   │   └── main.nf
            │           │   └── extract
            │           │       ├── functions.nf
            │           │       └── main.nf
            │           └── untar
            │               ├── functions.nf
            │               ├── main.nf
            │               └── meta.yml
            ├── modules.json
            ├── nextflow.config
            ├── nextflow_schema.json
            ├── subworkflows
            │   ├── local
            │   │   ├── align_star.nf
            │   │   ├── input_check.nf
            │   │   ├── prepare_genome.nf
            │   │   ├── quantify_rsem.nf
            │   │   └── quantify_salmon.nf
            │   └── nf-core
            │       ├── align_hisat2.nf
            │       ├── bam_sort_samtools.nf
            │       ├── bam_stats_samtools.nf
            │       ├── bedgraph_to_bigwig.nf
            │       ├── dedup_umi_umitools.nf
            │       ├── fastqc_umitools_trimgalore.nf
            │       ├── mark_duplicates_picard.nf
            │       └── rseqc.nf
            └── workflows
                └── rnaseq.nf

76 directories, 264 files
```
</details>

### **tools.biocommons.aarnet.edu.au**

This repository contains subset fastq files used in the 2022 rnaseq workshop

<details>
<summary>

```
tree /cvmfs/tools.biocommons.aarnet.edu.au
```

</summary>

```

```
</details>
