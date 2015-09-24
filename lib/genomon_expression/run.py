#! /usr/bin/env python

import os
import subprocess
import utils

def main(args):

    input_bam = args.bam_file
    output = args.output
    exon_bed = args.exon_bed
    bedtools_path = args.bedtools_path
    mapq_thres = args.q

    output_dir = os.path.dirname(output)
    if not os.path.exists(output_dir):
       os.makedirs(output_dir)

    utils.filterImproper(input_bam, output + ".filt.bam", mapq_thres)

    hOUT = open(output + ".filt.bed12", 'w')
    subprocess.call([bedtools_path + "/bedtools", "bamtobed", "-bed12", "-i", output + ".filt.bam"], stdout = hOUT)
    hOUT.close()
 
    hOUT = open(output + ".exon.bed", 'w')
    subprocess.call([bedtools_path + "/bedtools", "intersect", "-a", output + ".filt.bed12",
                     "-b", exon_bed, "-wao", "-bed", "-split"], stdout = hOUT)
    hOUT.close()

    utils.exon_base_count(output + ".exon.bed", output + ".exon2base.txt")

