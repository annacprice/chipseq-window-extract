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
                        Path to the reference genome
  -o OUTPUTFASTA, --output-fasta OUTPUTFASTA
                        Path for the output fasta
  -i COLSEQ, --col-seq COLSEQ
                        Column number for the sequence ID
  -s COLSTART, --col-start COLSTART
                        Column number for the start coordinate of the window
  -e COLEND, --col-end COLEND
                        Column number for the end coordinate of the window
```
chipWinExtract.py requires an input chip-seq tsv file with the window coordinates and a reference genome.

## **Examples**
E.g. running for chr1 in testdata:
```
python chipWinExtract.py -t testdata/chr1.tsv -r testdata/chr1.fasta -o testdata/chr1_windows.fasta -i 1 -s 2 -e 3
```
reproduces testdata/chr1_windows.fasta.

To extract the windows for both chr1 and chr2 in testdata, you can use the bash wrapper script chipWinBash.sh:
```
./chipWinBash.sh
```
which reproduces testdata/chr1_windows.fasta and testdata/chr2_windows.fasta.

chipWinExtract.py expects only one chromosome per tsv file. To split your tsv file into separate chromosomes, you can use the following command in bash:
```
awk 'NR==1 { header=$0 } NR>1 { print (!a[$1]++? header ORS $0 : $0) >> (""$1".txt"); close(""$1".txt")}' input.tsv
```
