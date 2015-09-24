#! /usr/bin/env python

import re
import pysam

def filterImproper(input_bam, output_bam, mapq_thres):

    """
    This function is used for filtering short read with improper pairs,
    and low mapping qualities.
    """

    bamfile_in = pysam.AlignmentFile(input_bam, 'rb')
    bamfile_out = pysam.AlignmentFile(output_bam, 'wb', template = bamfile_in)

    for read in bamfile_in.fetch():
    
        # get the flag information
        flags = format(int(read.flag), "#014b")[:1:-1]

        # skip improper read pair
        if flags[1] != "1": continue

        # skip if either of the read pair is unmapped
        if flags[2] == "1" or flags[3] == "1": continue

        # skip supplementary alignment
        if flags[8] == "1" or flags[11] == "1": continue

        # skip duplicated reads
        if flags[10] == "1": continue

        # skip if below the minimum mapping quality
        if (read.mapq < mapq_thres): continue


        bamfile_out.write(read)


def exon_base_count(input_file, output_file):

    exon2count = {}
    hIN = open(input_file, 'r')
    hOUT = open(output_file, 'w')

    for line in hIN:
        F = line.rstrip('\n').split('\t')
        if int(F[18]) == 0: continue

        exon = '\t'.join(F[12:18])
        if exon in exon2count:
            exon2count[exon] = exon2count[exon] + int(F[18])
        else:
            exon2count[exon] = int(F[18])

    for exon in exon2count:
        print >> hOUT, exon + '\t' + str(exon2count[exon])

    hIN.close()
    hOUT.close()


def mapped_base_count(input_file, output_file):

    hIN = open(input_file, 'r')
    hOUT = open(output_file, 'w')

    count = 0    
    for line in hIN:
        F = line.rstrip('\n').split('\t')
        count = count + int(F[9])

    print >> hOUT, str(count)

    hIN.close()
    hOUT.close()
   


def ref_base_count(input_file, output_file):

    hIN = open(input_file, 'r')
    hOUT = open(output_file, 'w')

    ref2count = {}
    ref2len = {}

    for line in hIN:
        F = line.rstrip('\n').split('\t')

        refID = F[3]
        refID = re.sub(r'_\d+$', '', refID)
        symbol = F[4]

        if refID not in ref2count: ref2count[refID] = 0
        if refID not in ref2len: ref2len[refID] = 0
             
        ref2count[refID] = ref2count[refID] + int(F[6])
        ref2len[refID] = ref2len[refID] + int(F[2]) - int(F[1])

    for refID in ref2count:
        print >> hOUT, refID + '\t' + str(ref2count[refID]) + '\t' + str(ref2len[refID])
    
    hIN.close()
    hOUT.close()
 
