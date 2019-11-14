#!/usr/bin/env python3

import pandas as pd
from Bio import SeqIO
import argparse

def TSVextract(inputTSV, colSeq, colStart, colEnd):
    # extract columns from the tsv

    # load tsv, skip first line and set header to None
    tsv = pd.read_csv(inputTSV, sep='\t', skiprows=[0], header=None)

    # create an array for each column
    seqName = tsv.values[:,int(colSeq)]
    startCoord = tsv.values[:,int(colStart)]
    endCoord = tsv.values[:,int(colEnd)]

    return seqName, startCoord, endCoord

def genomeParser(inputREF):
    # save the reference genome to biopython Seq object

    # use biopython to parse the reference fasta file
    for seq_rec in SeqIO.parse(inputREF, 'fasta'):
        genome = seq_rec.seq

    return genome

def buildFASTA(genome, seqName, startCoord, endCoord, outputFASTA):
    # build FASTA file with sequence information in the headers
    
    # write fasta file
    with open(outputFASTA, 'w') as write_file:
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--input-tsv", dest="inputTSV", required=True, \
                        help="Path to the input tsv")
    parser.add_argument("-r", "--input-ref", dest="inputREF", required=True, \
                        help="Path to the reference genome")
    parser.add_argument("-o", "--output-fasta", dest="outputFASTA", required=True, \
                        help="Path for the output fasta")
    parser.add_argument("-i", "--col-seq", dest="colSeq", required=True, \
                        help="Column number for the sequence ID")
    parser.add_argument("-s", "--col-start", dest="colStart", required=True, \
                        help="Column number for the start coordinate of the window")
    parser.add_argument("-e", "--col-end", dest="colEnd", required=True, \
                        help="Column number for the end coordinate of the window")
                        
    args = parser.parse_args()
    inputTSV = args.inputTSV
    inputREF = args.inputREF
    outputFASTA =args.outputFASTA
    colSeq = args.colSeq
    colStart = args.colStart
    colEnd = args.colEnd
    
    seqName, startCoord, endCoord = TSVextract(inputTSV, colSeq, colStart, colEnd)
    genome = genomeParser(inputREF)
    buildFASTA(genome, seqName, startCoord, endCoord, outputFASTA)

if __name__ == "__main__":
    main()
