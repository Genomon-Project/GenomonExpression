#! /usr/bin/env python

from run import *
import argparse

def create_parser():

    parser = argparse.ArgumentParser(prog = "genomon_expression")

    parser.add_argument("--version", action = "version", version = "genomon_expression-0.4.0")

    parser.add_argument("bam_file", metavar = "sequence.bam", default = None, type = str,
                        help = "the path to the bam file")

    parser.add_argument("output_prefix", metavar = "output_prefix", default = None, type = str, 
                        help = "the prefix of the output")

    parser.add_argument("--grc", default = False, action = 'store_true',
                        help = "convert chromosome names to Genome Reference Consortium nomenclature (default: %(default)s)")

    parser.add_argument("--genome_id", choices = ["hg19", "hg38", "mm10"], default = "hg19",
                        help = "the genome id used for selecting UCSC-GRC chromosome name corresponding files (default: %(default)s)")

    parser.add_argument("-q", metavar = "mapping_qual_thres", default='20', type=int,
                        help = "threshold for mapping quality for calculating base counts")

    parser.add_argument("--keep_improper_pair", action = 'store_true', default = False,
                        help = "keep improper paired reads (activate for single end reads)")

    parser.add_argument("--debug", default = False, action = 'store_true', help = "keep intermediate files")

    return parser


