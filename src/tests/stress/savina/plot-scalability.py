import sys
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('bmh')
cores = [2, 4, 8, 16, 32, 64]

def plot(ax, encore, akka, name):
  ax.plot(cores, encore, 'bo-', label="Encore")
#  ax.plot(cores, akka, 'r^-', label="Akka")
  ax.set_title(name)
  ax.set_xlabel('#cores', fontsize=16)
  ax.set_ylabel('time (millisec)', fontsize=16)

def finalisePlot(bm):
  plt.legend(loc='best', shadow=True, fontsize=16)
  plt.savefig(bm + '_scalability.pdf', format='pdf', pad_inches=0, bbox_inches='tight') 

def getMilliSec(t):
  """ 0:04.67"""
  aux=t.split(":")
  minutes=int(aux[0])
  sms=float(aux[1])
  r= float(minutes*60) + sms
  return r

def read_file(fn):
  with open(fn) as f:
    return f.readlines()

def newRun(di, cores, tt):
  t = di.get(cores, list())
  t.append(tt)    
  di[cores] = t 

def parse_encore(fn): 
  """Cores: 2 :: Input:  :: Iteration: 4 :: Time: 0:09.03"""
  results={} # cores --> list of times
  for line in read_file(fn):
    words=line.split(" :: ")
    cc=int(words[0].split(" ")[1])
    iteration=int(words[2].split(" ")[1])
    tt=getMilliSec(words[3].split(" ")[1])
    newRun(results, cc, tt)
  """construct list of times"""
  times=[]
  for cc in cores:
    times.append(np.average(results.get(cc)))
  return times

def parse_akka(fn):
  return list()

def parseAndPlot(ax, encore_path, akka_path, bm):
  encore=parse_encore(encore_path + '/result.txt')
  akka=parse_akka(akka_path + '/result.txt')
  plot(ax, encore, akka, bm)

f, ax = plt.subplots(1, 1)
akka_loc='' # TODO
enc_loc = sys.argv[1]
benchmark = sys.argv[2]

parseAndPlot(ax, enc_loc, akka_loc, benchmark)
finalisePlot(benchmark)
