#!/usr/bin/env python3

import pandas as pd
import re
from Bio import SeqIO


def TSVextract():
    # extract columns from the tsv

    # load tsv
    tsv = pd.read_csv('testdata/chipseq.tsv', sep='\t')

    # create an array for each column
    seqName = tsv['seqnames'].values
    startCoord = tsv['start'].values
    endCoord = tsv['end'].values

    return seqName, startCoord, endCoord

def genomeParser():
    # save the reference genome to biopython Seq object

    for seq_rec in SeqIO.parse('testdata/genome.fasta', 'fasta'):
        genome = seq_rec.seq

    return genome

def main():
    seqName, startCoord, endCoord = TSVextract()
    genome = genomeParser()


if __name__ == "__main__":
    main()
