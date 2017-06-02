#!/bin/bash

benchmarks=$(ls -I "*.md" -I "*.sh" -I "Makefile" -I "*.py" -I "*.pdf")

for bm in ${benchmarks[@]}
do : 
  echo $bm 
  python plot-scalability.py $bm $bm
done

ls  */result.txt

