#!/bin/bash
######## README:
## If you are about to modify this script, it is because you have
## added a new benchmark and you want to plot Encore and Akka
## results for that benchmark. In that case, please add a line:
##    "<path to Encore logs>;<path to Akka logs>;<benchmark name>""
## to the following list. No Spaces!
########

logs=(
  "1.pingpong/result.txt;_AkkaResults/pingpong.PingPongAkkaActorBenchmark.result.txt;1.pingpong"
  "2.ThreadRing/result.txt;_AkkaResults/threadring.ThreadRingAkkaActorBenchmark.result.txt;2.ThreadRing"
  "3.Counting/result.txt;_AkkaResults/count.CountingAkkaActorBenchmark.result.txt;3.Counting"
  "6.Fib/result.txt;_AkkaResults/fib.FibonacciAkkaActorBenchmark.result.txt;6.Fib"
  "7.Chameneos/result.txt;_AkkaResults/chameneos.ChameneosAkkaActorBenchmark.result.txt;7.Chameneos"
  "8.Big/result.txt;_AkkaResults/big.BigAkkaActorBenchmark.result.txt;8.Big"
  "9.concdict/result.txt;_AkkaResults/concdict.DictionaryAkkaActorBenchmark.result.txt;9.concdict"
  "11.BndBuffer/result.txt;_AkkaResults/bndbuffer.ProdConsAkkaActorBenchmark.result.txt;11.BndBuffer"
  "12.DiningPhilosophers/result.txt;_AkkaResults/bndbuffer.ProdConsAkkaActorBenchmark.result.txt;12.DiningPhilosophers"
  "12.DiningPhilosophersBusy/result.txt;_AkkaResults/bndbuffer.ProdConsAkkaActorBenchmark.result.txt;12.DiningPhilosophersBusy"
  "12.DiningPhilosophers_Hot/result.txt;_AkkaResults/bndbuffer.ProdConsAkkaActorBenchmark.result.txt;12.DiningPhilosophersHot"
  "21.ParallelQuickSort/result.txt;_AkkaResults/quicksort.QuickSortAkkaActorBenchmark.result.txt;21.ParallelQuickSort"
  "25.Sieve/result.txt;_AkkaResults/sieve.SieveAkkaActorBenchmark.result.txt;25.Sieve"
  "28.TrapezoidalApproximation/result.txt;_AkkaResults/trapezoid.TrapezoidalAkkaActorBenchmark.result.txt;28.TrapezoidalApproximation"
  "29.PiPrecision/result.txt;_AkkaResults/piprecision.PiPrecisionAkkaActorBenchmark.result.txt;29.PiPrecision"
)

for l in ${logs[@]}
do :
  args=$(echo $l | tr ';' '\n')
  echo "***** " ${args[@]}
  python plot-scalability.py ${args[@]}
done
