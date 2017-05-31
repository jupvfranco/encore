#!/bin/bash

# compile benchmark before
encorec=./../../../../release/encorec
main=$(grep "Main" * | tr ':' '\n' | grep ".enc")
$encorec $main -O3 --out-file main  

cores=( "0,8"
	    "0,8,16,24"
        "0,8,16,24,32,40,48,60"
        "0,8,16,24,32,40,48,60,2,10,18,26,34,42,50,58"
        "0,8,16,24,32,40,48,60,2,10,18,26,34,42,50,58,3,11,19,27,35,43,51,59,1,9,17,25,33,41,49,57"
        "0-63" ) 

RESULT="result.txt" 
rm $RESULT
input=$(cat "input.txt")

for c in ${cores[@]}
do : 
  numactl -C $c \
    /usr/bin/time -f "%E" -o "tmp" ./main $input
    elapsed=$(cat "tmp")
    echo $c" cores and input "$input" :: "$elapsed >> $RESULT
done

rm tmp 
rm main
