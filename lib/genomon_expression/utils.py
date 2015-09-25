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

    for exon in sorted(exon2count):
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

    hIN.close()
   
    print >> hOUT, str(count)



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
        ID = refID + '\t' + symbol

        if ID not in ref2count: ref2count[ID] = 0
        if ID not in ref2len: ref2len[ID] = 0
             
        ref2count[ID] = ref2count[ID] + int(F[6])
        ref2len[ID] = ref2len[ID] + int(F[2]) - int(F[1])

    for ID in sorted(ref2count):
        print >> hOUT, ID + '\t' + str(ref2len[ID]) + '\t' + str(ref2count[ID])
    
    hIN.close()
    hOUT.close()


def sym_base_count(input_file, output_file):

    hIN = open(input_file, 'r')
    hOUT = open(output_file, 'w')

    sym2exp = {}
    for line in hIN:
        F = line.rstrip('\n').split('\t')
        symbol = F[1]

        if symbol not in sym2exp:
            if F[2] > 0 and F[3] > 0:
                sym2exp[symbol] = F[2] + '\t' + F[3]

        else:

            temp = sym2exp[symbol].split('\t')
            tempV = float(temp[1]) / float(temp[0])

            if F[2] > 0 and F[3] > 0 and float(F[3]) / float(F[2]) > tempV:
                sym2exp[symbol] = F[2] + '\t' + F[3]

    for symbol in sorted(sym2exp):
        print >> hOUT, symbol + '\t' + str(sym2exp[symbol])

    hIN.close() 
    hOUT.close()


def sym_fkpm(input_file, output_file, mapped_base_count_file):

    hIN = open(mapped_base_count_file, 'r')
    mapped_base_count = hIN.readline().rstrip('\n')
    hIN.close()

    hIN = open(input_file, 'r')
    hOUT = open(output_file, 'w')
  
    for line in hIN:
        F = line.rstrip('\n').split('\t')
        fkpm = float(int(F[2]) * 1000 * 1000000) / float(int(mapped_base_count) * int(F[1]))
        print >> hOUT, F[0] + '\t' + str(round(fkpm, 3))

    hIN.close()
    hOUT.close()

