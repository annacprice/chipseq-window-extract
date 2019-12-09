#!/usr/bin/env python3

import pandas as pd
from Bio import SeqIO
import argparse
import csv
from itertools import groupby

def TSVextract(inputTSV, colSeq, colStart, colEnd):
    # extract columns from the tsv
    
    # reset column numbers for pandas (counts from 0)
    colSeq = int(colSeq) - 1
    colStart = int(colStart) - 1
    colEnd = int(colEnd) - 1

    # load tsv, set header to None
    tsv = pd.read_csv(inputTSV, sep='\t', header=None)

    # create an array for each column
    seqName = tsv.values[:,int(colSeq)]
    startCoord = tsv.values[:,int(colStart)]
    endCoord = tsv.values[:,int(colEnd)]

    return seqName, startCoord, endCoord

def genomeParser(chro, inputREF):
    # save the reference genome to biopython Seq object

    genomePath = inputREF + "/" + chro + ".fasta"
    # use biopython to parse the reference fasta file
    for seq_rec in SeqIO.parse(genomePath, 'fasta'):
        genome = seq_rec.seq

    return genome

def buildFASTA(chro, genome, seqName, startCoord, endCoord, outputFASTA):
    # build FASTA file with sequence information in the headers
    
    # write fasta file
    filepath = outputFASTA + "/" + chro + "_windows" + ".fasta"
    with open(filepath, 'w') as write_file:
        for name, coord1, coord2 in zip(seqName, startCoord, endCoord):
            FASTAhead = ">{0}|{1}|{2}".format(name, int(coord1), int(coord2))
            write_file.write(FASTAhead + '\n')
            seqWin = genome[int(coord1):int(coord2)]
            seqWin = str(seqWin)
            # convert sequence to uppercase
            seqWin = seqWin.upper()
            # chunk sequence into lengths of 50
            seq50 = [seqWin[i:i+50] for i in range(0, len(seqWin), 50)]
            for elem in seq50:
                write_file.write(elem + '\n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--input-tsv", dest="inputTSV", required=True, \
                        help="Path to the input chip-seq tsv")
    parser.add_argument("-r", "--input-ref", dest="inputREF", required=True, \
                        help="Path to the directory where the reference chromosomes are")
    parser.add_argument("-o", "--output-dir", dest="outputFASTA", required=True, \
                        help="Output directory path for the generated fasta")
    parser.add_argument("-i", "--col-name", dest="colName", required=True, \
                        help="Column number for the chromosome name")
    parser.add_argument("-s", "--col-start", dest="colStart", required=True, \
                        help="Column number for the start coordinate of the window")
    parser.add_argument("-e", "--col-end", dest="colEnd", required=True, \
                        help="Column number for the end coordinate of the window")
                        
    args = parser.parse_args()
    inputTSV = args.inputTSV
    inputREF = args.inputREF
    outputFASTA = args.outputFASTA
    colName = args.colName
    colStart = args.colStart
    colEnd = args.colEnd
    
    # split input tsv by chromosome
    csv_reader = csv.reader(open(inputTSV), delimiter="\t")
    # skip header
    next(csv_reader)
    for chro, rows in groupby(csv_reader,
                             lambda row: row[int(colName)-1]):
        with open("%s.tsv" % chro, "w") as output:
            for row in rows:
                output.write("\t".join(row) + "\n")
        seqName, startCoord, endCoord = TSVextract("%s.tsv" % chro, colName, colStart, colEnd)
        genome = genomeParser(chro, inputREF)
        buildFASTA(chro, genome, seqName, startCoord, endCoord, outputFASTA)

if __name__ == "__main__":
    main()
