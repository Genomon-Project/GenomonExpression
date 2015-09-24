#! /usr/bin/env bash


wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/refGene.txt.gz

echo "python proc_ref_exon.py refGene.txt.gz | sort -k1,1 -k2,2n -k3,3n - > exon.bed"
python proc_ref_exon.py refGene.txt.gz | sort -k1,1 -k2,2n -k3,3n - > exon.bed


