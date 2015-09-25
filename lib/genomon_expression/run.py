#! /usr/bin/env python

import os
import subprocess
import utils

def main(args):

    input_bam = args.bam_file
    output_prefix = args.output_prefix
    exon_bed = args.exon_bed
    bedtools_path = args.bedtools_path
    mapq_thres = args.q

    output_prefix_dir = os.path.dirname(output_prefix)
    if output_prefix_dir != "" and not os.path.exists(output_prefix_dir):
       os.makedirs(output_prefix_dir)

    utils.filterImproper(input_bam, output_prefix + ".filt.bam", mapq_thres)

    hOUT = open(output_prefix + ".filt.bed12", 'w')
    subprocess.call([bedtools_path + "/bedtools", "bamtobed", "-bed12", "-i", output_prefix + ".filt.bam"], stdout = hOUT)
    hOUT.close()
 
    hOUT = open(output_prefix + ".exon.bed", 'w')
    subprocess.call([bedtools_path + "/bedtools", "intersect", "-a", output_prefix + ".filt.bed12",
                     "-b", exon_bed, "-wao", "-bed", "-split"], stdout = hOUT)
    hOUT.close()
    

    utils.exon_base_count(output_prefix + ".exon.bed", output_prefix + ".exon2base.txt")

    utils.mapped_base_count(output_prefix + ".filt.bed12", output_prefix + ".mapped_base_count.txt")

    utils.ref_base_count(output_prefix + ".exon2base.txt", output_prefix + ".ref2base.txt")

    utils.sym_base_count(output_prefix + ".ref2base.txt", output_prefix + ".sym2base.txt")

    utils.sym_fkpm(output_prefix + ".sym2base.txt", output_prefix + ".sym2fkpm.txt", output_prefix + ".mapped_base_count.txt")

    subprocess.call(["rm", "-rf", output_prefix + ".filt.bam"])
    subprocess.call(["rm", "-rf", output_prefix + ".filt.bed12"])
    subprocess.call(["rm", "-rf", output_prefix + ".exon.bed"])
    subprocess.call(["rm", "-rf", output_prefix + ".exon2base.txt"])
