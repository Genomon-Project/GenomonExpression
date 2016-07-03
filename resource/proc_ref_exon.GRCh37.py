#! /usr/bin/env python

import sys, gzip

inputFile = sys.argv[1]
GRCh37_assembly_file = sys.argv[2]

hg2grch = {}
with open(GRCh37_assembly_file, 'r') as hin:
    for line in hin:
        if line.startswith('#'): continue
        F = line.rstrip('\n\r').split('\t')
        if F[4].startswith('CM'):
            hg2grch[F[9]] = F[2]
        else:
            hg2grch[F[9]] = F[4]

hIN = gzip.open(inputFile, 'r')
for line in hIN:
    F = line.rstrip('\n').split('\t')

    if F[2] not in hg2grch: 
        print >> sys.stderr, "no chr name in GRCh37 assembly file"
        sys.exit(1)

    chr = hg2grch[F[2]]
    starts = F[9].split(',')
    ends = F[10].split(',')
    strand = F[3]
    exonNum = int(F[8])
    gene = F[1]
    symbol = F[12]

    chr = chr.replace('chr', '')

    for i in range(0, len(starts) - 1):
        key = chr + '\t' + starts[i] + '\t' + ends[i]
        if strand == "+":
            print key + '\t' + gene + "_" + str(i) + '\t' + symbol + '\t' + "+"
        else:
            print key + '\t' + gene + "_" + str(exonNum - i - 1) + '\t' + symbol + '\t' + "-"

hIN.close()


