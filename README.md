# **chipseq-window-extract**
Extracts chip-seq windows from reference chromosomes and builds a fasta file for each chromosome.

## **Requirements**
Requires python 3.x

The following python packages are prerequisites:
- biopython

## **Usage**
```
usage: chipWinExtract.py [-h] -t INPUTTSV -r INPUTREF -o OUTPUTFASTA -i
COLNAME -s COLSTART -e COLEND

optional arguments:
    -h, --help            show this help message and exit
    -t INPUTTSV, --input-tsv INPUTTSV
                          Path to the input chip-seq tsv
    -r INPUTREF, --input-ref INPUTREF
                          Path to the directory where the reference chromosomes are
    -o OUTPUTFASTA, --output-dir OUTPUTFASTA
                          Output directory path for the generated fasta files
    -i COLNAME, --col-name COLNAME
                          Column number for the chromosome name
    -s COLSTART, --col-start COLSTART
                          Column number for the start coordinate of the window
    -e COLEND, --col-end COLEND
                          Column number for the end coordinate of the window
    -c, --concat-fasta    Concatenate the final fasta files into one file

```
chipWinExtract.py requires an input chip-seq tsv file, with columns for the name of each chromosome and the start and end window coordinates. You will also need the corresponding reference chromosomes to extract the sequence windows from. 

It splits the input tsv by chromosome, then creates a fasta file for each chromosome's extracted windows. The name of the chromosome in the tsv file should be the same as the reference chromosome, which is assumed to have the file extension .fa* (e.g. .fa or .fasta).

## **Examples**
E.g. to run for the data in testdata:
```
python chipWinExtract.py -t testdata/chipseq.tsv -r testdata/ref_chromosomes -o testdata/extracted_windows -i 1 -s 2 -e 3
```
this reproduces testdata/extracted_windows/chr1_windows.fasta and testdata/extracted_windows/chr2_windows.fasta.

You can also use the optional **--concat-fasta** flag to concatenate all the output fasta files into a single fasta.
