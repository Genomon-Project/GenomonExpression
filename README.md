# GenomonExpression
python script for calculating expression values from RNA-seq

## Introduction

GenomonExpression is a software for simply calculating transcriptome expression values 
from rna sequencing data. The procedure is as follows:

1. Filter inconsistent read pairs (sam format flag 2 is on) and low mapping quality reads (default above 20).
2. For each specified exon, calculate the aligned bases.
3. For each refseq gene, calculate the aligned bases. 
4. For each gene symbol, get the associated refseq genes with maximum mapped bases divided by region size.
5. Derive FKPM value for each gene symbol.

Note that this software is just for obtaining gene symbol bases expression values.
For those who want to get the expression values for each splicing variant, go to cufflinks, kallisto, salmon and so on.

## Dependency

### Python
Python (>= 2.7), `pysam (>= 0.8.1)`

### Software
[bedtools](http://bedtools.readthedocs.org/en/latest/])

## Install

```
git clone https://github.com/Genomon-Project/GenomonExpression.git
cd GenomonExpression
python setup.py build 
python setup.py install 
```

For the last command, you may need to add --user if you are using a shared computing cluster.
```
python setup.py install --user
```


## Preparation

1. Install the bedtools and set the path to it.
2. Prepare annotation file for each refseq gene and exon. The example script getting this is resource/prepGeneInfo.sh.

```
cd resource
bash prepGeneInfo.sh
```

## Commands

```
genomon_expression [-h] [--version] [-q mapping_qual_thres] [--keep_improper_pair] 
                   sequence.bam output_prefix exon.GRCh37.bed
```

You can check the manual by typing
```
genomon_expression -h
```

