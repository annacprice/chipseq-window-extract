#!/usr/bin/env python3

import pandas as pd
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

    # use biopython to parse the fasta file
    for seq_rec in SeqIO.parse('testdata/genome.fasta', 'fasta'):
        genome = seq_rec.seq

    return genome

def buildFASTA(genome, seqName, startCoord, endCoord):
    # build FASTA file with sequence information in the headers
    
    # write fasta file
    with open('testdata/output.fasta', 'w') as write_file:
        for name, coord1, coord2 in zip(seqName, startCoord, endCoord):
            FASTAhead = ">{0}|{1}|{2}".format(name, coord1, coord2)
            write_file.write(FASTAhead + '\n')
            seqWin = genome[coord1:coord2]
            seqWin = str(seqWin)
            # chunk sequence into lengths of 50
            seq50 = [seqWin[i:i+50] for i in range(0, len(seqWin), 50)]
            for elem in seq50:
                write_file.write(elem + '\n')


def main():
    seqName, startCoord, endCoord = TSVextract()
    genome = genomeParser()
    buildFASTA(genome, seqName, startCoord, endCoord)

if __name__ == "__main__":
    main()
