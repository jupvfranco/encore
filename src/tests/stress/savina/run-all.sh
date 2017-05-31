#!/bin/bash

benchmarks=$(ls -I "*.md" -I "*.sh" -I "Makefile")
for bm in ${benchmarks[@]}
do : 
  echo $bm 
  cd $bm
  bash ../run-scalability.sh
  cd ..
done

ls  */result.txt

