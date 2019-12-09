# **chipseq-window-extract**
Extracts chip-seq windows from a reference genome and builds a fasta file.

## **Requirements**
Requires python 3.x

The following python packages are prerequisites:
- pandas
- biopython

## **Usage**
```
usage: chipWinExtract.py [-h] -t INPUTTSV -r INPUTREF -o OUTPUTFASTA -i COLSEQ
                         -s COLSTART -e COLEND

optional arguments:
  -h, --help            show this help message and exit
  -t INPUTTSV, --input-tsv INPUTTSV
                        Path to the input tsv
  -r INPUTREF, --input-ref INPUTREF
                        Path to directory of the reference genome
  -o OUTPUTFASTA, --output-fasta OUTPUTFASTA
                        Path for the directory for the output fasta
  -i COLSEQ, --col-seq COLSEQ
                        Column number for the chromosome name
  -s COLSTART, --col-start COLSTART
                        Column number for the start coordinate of the window
  -e COLEND, --col-end COLEND
                        Column number for the end coordinate of the window

```

## **Examples**
chipWinExtract.py requires an input chip-seq tsv file with no header, with columns for the name of each chromosome and the start and end window coordinates. You will also need the corresponding reference chromosomes to extract the sequence windows from. It splits the input tsv by chromosome, then creates a fasta file for each chromosome. The name of the chromosome in the tsv file should be the same as the reference chromosome, which is assumed to have the file extension .fasta.

E.g. to run for the data in testdata:
```
python chipWinExtract.py -t testdata/chipseq.tsv -r testdata -o testdata -i 1 -s 2 -e 3
```
this reproduces testdata/chr1_windows.fasta and testdata/chr2_windows.fasta.
