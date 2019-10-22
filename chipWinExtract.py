#!/usr/bin/env python3

import pandas as pd
import re
from Bio import SeqIO
import numpy as np

def TSVextract():
    # extract columns from the tsv

    # load tsv
    tsv = pd.read_csv('testdata/chipseq.tsv', sep='\t')

    # create an array for each column
    seqName = tsv['seqnames'].values
    startCoord = tsv['start'].values
    endCoord = tsv['end'].values

    return seqName, startCoord, endCoord

def genomeArray():
    # save the reference genome to an array

    genome = []
    for seq_rec in SeqIO.parse('testdata/genome.fasta', '''fasta'''):
        genome.append(seq_rec.seq)

    genomeArr = np.array(genome)

    return genomeArr

def main():
    seqName, startCoord, endCoord = TSVextract()
    genomeArr = genomeArray()


if __name__ == "__main__":
    main()
