#! /usr/bin/env bash

rm -rf GCF_000001405.13.assembly.txt
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/ASSEMBLY_REPORTS/All/GCF_000001405.13.assembly.txt

rm -rf refGene.txt.gz
echo "wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/refGene.txt.gz"
wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/refGene.txt.gz

echo "python proc_ref_exon.py refGene.txt.gz | sort -k1,1 -k2,2n -k3,3n - > exon.hg19.bed"
python proc_ref_exon.py refGene.txt.gz | sort -k1,1 -k2,2n -k3,3n - > exon.hg19.bed

echo "python proc_ref_exon.GRCh37.py refGene.txt.gz GCF_000001405.13.assembly.txt | sort -k1,1 -k2,2n -k3,3n - > exon.GRCh37.bed"
python proc_ref_exon.GRCh37.py refGene.txt.gz GCF_000001405.13.assembly.txt | sort -k1,1 -k2,2n -k3,3n - > exon.GRCh37.bed

