#!/bin/bash

while read x
do
python chipWinExtract.py -t testdata/"${x}".tsv -r testdata/"${x}".fasta -o testdata/"${x}"_windows.fasta -i 1 -s 2 -e 3
done < testdata/chr_list.txt
