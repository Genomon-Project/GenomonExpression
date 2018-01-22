# GenomonExpression

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.org/Genomon-Project/GenomonExpression.svg?branch=devel)](https://travis-ci.org/Genomon-Project/GenomonExpression)

python script for calculating expression values from RNA-seq

## Introduction

GenomonExpression is a software for simply calculating transcriptome expression values 
from rna sequencing data. The procedure is as follows:

1. Filter inconsistent read pairs (sam format flag 2 is on) and low mapping quality reads (default above 20).
2. For each specified exon, calculate the aligned bases.
3. For each refseq gene, calculate the aligned bases. 
4. For each gene symbol, get the associated refseq genes with maximum mapped bases divided by region size.
5. Derive FPKM value for each gene symbol.

Note that this software is just for obtaining gene symbol bases expression values.
For those who want to get the expression values for each splicing variant, go to cufflinks, kallisto, salmon and so on.

## Dependency

### Python
Python (>= 2.7), pysam, [annot_utils](https://github.com/friend1ws/annot_utils)

### Software
[bedtools](http://bedtools.readthedocs.org/en/latest/])

## Install

```
pip install genomon_expression
```

For the last command, you may need to add --user if you are using a shared computing cluster.
```
pip install genomon_expression --user
```


## Preparation

1. Install the bedtools and set the path to it.
2. Install [annot_utils](https://github.com/friend1ws/annot_utils)


## Commands

```
genomon_expression [-h] [--version] [--grc]
                        [--genome_id {hg19,hg38,mm10}]
                        [-q mapping_qual_thres] [--keep_improper_pair]
                        [--debug]
                        sequence.bam output_prefix
```

You can check the manual by typing
```
genomon_expression -h
```

## Results

The primary result is ${output_prefix}.sym2fkpm.txt, in which the first column is the gene symbol and the second column is the FPKM value.
