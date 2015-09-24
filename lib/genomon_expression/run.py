#! /usr/bin/env python

import os
import subprocess
import utils

def main(args):

    input_bam = args.bam_file
    output = args.output
    bedtools_path = args.bedtools_path

    if not os.path.dirname(output):
       os.makedirs(os.path.dirname(output))
 
    utils.filterImproper(input_bam, output + ".filt.bam", mapq_thres)

    hOUT = open(output + ".filt.bed12", 'w')
    subprocess.call([bedtools_path + "/bedtools", "bamtobed", "-bed12", "-i", output + ".filt.bam"], stdout = hOUT)
    hOUT.close()


