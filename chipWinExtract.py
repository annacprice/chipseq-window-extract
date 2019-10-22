#!/usr/bin/env python3

import pandas as pd

def TSVextract():

    # load tsv
    tsv = pd.read_csv('testdata/chipseq.tsv', sep='\t')

    # create an array for each column
    seqName = tsv['seqnames'].values
    startCoord = tsv['start'].values
    endCoord = tsv['end'].values

def main():
    TSVextract()

if __name__ == "__main__":
    main()
