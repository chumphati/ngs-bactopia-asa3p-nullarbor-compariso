#!/bin/bash
#commandes a executer dans le container
rm -rf /app/results
nullarbor.pl --name lactis --ref /app/data/LAC460_ref.fasta --input /app/input_file.tsv --outdir /app/results_test2 --trim
cd /app/results_test2 && make -j 4