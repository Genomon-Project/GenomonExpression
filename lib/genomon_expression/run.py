#! /usr/bin/env python

import os
import subprocess
import utils

def main(args):

    input_bam = args.bam_file
    output = args.output
    bedtools_path = args.bedtools_path
    mapq_thres = args.q

    output_dir = os.path.dirname(output)
    if not os.path.exists(output_dir):
       os.makedirs(output_dir)
 
    utils.filterImproper(input_bam, output + ".filt.bam", mapq_thres)

    """
    hOUT = open(output + ".filt.bed12", 'w')
    subprocess.call([bedtools_path + "/bedtools", "bamtobed", "-bed12", "-i", output + ".filt.bam"], stdout = hOUT)
    hOUT.close()
    """


