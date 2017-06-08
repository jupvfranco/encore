import sys
import numpy as np
import matplotlib.pyplot as plt

#plt.style.use('bmh')
cores = [2, 4, 8, 16, 32, 64]

def plot(ax, first, second, name, label2):
  ax.plot(cores, first, 'bo-', label="basic")
  ax.plot(cores, second, 'r^-', label=label2)
  ax.set_title(name+ ' in Encore')
  ax.set_xlabel('#cores', fontsize=16)
  ax.set_ylabel('time (sec)', fontsize=16)

def finalisePlot(bm):
  plt.legend(loc='best', shadow=True, fontsize=16)
  plt.savefig(bm + '_scalability.pdf', format='pdf', pad_inches=0, bbox_inches='tight')

def getSecFromMinutes(t):
  """ 0:04.67"""
  aux=t.split(":")
  minutes=int(aux[0])
  sms=float(aux[1])
  r= float(minutes*60) + sms
  return r

def getSecFromMS(t):
  """3882.501"""
  return float(t)/1000

def read_file(fn):
  with open(fn) as f:
    return f.readlines()

def newRun(di, cores, tt):
  t = di.get(cores, list())
  t.append(tt)
  di[cores] = t

def final_numbers(results):
  times=[]
  for cc in cores:
    xs = results.get(cc)
    # Remove two worse times from the 12 executions
    xs.remove(max(xs))
    xs.remove(max(xs))
    times.append(np.average(xs))
  return times

def parse_encore(fn):
  """Cores: 2 :: Input:  :: Iteration: 4 :: Time: 0:09.03"""
  results={} # cores --> list of times
  for line in read_file(fn):
    words=line.split(" :: ")
    cc=int(words[0].split(" ")[1])
    iteration=int(words[2].split(" ")[1])
    tt=getSecFromMinutes(words[3].split(" ")[1])
    newRun(results, cc, tt)
  return final_numbers(results)


def parseAndPlot(ax, first_path, second_path, bm, label2):
  first=parse_encore(first_path)
  second=parse_encore(second_path)
  plot(ax, first, second, bm, label2)

f, ax = plt.subplots(1, 1)
first_loc = sys.argv[1]
second_loc= sys.argv[2]
benchmark = sys.argv[3]
label2 = sys.argv[4]

parseAndPlot(ax, first_loc, second_loc, benchmark, label2)
finalisePlot(benchmark)
