#!/bin/bash

# compile benchmark before
main=$(grep "Main" * | tr ':' '\n' | grep ".enc")
../../../../../release/encorec $main -O3 --out-file main  

cores=( "0,8"
	"0,8,16,24"
        "0,8,16,24,32,40,48,60"
        "0,8,16,24,32,40,48,60,2,10,18,26,34,42,50,58"
        "0,8,16,24,32,40,48,60,2,10,18,26,34,42,50,58,3,11,19,27,35,43,51,59,1,9,17,25,33,41,49,57"
        "0-63" ) 

REPETITION=12
RESULT="result.txt" 
rm $RESULT
input=$(cat "input.txt")

ncores=2
for c in ${cores[@]}
do : 
  it=1
  while [ $it -le $REPETITION ]
  do :
    numactl -C $c \
      /usr/bin/time -f "%E" -o "tmp" ./main $input
      elapsed=$(cat "tmp")
      echo "Cores: "$ncores" :: Input: "$input" :: Iteration: "$it" :: Time: "$elapsed >> $RESULT
    it=$[$it + 1]
  done
  ncores=$[$ncores + $ncores]
done

rm tmp 
rm main
