#! /usr/bin/env python

import os
import subprocess
import utils
import annot_utils.exon


def main(args):

    input_bam = args.bam_file
    output_prefix = args.output_prefix
    # exon_bed = args.exon_bed
    # bedtools_path = args.bedtools_path
    mapq_thres = args.q
    keep_improper_pair = args.keep_improper_pair

    output_prefix_dir = os.path.dirname(output_prefix)
    if output_prefix_dir != "" and not os.path.exists(output_prefix_dir):
       os.makedirs(output_prefix_dir)

    annot_utils.exon.make_exon_info(output_prefix + ".refExon.bed.gz", "refseq", args.genome_id, args.grc, True)
    
    utils.filterImproper(input_bam, output_prefix + ".filt.bam", mapq_thres, keep_improper_pair)

    hout = open(output_prefix + ".exon.bed", 'w')
    subprocess.call(["bedtools", "intersect", "-abam", output_prefix + ".filt.bam",
                     "-b", output_prefix + ".refExon.bed.gz", "-wao", "-bed", "-split"], stdout = hout)
    hout.close()                
 
    utils.exon_base_count(output_prefix + ".exon.bed", output_prefix + ".exon2base.txt")

    utils.mapped_base_count(output_prefix + ".exon.bed", output_prefix + ".mapped_base_count.txt")

    utils.ref_base_count(output_prefix + ".exon2base.txt", output_prefix + ".ref2base.txt", output_prefix + ".refExon.bed.gz")

    utils.sym_base_count(output_prefix + ".ref2base.txt", output_prefix + ".sym2base.txt")

    utils.sym_fkpm(output_prefix + ".sym2base.txt", output_prefix + ".sym2fpkm.txt", output_prefix + ".mapped_base_count.txt")

    if not args.debug:
        subprocess.call(["rm", "-rf", output_prefix + ".refExon.bed.gz"])
        subprocess.call(["rm", "-rf", output_prefix + ".refExon.bed.gz.tbi"])
        subprocess.call(["rm", "-rf", output_prefix + ".filt.bam"])
        subprocess.call(["rm", "-rf", output_prefix + ".filt.bed12"])
        subprocess.call(["rm", "-rf", output_prefix + ".exon.bed"])
        subprocess.call(["rm", "-rf", output_prefix + ".exon2base.txt"])

